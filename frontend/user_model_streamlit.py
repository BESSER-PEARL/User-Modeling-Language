import streamlit as st
import json

json_schema = {}

with open("json_schema.json", "r") as file:
    json_schema = json.load(file)
# Function to render forms dynamically
def render_form(schema, data_key=None):
    if "type" not in schema:
        return st.error(data_key)
    elif "type" in schema and schema["type"] == "object":
        for key, value in schema["properties"].items():
            
            if "$ref" in value:
                # If it's a reference, create a nested form
                
                ref_name = value["$ref"].split("/")[-1]
                if "bility" in data_key:
                    print("we are in ")
                    print(key)
                    print(value)
                    print(ref_name)
                if ref_name == "Range":
                    name = f"{data_key}_{key}" if data_key else key
                    st.slider(f"{key}", min_value=0, max_value=100, value=-1, key=name)
                else:
                    
                    if "enum" in json_schema["definitions"][ref_name]:
                        st.selectbox(
                            key,
                            ["Select an option"] + json_schema["definitions"][ref_name]["enum"],
                            key=f"{data_key}_{key}"
                        )
                    else:
                        if ref_name not in st.session_state.visited_objects:
                            st.session_state.visited_objects.append(ref_name)
                            st.markdown(f"##### {key.capitalize()}")
                            name = f"{data_key}_{key}" if data_key else key
                            render_form(json_schema["definitions"][ref_name]["allOf"][0], name)
                    
            elif value["type"] == "string":
                st.text_input(f"{key.capitalize()}:", key=f"{data_key}_{key}")
            elif value["type"] == "integer":
                min_val = value.get("minimum", -1)
                max_val = value.get("maximum", 100)
                st.number_input(
                    f"{key.capitalize()}:", 
                    min_value=min_val, 
                    max_value=max_val, 
                    key=f"{data_key}_{key}"
                )
            elif value["type"] == "array":
                st.markdown(f"#### {key.capitalize()}")
                items = value.get("items", {})
                if "$ref" in items:
                    ref_name = items["$ref"].split("/")[-1]
                    if ref_name not in st.session_state.visited_objects:
                        st.markdown(f"Array of {ref_name}")
                        name = f"{data_key}_{key}" if data_key else key
                        if name not in st.session_state.arrays:
                            st.session_state.arrays[name] = []
                        for idx, item in enumerate(st.session_state.arrays.get(name)):
                            st.text(f"{ref_name} {idx + 1}: {item}")
                            if st.button(
                                f"Remove {ref_name} {idx + 1}", key=f"{ref_name}_{idx}"
                            ):
                                st.session_state.arrays[name].pop(idx)
                                st.rerun()
                        render_form(json_schema["definitions"][ref_name]["allOf"][0], name)
                        if st.button(f"Add {ref_name}", key=name):
                            new_object = {}
                            for item in json_schema["definitions"][ref_name]["allOf"][0]["properties"]:
                                if st.session_state.get(name+"_"+item) not in ["", "Select an option", -1]:
                                    new_object[item] = st.session_state.get(name+"_"+item)
                            st.markdown(new_object)
                            st.session_state.arrays[name].append(new_object)
                            st.rerun()
                                
                                
                else:
                    st.text_area(f"{key.capitalize()} (Array Items):", key=f"{data_key}_{key}")
    elif schema["type"] == "array":
        st.markdown(f"#### {data_key.capitalize()}")
        items = schema.get("items", {})
        if "$ref" in items:  
            ref_name = items["$ref"].split("/")[-1]
            if ref_name == "Range":
                name = data_key
                st.slider("Select a value", min_value=0, max_value=100, value=-1, key=name)
            else:
                if ref_name not in st.session_state.visited_objects:
                    st.markdown(f"Array of {ref_name}")
                    name = data_key
                    if name not in st.session_state.arrays:
                        st.session_state.arrays[name] = []
                    for idx, item in enumerate(st.session_state.arrays.get(name)):
                        st.text(f"{ref_name} {idx + 1}: {item}")
                        if st.button(
                            f"Remove {ref_name} {idx + 1}", key=f"{ref_name}_{idx}"
                        ):
                            st.session_state.arrays[name].pop(idx)
                            st.rerun()
                    render_form(json_schema["definitions"][ref_name]["allOf"][0], name)
                    if st.button(f"Add {ref_name}"):
                        new_object = {}
                        for item in json_schema["definitions"][ref_name]["allOf"][0]["properties"]:
                            if st.session_state.get(name+"_"+item) not in ["", "Select an option", -1]:
                                new_object[item] = st.session_state.get(name+"_"+item)
                        st.markdown(new_object)
                        st.session_state.arrays[name].append(new_object)
                        st.rerun()
    else:
        st.error(f"Unsupported type: {schema['type']}")


