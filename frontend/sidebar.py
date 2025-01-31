import base64
import json
import queue
from datetime import datetime

import streamlit as st

import os

from besser.bot.core.file import File
from besser.bot.core.message import MessageType, Message
from besser.bot.platforms.payload import PayloadEncoder, PayloadAction, Payload
from besser.bot.platforms.websocket.streamlit_ui.vars import WEBSOCKET, HISTORY, QUEUE, SUBMIT_AUDIO, SUBMIT_FILE


from jsonschema import validate, exceptions


def sidebar():
    ws = st.session_state[WEBSOCKET]

    with st.sidebar:
        if reset_button := st.button(label="Reset bot"):
            st.session_state[HISTORY] = []
            st.session_state[QUEUE] = queue.Queue()
            payload = Payload(action=PayloadAction.RESET)
            ws.send(json.dumps(payload, cls=PayloadEncoder))


        def submit_audio():
            # Necessary callback due to buf after 1.27.0 (https://github.com/streamlit/streamlit/issues/7629)
            # It was fixed for rerun but with _handle_rerun_script_request it doesn't work
            st.session_state[SUBMIT_AUDIO] = True

        voice_bytes_io = st.audio_input(label='Say something', on_change=submit_audio)
        if st.session_state[SUBMIT_AUDIO]:
            st.session_state[SUBMIT_AUDIO] = False
            voice_bytes = voice_bytes_io.read()
            # Encode the audio bytes to a base64 string
            voice_message = Message(t=MessageType.AUDIO, content=voice_bytes, is_user=True, timestamp=datetime.now())
            st.session_state.history.append(voice_message)
            voice_base64 = base64.b64encode(voice_bytes).decode('utf-8')
            payload = Payload(action=PayloadAction.USER_VOICE, message=voice_base64)
            try:
                ws.send(json.dumps(payload, cls=PayloadEncoder))
            except Exception as e:
                st.error('Your message could not be sent. The connection is already closed')

        def submit_file():
            # Necessary callback due to buf after 1.27.0 (https://github.com/streamlit/streamlit/issues/7629)
            # It was fixed for rerun but with _handle_rerun_script_request it doesn't work
            st.session_state[SUBMIT_FILE] = True

        uploaded_file = st.file_uploader("Upload User Profile (JSON)", accept_multiple_files=False, on_change=submit_file)
        user_model_available = False
        if os.path.exists("user_model.json"):
            user_model_available = True
        else:
            user_model_available = False

        # Label indicating upload status
        if uploaded_file:
            st.session_state[SUBMIT_FILE] = False
            file_name = uploaded_file.name.lower()
            # Check if the uploaded file is a JSON file
            if file_name.endswith(".json"):
                bytes_data = uploaded_file.read()
                try:
                    # Validate JSON format
                    json_data = json.loads(bytes_data.decode("utf-8"))
                    # Load the JSON schema
                    with open('json_schema.json', 'r') as schema_file:
                        schema = json.load(schema_file)
                    try:
                        validate(instance=json_data, schema=schema)
                        with open("user_model.json", "w", encoding="utf-8") as f:
                            json.dump(json_data, f, indent=4)
                        st.success("User profile uploaded successfully.")   
                        st.rerun()
                    except exceptions.ValidationError as ve:
                        print(f"Validation Error: {ve.message}")
                        st.error(f"Provided json does not conform to the schema. Validation Error: {ve.message}")
                    except exceptions.SchemaError as se:
                        print(f"Schema Error: {se.message}")
                    # Save the file locally as 'user_model.json'

                
                except json.JSONDecodeError:
                    st.error("Invalid JSON file. Please upload a properly formatted JSON file.")
            else:
                st.error("Please upload a JSON file.")
        if not user_model_available:
            # Inform the user to upload a file
            st.info("No user profile uploaded yet. Please upload a JSON file following the user model schema for a personalized experience.")
        else :
            st.info("User profile uploaded. You will now expereince a personalized chatbot experience.")
            if os.path.exists("user_model.json"):  # Use os to check file existence
                with open("user_model.json", "r", encoding="utf-8") as f:
                    json_data = f.read()

                # Streamlit download button
                st.download_button(
                    label="📥 Download user_model.json",
                    data=json_data,
                    file_name="user_model.json",
                    mime="application/json"
                )
            else:
                st.error("No JSON file found. Please upload one first.")
        # Add the "Enter User Model editor" button
        if user_model_button := st.button(label="Enter User Profile Editor"):
            # Define the functionality when the button is clicked
            st.session_state['user_model_editor'] = True
            st.success("User Profile mode activated")
            st.rerun()
