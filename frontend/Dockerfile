# Use the official Python 3.10.8 image from the Docker Hub
FROM python:3.11.9

# Set the working directory in the container
WORKDIR /app


# Install the dependencies specified in requirements.txt
RUN pip install besser-bot-framework==1.5.0
RUN pip install opencv-python==4.10.0.84
RUN pip install httpx==0.27.0
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y


# Copy the rest of your application code into the container at /app
COPY . .



# Replace the file
COPY streamlit_ui.py /usr/local/lib/python3.11/site-packages/besser/bot/platforms/websocket/streamlit_ui/streamlit_ui.py
COPY user_model_streamlit.py /usr/local/lib/python3.11/site-packages/besser/bot/platforms/websocket/streamlit_ui/user_model_streamlit.py
COPY llm.py /usr/local/lib/python3.11/site-packages/besser/bot/nlp/llm/llm.py

# Expose the port that the app runs on
EXPOSE 8765



CMD ["python", "./adapted_gpt.py"]