# Function to extract user input based on schema
def extract_user_data(schema, data_key=None):
    user_data = {}

    if "type" not in schema:
        return user_data
    elif "type" in schema and schema["type"] == "object":
        for key, value in schema["properties"].items():

            unique_key = f"{data_key}_{key}" if data_key else key
            if "$ref" in value:
                
                if "Range" in value["$ref"]:
                    user_data[key] = st.session_state.get(unique_key)
                
                else:
                    # If it's a reference, recurse into the referenced schema
                    ref_name = value["$ref"].split("/")[-1]
                    if "allOf" in json_schema["definitions"][ref_name]:
                        user_data[key] = extract_user_data(json_schema["definitions"][ref_name]["allOf"][0], unique_key)
                    elif "enum" in json_schema["definitions"][ref_name]:
                        user_data[key] = st.session_state.get(unique_key)
                    else:
                        nothing = "dldl"
                    
                    
            elif value["type"] == "string":
                user_data[key] = st.session_state.get(unique_key)
            elif value["type"] == "integer":
                if "culture" in unique_key:
                    st.error(data_key)
                user_data[key] = st.session_state.get(unique_key, -1)
            elif value["type"] == "array":
                user_data[key] = st.session_state.arrays.get(unique_key, [])
    elif schema["type"] == "array":
        user_data = st.session_state.arrays[unique_key]
    return user_data




def clean_json(obj):
    if isinstance(obj, dict):
        # Recursively clean dictionary values
        cleaned_dict = {
            k: clean_json(v)
            for k, v in obj.items()
            if clean_json(v) not in ["", "Select an option", -1, [], None]  # Ensure values are cleaned
        }
        # Return None if the dictionary is empty after cleaning
        return cleaned_dict if cleaned_dict else None

    elif isinstance(obj, list):
        # Recursively clean each item in the list
        cleaned_list = [clean_json(item) for item in obj]
        # Remove None values and empty dictionaries from the list
        cleaned_list = [item for item in cleaned_list if item not in ["", "Select an option", -1, [], None]]
        return cleaned_list if cleaned_list else None

    else:
        # Return None for values that should be removed
        return None if obj in ["", "Select an option", -1, [], None] else obj

def user_model_forms():
    # Load the JSON schema
    json_schema = {}

    with open("json_schema.json", "r") as file:
        json_schema = json.load(file)

    st.session_state.visited_objects = []
    if "arrays" not in st.session_state:
        st.session_state.arrays = {}
    # Main Streamlit app
    st.title("User Profile Editor")

    # Render the form
    user_schema = json_schema["definitions"]["User"]["allOf"][0]
    for category, category_schema in user_schema["properties"].items():
        with st.expander(category, expanded=False):
            if "$ref" in category_schema:
                ref_name = category_schema["$ref"].split("/")[-1]
                st.markdown(f"### Editing: {category}")
                render_form(json_schema["definitions"][ref_name]["allOf"][0], ref_name)
            else:
                render_form(category_schema, category)
    # Save button
    if st.button("Save JSON"):
        # Extract user data
        user_data = {}
        user_data["User"] = extract_user_data(user_schema)
        user_data = clean_json(user_data)
        if not user_data:
            st.error("Please fill in some data before saving.")
        else:
            # user_data = clean_json(user_data)
            # Save the data to a file
            with open("user_model.json", "w") as f:
                json.dump(user_data, f, indent=4)
        
            st.success("JSON data has been saved as user_data.json")
            st.json(user_data)  # Optionally display the JSON data in the app
            st.session_state['user_model_editor'] = False
            st.rerun()
