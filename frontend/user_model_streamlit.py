import streamlit as st
import json
import logging

# Suppress Streamlit warnings
logging.getLogger("streamlit").setLevel(logging.ERROR)


# Define your Streamlit app
def user_model_forms():
    st.title("Userr Model Streamlit App")

    # Expandable Personal Information Section
    with st.expander("Personal Information"):
        st.subheader("Personal Information")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        age = st.number_input("Age", min_value=0)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])

        nationalities = [
            "Afghan",
            "Albanian",
            "Algerian",
            "American",
            "Andorran",
            "Angolan",
            "Antiguans",
            "Argentinean",
            "Armenian",
            "Australian",
            "Austrian",
            "Azerbaijani",
            "Bahamian",
            "Bahraini",
            "Bangladeshi",
            "Barbadian",
            "Barbudans",
            "Batswana",
            "Belarusian",
            "Belgian",
            "Belizean",
            "Beninese",
            "Bhutanese",
            "Bolivian",
            "Bosnian",
            "Brazilian",
            "British",
            "Bruneian",
            "Bulgarian",
            "Burkinabe",
            "Burmese",
            "Burundian",
            "Cambodian",
            "Cameroonian",
            "Canadian",
            "Cape Verdean",
            "Central African",
            "Chadian",
            "Chilean",
            "Chinese",
            "Colombian",
            "Comoran",
            "Congolese",
            "Costa Rican",
            "Croatian",
            "Cuban",
            "Cypriot",
            "Czech",
            "Danish",
            "Djibouti",
            "Dominican",
            "Dutch",
            "East Timorese",
            "Ecuadorean",
            "Egyptian",
            "Emirian",
            "Equatorial Guinean",
            "Eritrean",
            "Estonian",
            "Ethiopian",
            "Fijian",
            "Filipino",
            "Finnish",
            "French",
            "Gabonese",
            "Gambian",
            "Georgian",
            "German",
            "Ghanaian",
            "Greek",
            "Grenadian",
            "Guatemalan",
            "Guinea-Bissauan",
            "Guinean",
            "Guyanese",
            "Haitian",
            "Herzegovinian",
            "Honduran",
            "Hungarian",
            "I-Kiribati",
            "Icelander",
            "Indian",
            "Indonesian",
            "Iranian",
            "Iraqi",
            "Irish",
            "Israeli",
            "Italian",
            "Ivorian",
            "Jamaican",
            "Japanese",
            "Jordanian",
            "Kazakhstani",
            "Kenyan",
            "Kittian and Nevisian",
            "Kuwaiti",
            "Kyrgyz",
            "Laotian",
            "Latvian",
            "Lebanese",
            "Liberian",
            "Libyan",
            "Liechtensteiner",
            "Lithuanian",
            "Luxembourger",
            "Macedonian",
            "Malagasy",
            "Malawian",
            "Malaysian",
            "Maldivan",
            "Malian",
            "Maltese",
            "Marshallese",
            "Mauritanian",
            "Mauritian",
            "Mexican",
            "Micronesian",
            "Moldovan",
            "Monacan",
            "Mongolian",
            "Moroccan",
            "Mosotho",
            "Motswana",
            "Mozambican",
            "Namibian",
            "Nauruan",
            "Nepalese",
            "New Zealander",
            "Nicaraguan",
            "Nigerian",
            "Nigerien",
            "North Korean",
            "Northern Irish",
            "Norwegian",
            "Omani",
            "Pakistani",
            "Palauan",
            "Panamanian",
            "Papua New Guinean",
            "Paraguayan",
            "Peruvian",
            "Polish",
            "Portuguese",
            "Qatari",
            "Romanian",
            "Russian",
            "Rwandan",
            "Saint Lucian",
            "Salvadoran",
            "Samoan",
            "San Marinese",
            "Sao Tomean",
            "Saudi",
            "Scottish",
            "Senegalese",
            "Serbian",
            "Seychellois",
            "Sierra Leonean",
            "Singaporean",
            "Slovakian",
            "Slovenian",
            "Solomon Islander",
            "Somali",
            "South African",
            "South Korean",
            "Spanish",
            "Sri Lankan",
            "Sudanese",
            "Surinamer",
            "Swazi",
            "Swedish",
            "Swiss",
            "Syrian",
            "Taiwanese",
            "Tajik",
            "Tanzanian",
            "Thai",
            "Togolese",
            "Tongan",
            "Trinidadian or Tobagonian",
            "Tunisian",
            "Turkish",
            "Tuvaluan",
            "Ugandan",
            "Ukrainian",
            "Uruguayan",
            "Uzbekistani",
            "Venezuelan",
            "Vietnamese",
            "Welsh",
            "Yemenite",
            "Zambian",
            "Zimbabwean",
        ]

        nationality = st.multiselect("Nationality", nationalities)
        hobby = st.text_area("Hobby (comma separated)").split(",")
        languages = [
            "Afrikaans",
            "Albanian",
            "Amharic",
            "Arabic",
            "Armenian",
            "Azerbaijani",
            "Basque",
            "Belarusian",
            "Bengali",
            "Bosnian",
            "Bulgarian",
            "Catalan",
            "Cebuano",
            "Chichewa",
            "Chinese",
            "Corsican",
            "Croatian",
            "Czech",
            "Danish",
            "Dutch",
            "English",
            "Esperanto",
            "Estonian",
            "Filipino",
            "Finnish",
            "French",
            "Frisian",
            "Galician",
            "Georgian",
            "German",
            "Greek",
            "Gujarati",
            "Haitian Creole",
            "Hausa",
            "Hawaiian",
            "Hebrew",
            "Hindi",
            "Hmong",
            "Hungarian",
            "Icelandic",
            "Igbo",
            "Indonesian",
            "Irish",
            "Italian",
            "Japanese",
            "Javanese",
            "Kannada",
            "Kazakh",
            "Khmer",
            "Kinyarwanda",
            "Korean",
            "Kurdish",
            "Kyrgyz",
            "Lao",
            "Latin",
            "Latvian",
            "Lithuanian",
            "Luxembourgish",
            "Macedonian",
            "Malagasy",
            "Malay",
            "Malayalam",
            "Maltese",
            "Maori",
            "Marathi",
            "Mongolian",
            "Myanmar (Burmese)",
            "Nepali",
            "Norwegian",
            "Odia (Oriya)",
            "Pashto",
            "Persian",
            "Polish",
            "Portuguese",
            "Punjabi",
            "Romanian",
            "Russian",
            "Samoan",
            "Scots Gaelic",
            "Serbian",
            "Sesotho",
            "Shona",
            "Sindhi",
            "Sinhala",
            "Slovak",
            "Slovenian",
            "Somali",
            "Spanish",
            "Sundanese",
            "Swahili",
            "Swedish",
            "Tajik",
            "Tamil",
            "Tatar",
            "Telugu",
            "Thai",
            "Turkish",
            "Turkmen",
            "Ukrainian",
            "Urdu",
            "Uyghur",
            "Uzbek",
            "Vietnamese",
            "Welsh",
            "Xhosa",
            "Yiddish",
            "Yoruba",
            "Zulu",
        ]

        if "languages" not in st.session_state:
            st.session_state.languages = []

        # Display added languages
        for idx, lang in enumerate(st.session_state.languages):
            st.text(f"Language {idx + 1}: {lang['value']} ({lang['level']})")
            if st.button(f"Remove Language {idx + 1}", key=f"remove_language_{idx}"):
                st.session_state.languages.pop(idx)
                st.rerun()

        # Form to add new languages
        with st.form("add_language"):
            language = st.selectbox(
                "Select Spoken Language", [None] + languages, key="new_language"
            )
            level = st.selectbox(
                "Select Proficiency Level",
                ["A1", "A2", "B1", "B2", "C1", "C2"],
                key="new_level",
            )
            submitted = st.form_submit_button("Add Language")

            if submitted and language:
                st.session_state.languages.append({"value": language, "level": level})
                st.rerun()

        address = st.text_area("Address (comma separated geolocations)").split(",")

        interests_data = {
            "Film": [
                "Action",
                "Adventure",
                "Animation",
                "ChildrenAndFamily",
                "Classics",
                "Comedy",
                "Crime",
                "Documentary",
                "Drama",
                "Fantasy",
                "Foreign",
                "Horror",
                "Independent",
                "MartialArts",
                "MusicAndConcert",
                "Musicals",
                "Mystery",
                "Romance",
                "ScienceFiction",
                "Soaps",
                "SportsAndExercise",
                "Television",
                "Thriller",
                "War",
                "Westerns",
                "Other",
            ],
            "Music": [
                "Blues",
                "Celtic",
                "Children",
                "ChoralMusic",
                "Classical",
                "Composers",
                "Concerts",
                "Country",
                "Dance",
                "Electronic",
                "Folk",
                "HeavyMetal",
                "Hip-Hop",
                "HumorAndComedy",
                "Hymns",
                "Improvisation",
                "Indian",
                "Jazz",
                "Jewish",
                "Karaoke",
                "Lyrics",
                "MusicalInstruments",
                "Musicals",
                "NewAge",
                "Opera",
                "Popular",
                "Psychedelic",
                "PunkRock",
                "Quartets",
                "Ragtime",
                "Rap",
                "RaveCulture",
                "Reggae",
                "Religion",
                "Rhythm-n-Blues",
                "Rock",
                "SymphonyOrchestras",
                "WesternSwing",
                "WorldMusic",
            ],
            "Sports": [
                "Athletics",
                "AutomobileRacing",
                "Badminton",
                "Baseball",
                "Basketball",
                "Boating",
                "Boomerangs",
                "Bowling",
                "Boxing",
                "Chess",
                "Climbing",
                "Cricket",
                "Cycling",
                "Fencing",
                "FieldHockey",
                "FlyingDiscs",
                "Football",
                "Golf",
                "Gymnastics",
                "Hockey",
                "HorseRacing",
                "IceHockey",
                "IceSkating",
                "Karting",
                "Luge",
                "Motorcycles",
                "Olympics",
                "Rodeos",
                "Running",
                "Sailing",
                "ScubaDiving",
                "Skateboarding",
                "Skydiving",
                "Skating",
                "Skiing",
                "Snowboarding",
                "Soccer",
                "Softball",
                "Surfing",
                "Swimming",
                "TableTennis",
                "Tennis",
                "Triathlon",
                "Volleyball",
                "Windsurfing",
                "WinterSports",
                "Wrestling",
            ],
            "Recreation": [
                "Aquariums",
                "ArtGalleries",
                "Backpacking",
                "Beaches",
                "Bicycling",
                "BirdWatching",
                "Books",
                "Camping",
                "CardTricks",
                "Circus",
                "Collecting",
                "Crafts",
                "CrosswordPuzzles",
                "Dance",
                "Fairs",
                "Festivals",
                "Fireworks",
                "Fishing",
                "Fortune-telling",
                "Gambling",
                "Games",
                "Gardening",
                "Hiking",
                "Humor",
                "Hunting",
                "JigsawPuzzles",
                "Juggling",
                "Kites",
                "Lotteries",
                "MagicTricks",
                "Movies",
                "Museums",
                "Pets",
                "Photography",
                "Puppets",
                "Rafting",
                "Radio",
                "RailroadModels",
                "Television",
                "Toys",
                "Travel",
                "WordGames",
                "Zoos",
            ],
            "EnvironmentalTopics": [
                "AirPollution",
                "BiologicalDiversity",
                "ClimaticChangesAndGlobalWarming",
                "CoralReefs",
                "DesertsAndDesertification",
                "Disasters",
                "EndangeredSpecies",
                "EnergyConservation",
                "EnvironmentalEducation",
                "EnvironmentalHealth",
                "Fire",
                "ForestsAndDeforestation",
                "FuelCells",
                "GovernmentalPolicy",
                "Habitat",
                "HazardousSubstances",
                "HazardousWastes",
                "IndustrialSafety",
                "LightPollution",
                "Littering",
                "NaturalHistory",
                "NoisePollution",
                "NuclearEnergy",
                "Pesticides",
                "PestsAndDiseases",
                "PetroleumIndustry",
                "Ponds",
                "Protection",
                "RadioactiveWaste",
                "RainForests",
                "Recycling",
                "RenewableEnergy",
                "RuralDevelopment",
                "SolarEnergy",
                "Toxicology",
                "Water",
                "Weather",
                "Wetlands",
                "WildlifeConservation",
                "WindPower",
            ],
            "Science": [
                "Agriculture",
                "Animals",
                "Anthropology",
                "Archaeology",
                "Astronomy",
                "Biology",
                "Botany",
                "Chemistry",
                "Cloning",
                "ComputerScience",
                "Environment",
                "Evolution",
                "Expeditions",
                "Genetics",
                "Geography",
                "Geology",
                "HumanGenome",
                "Inventions",
                "LifeSciences",
                "Mathematics",
                "Medicine",
                "Microorganisms",
                "Molecules",
                "NatureSounds",
                "NobelPrizes",
                "NuclearEnergy",
                "Ontologies",
                "PhysicalSciences",
                "Physics",
                "Plants",
                "Psychology",
                "Scientists",
                "SemanticWeb",
                "Standardization",
                "Taxonomy",
                "Technology",
                "UbiquitousComputing",
                "UserModeling",
                "Weather",
                "Zoology",
            ],
            "PC-Games": [
                "Adventure",
                "Action",
                "Arcade",
                "BoardGames",
                "Children",
                "Fighting",
                "Platform",
                "Puzzle",
                "Racing",
                "Shoot-Em-Up",
                "Simulation",
                "Sports",
                "Strategy",
            ],
            # Add other categories here...
        }
        # Initialize session state for interests
        if "selected_interests" not in st.session_state:
            st.session_state.selected_interests = []
        st.subheader("Interests")

        # Select an interest category
        category = st.selectbox("Select Interest Category", [None] + list(interests_data.keys()), key="interest_category")

        if category:
            # Select interests within the chosen category
            options = interests_data[category]
            selected = st.multiselect(f"Select {category} Interests", options, key="interest_selection")
            
            if st.button("Add Interests"):
                for interest in selected:
                    if {"category": category, "interest": interest} not in st.session_state.selected_interests:
                        st.session_state.selected_interests.append({"category": category, "interest": interest})
                st.success(f"Added {len(selected)} interests.")

        # Display selected interests
        if st.session_state.selected_interests:
            st.write("### Selected Interests")
            indices_to_remove = []
            for idx, interest in enumerate(st.session_state.selected_interests):
                col1, col2 = st.columns([6, 1])
                with col1:
                    st.write(f"{idx + 1}. {interest['category']} - {interest['interest']}")
                with col2:
                    if st.button("Remove", key=f"remove_interest_{idx}"):
                        indices_to_remove.append(idx)

            # Remove items after iterating to avoid affecting the list during iteration
            if indices_to_remove:
                for idx in sorted(indices_to_remove, reverse=True):
                    st.session_state.selected_interests.pop(idx)
                st.success("Selected interest(s) removed.")

    # Expandable Accessibility Section
    with st.expander("Accessibility"):
        st.subheader("Accessibility")
        if "disabilities" not in st.session_state:
            st.session_state.disabilities = []

        for idx, disability in enumerate(st.session_state.disabilities):
            st.text(
                f"Disability {idx + 1}: {disability['name']}"
            )
            if st.button(
                f"Remove Disability {idx + 1}", key=f"remove_disability_{idx}"
            ):
                st.session_state.disabilities.pop(idx)
                st.rerun()

        with st.form("add_disability"):
            name = st.text_input("Disability Name", key="new_disability_name")
            description = st.text_input("Disability Description", key="new_disability_description")
            #affects = st.text_area(
            #    "Aspects Affected (comma separated)", key="new_disability_affects"
            #).split(",")
            submitted = st.form_submit_button("Add Disability")
            if submitted:
                st.session_state.disabilities.append({"name": name, "description": description})
                st.rerun()

    user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "gender": gender,
        "nationality": nationality,
        "hobby": hobby,
        "known_languages": st.session_state.languages,
        "disabilities": st.session_state.disabilities,
        "address": address,
        "interests": st.session_state.selected_interests
    }

    if st.button("Save and start bot"):
        with open("user_model.json", "w") as f:
            json.dump(user_data, f, indent=4)
        st.success("User data saved to user_data.json")
        st.session_state['user_model_saved'] = True
        st.rerun()


#if __name__ == "__main__":
   # main()
