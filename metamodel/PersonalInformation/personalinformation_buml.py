# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    Constraint
)

# Enumerations
GenderEnum: Enumeration = Enumeration(
    name="GenderEnum",
    literals={
            EnumerationLiteral(name="Other"),
			EnumerationLiteral(name="Female"),
			EnumerationLiteral(name="Male")
    }
)

ScienceFieldEnum: Enumeration = Enumeration(
    name="ScienceFieldEnum",
    literals={
            EnumerationLiteral(name="Agriculture"),
			EnumerationLiteral(name="Evolution"),
			EnumerationLiteral(name="Weather"),
			EnumerationLiteral(name="NobelPrizes"),
			EnumerationLiteral(name="Genetics"),
			EnumerationLiteral(name="Zoology"),
			EnumerationLiteral(name="NatureSounds"),
			EnumerationLiteral(name="Geography"),
			EnumerationLiteral(name="NuclearEnergy"),
			EnumerationLiteral(name="PhysicalSciences"),
			EnumerationLiteral(name="Anthropology"),
			EnumerationLiteral(name="Ontologies"),
			EnumerationLiteral(name="Cloning"),
			EnumerationLiteral(name="Archaeology"),
			EnumerationLiteral(name="HumanGenome"),
			EnumerationLiteral(name="Biology"),
			EnumerationLiteral(name="Psychology"),
			EnumerationLiteral(name="Molecules"),
			EnumerationLiteral(name="Astronomy"),
			EnumerationLiteral(name="Inventions"),
			EnumerationLiteral(name="UbiquitousComputing"),
			EnumerationLiteral(name="Mathematics"),
			EnumerationLiteral(name="Scientists"),
			EnumerationLiteral(name="Standardization"),
			EnumerationLiteral(name="Botany"),
			EnumerationLiteral(name="LifeSciences"),
			EnumerationLiteral(name="SemanticWeb"),
			EnumerationLiteral(name="Chemistry"),
			EnumerationLiteral(name="Medicine"),
			EnumerationLiteral(name="Taxonomy"),
			EnumerationLiteral(name="Microorganisms"),
			EnumerationLiteral(name="Technology"),
			EnumerationLiteral(name="Animals"),
			EnumerationLiteral(name="ComputerScience"),
			EnumerationLiteral(name="Geology"),
			EnumerationLiteral(name="Environment"),
			EnumerationLiteral(name="Plants"),
			EnumerationLiteral(name="UserModeling"),
			EnumerationLiteral(name="Expeditions"),
			EnumerationLiteral(name="Physics")
    }
)

RecreationEnum: Enumeration = Enumeration(
    name="RecreationEnum",
    literals={
            EnumerationLiteral(name="Beaches"),
			EnumerationLiteral(name="Rafting"),
			EnumerationLiteral(name="Backpacking"),
			EnumerationLiteral(name="Fishing"),
			EnumerationLiteral(name="ArtGalleries"),
			EnumerationLiteral(name="Fireworks"),
			EnumerationLiteral(name="Museums"),
			EnumerationLiteral(name="Festivals"),
			EnumerationLiteral(name="BirdWatching"),
			EnumerationLiteral(name="Camping"),
			EnumerationLiteral(name="Movies"),
			EnumerationLiteral(name="Fortune-telling"),
			EnumerationLiteral(name="MagicTricks"),
			EnumerationLiteral(name="Games"),
			EnumerationLiteral(name="Pets"),
			EnumerationLiteral(name="Cycling"),
			EnumerationLiteral(name="Puppets"),
			EnumerationLiteral(name="Juggling"),
			EnumerationLiteral(name="Fairs"),
			EnumerationLiteral(name="WordGames"),
			EnumerationLiteral(name="Lotteries"),
			EnumerationLiteral(name="Crafts"),
			EnumerationLiteral(name="Collecting"),
			EnumerationLiteral(name="Hunting"),
			EnumerationLiteral(name="Circus"),
			EnumerationLiteral(name="Aquariums"),
			EnumerationLiteral(name="Humor"),
			EnumerationLiteral(name="Television"),
			EnumerationLiteral(name="CrosswordPuzzles"),
			EnumerationLiteral(name="Hiking"),
			EnumerationLiteral(name="Dance"),
			EnumerationLiteral(name="RailroadModels"),
			EnumerationLiteral(name="JigsawPuzzles"),
			EnumerationLiteral(name="Radio"),
			EnumerationLiteral(name="Books"),
			EnumerationLiteral(name="Kites"),
			EnumerationLiteral(name="Toys"),
			EnumerationLiteral(name="Gambling"),
			EnumerationLiteral(name="Zoos"),
			EnumerationLiteral(name="CardTricks"),
			EnumerationLiteral(name="Photography"),
			EnumerationLiteral(name="Gardening")
    }
)

MusicGenreEnum: Enumeration = Enumeration(
    name="MusicGenreEnum",
    literals={
            EnumerationLiteral(name="Celtic"),
			EnumerationLiteral(name="Electronic"),
			EnumerationLiteral(name="Improvisation"),
			EnumerationLiteral(name="NewAge"),
			EnumerationLiteral(name="Folk"),
			EnumerationLiteral(name="Hip-Hop"),
			EnumerationLiteral(name="Ragtime"),
			EnumerationLiteral(name="WesternSwing"),
			EnumerationLiteral(name="Opera"),
			EnumerationLiteral(name="HeavyMetal"),
			EnumerationLiteral(name="Psychedelic"),
			EnumerationLiteral(name="Blues"),
			EnumerationLiteral(name="WorldMusic"),
			EnumerationLiteral(name="Popular"),
			EnumerationLiteral(name="HumorAndComedy"),
			EnumerationLiteral(name="PunkRock"),
			EnumerationLiteral(name="Hymns"),
			EnumerationLiteral(name="Quartets"),
			EnumerationLiteral(name="Children"),
			EnumerationLiteral(name="Dance"),
			EnumerationLiteral(name="Indian"),
			EnumerationLiteral(name="ChoralMusic"),
			EnumerationLiteral(name="Composers"),
			EnumerationLiteral(name="Musicals"),
			EnumerationLiteral(name="Rap"),
			EnumerationLiteral(name="Jazz"),
			EnumerationLiteral(name="Classical"),
			EnumerationLiteral(name="Karaoke"),
			EnumerationLiteral(name="SymphonyOrchestras"),
			EnumerationLiteral(name="RaveCulture"),
			EnumerationLiteral(name="Jewish"),
			EnumerationLiteral(name="Religion"),
			EnumerationLiteral(name="Concerts"),
			EnumerationLiteral(name="Reggae"),
			EnumerationLiteral(name="Lyrics"),
			EnumerationLiteral(name="Country"),
			EnumerationLiteral(name="Rhythm-n-Blues"),
			EnumerationLiteral(name="MusicalInstruments"),
			EnumerationLiteral(name="Rock")
    }
)

SexualityEnum: Enumeration = Enumeration(
    name="SexualityEnum",
    literals={
            EnumerationLiteral(name="Heterosexual"),
			EnumerationLiteral(name="Other"),
			EnumerationLiteral(name="Homosexual"),
			EnumerationLiteral(name="Asexual"),
			EnumerationLiteral(name="Bisexual"),
			EnumerationLiteral(name="Pansexual")
    }
)

SportEnum: Enumeration = Enumeration(
    name="SportEnum",
    literals={
            EnumerationLiteral(name="Chess"),
			EnumerationLiteral(name="Skating"),
			EnumerationLiteral(name="Skiing"),
			EnumerationLiteral(name="IceHockey"),
			EnumerationLiteral(name="Skydiving"),
			EnumerationLiteral(name="AutomobileRacing"),
			EnumerationLiteral(name="Karting"),
			EnumerationLiteral(name="Soccer"),
			EnumerationLiteral(name="FlyingDiscs"),
			EnumerationLiteral(name="Surfing"),
			EnumerationLiteral(name="Baseball"),
			EnumerationLiteral(name="Gymnastics"),
			EnumerationLiteral(name="Sailing"),
			EnumerationLiteral(name="Golf"),
			EnumerationLiteral(name="Windsurfing"),
			EnumerationLiteral(name="Skateboarding"),
			EnumerationLiteral(name="Wrestling"),
			EnumerationLiteral(name="Fencing"),
			EnumerationLiteral(name="Cycling"),
			EnumerationLiteral(name="Rodeos"),
			EnumerationLiteral(name="Cricket"),
			EnumerationLiteral(name="Athletics"),
			EnumerationLiteral(name="Badminton"),
			EnumerationLiteral(name="Olympics"),
			EnumerationLiteral(name="Triathlon"),
			EnumerationLiteral(name="FieldHockey"),
			EnumerationLiteral(name="Motorcycles"),
			EnumerationLiteral(name="Football"),
			EnumerationLiteral(name="Tennis"),
			EnumerationLiteral(name="Running"),
			EnumerationLiteral(name="TableTennis"),
			EnumerationLiteral(name="Boxing"),
			EnumerationLiteral(name="ScubaDiving"),
			EnumerationLiteral(name="Volleyball"),
			EnumerationLiteral(name="IceSkating"),
			EnumerationLiteral(name="WinterSports"),
			EnumerationLiteral(name="Climbing"),
			EnumerationLiteral(name="Softball"),
			EnumerationLiteral(name="Luge"),
			EnumerationLiteral(name="Boomerangs"),
			EnumerationLiteral(name="Swimming"),
			EnumerationLiteral(name="Boating"),
			EnumerationLiteral(name="HorseRacing"),
			EnumerationLiteral(name="Basketball"),
			EnumerationLiteral(name="Hockey"),
			EnumerationLiteral(name="Bowling")
    }
)

PoliticalEnum: Enumeration = Enumeration(
    name="PoliticalEnum",
    literals={
            EnumerationLiteral(name="Sligthly Conservative"),
			EnumerationLiteral(name="Neutral"),
			EnumerationLiteral(name="Extremely Liberal"),
			EnumerationLiteral(name="Liberal"),
			EnumerationLiteral(name="Sligthly Liberal"),
			EnumerationLiteral(name="Extremely Conservative"),
			EnumerationLiteral(name="Conservative")
    }
)

FilmGenreEnum: Enumeration = Enumeration(
    name="FilmGenreEnum",
    literals={
            EnumerationLiteral(name="Fantasy"),
			EnumerationLiteral(name="Drama"),
			EnumerationLiteral(name="Westerns"),
			EnumerationLiteral(name="Documentary"),
			EnumerationLiteral(name="War"),
			EnumerationLiteral(name="Horror"),
			EnumerationLiteral(name="Thriller"),
			EnumerationLiteral(name="MartialArts"),
			EnumerationLiteral(name="Other"),
			EnumerationLiteral(name="Adventure"),
			EnumerationLiteral(name="Comedy"),
			EnumerationLiteral(name="Soaps"),
			EnumerationLiteral(name="Classics"),
			EnumerationLiteral(name="Television"),
			EnumerationLiteral(name="Romance"),
			EnumerationLiteral(name="Action"),
			EnumerationLiteral(name="Mystery"),
			EnumerationLiteral(name="ChildrenAndFamily"),
			EnumerationLiteral(name="Musicals"),
			EnumerationLiteral(name="Animation"),
			EnumerationLiteral(name="ScienceFiction"),
			EnumerationLiteral(name="SportsAndExercise"),
			EnumerationLiteral(name="Independent"),
			EnumerationLiteral(name="Crime"),
			EnumerationLiteral(name="MusicAndConcert")
    }
)

EnvironmentEnum: Enumeration = Enumeration(
    name="EnvironmentEnum",
    literals={
            EnumerationLiteral(name="Ponds"),
			EnumerationLiteral(name="Windpower"),
			EnumerationLiteral(name="EndangeredSpecies"),
			EnumerationLiteral(name="Habitat"),
			EnumerationLiteral(name="SolarEnergy"),
			EnumerationLiteral(name="BiologicalDiversity"),
			EnumerationLiteral(name="RadioactiveWaste"),
			EnumerationLiteral(name="CoralReefs"),
			EnumerationLiteral(name="NaturalHistory"),
			EnumerationLiteral(name="Water"),
			EnumerationLiteral(name="HazardousSubstances"),
			EnumerationLiteral(name="ClimaticChangesAndGlobalWarming"),
			EnumerationLiteral(name="IndustrialSafety"),
			EnumerationLiteral(name="RainForests"),
			EnumerationLiteral(name="Weather"),
			EnumerationLiteral(name="HazardousWastes"),
			EnumerationLiteral(name="RenewableEnergy"),
			EnumerationLiteral(name="DesertsAndDesertification"),
			EnumerationLiteral(name="Recycling"),
			EnumerationLiteral(name="LightPollution"),
			EnumerationLiteral(name="Disasters"),
			EnumerationLiteral(name="Littering"),
			EnumerationLiteral(name="RuralDevelopment"),
			EnumerationLiteral(name="Toxicology"),
			EnumerationLiteral(name="AirPollution"),
			EnumerationLiteral(name="EnergyConservation"),
			EnumerationLiteral(name="GovernmentPolicy"),
			EnumerationLiteral(name="NoisePollution"),
			EnumerationLiteral(name="EnvironmentalEducation"),
			EnumerationLiteral(name="Fire"),
			EnumerationLiteral(name="Protection"),
			EnumerationLiteral(name="NuclearEnergy"),
			EnumerationLiteral(name="EnvironmentalHealth"),
			EnumerationLiteral(name="PestsAndDiseases"),
			EnumerationLiteral(name="Wetlands"),
			EnumerationLiteral(name="Pesticides"),
			EnumerationLiteral(name="ForestsAndDeforestation"),
			EnumerationLiteral(name="WildlifeConservation"),
			EnumerationLiteral(name="PetroleumIndustry"),
			EnumerationLiteral(name="FuelCells")
    }
)

GameGenreEnum: Enumeration = Enumeration(
    name="GameGenreEnum",
    literals={
            EnumerationLiteral(name="Action"),
			EnumerationLiteral(name="Shoot-Em-Up"),
			EnumerationLiteral(name="Puzzle"),
			EnumerationLiteral(name="Simulation"),
			EnumerationLiteral(name="Strategy"),
			EnumerationLiteral(name="Adventure"),
			EnumerationLiteral(name="Arcade"),
			EnumerationLiteral(name="Platform"),
			EnumerationLiteral(name="Sports"),
			EnumerationLiteral(name="Children"),
			EnumerationLiteral(name="BoardGames"),
			EnumerationLiteral(name="Racing"),
			EnumerationLiteral(name="Fighting")
    }
)

# Classes
Music = Class(name="Music")
Science = Class(name="Science")
Film = Class(name="Film")
PersonalInformation = Class(name="PersonalInformation")
Hobby = Class(name="Hobby")
Sport = Class(name="Sport")
Other = Class(name="Other")
Recreation = Class(name="Recreation")
Environment = Class(name="Environment")
Interest = Class(name="Interest")
Topic = Class(name="Topic")
VideoGames = Class(name="VideoGames")

# Music class attributes and methods
Music_genres: Property = Property(name="genres", type=MusicGenreEnum)
Music.attributes={Music_genres}

# Science class attributes and methods
Science_fields: Property = Property(name="fields", type=ScienceFieldEnum)
Science.attributes={Science_fields}

# Film class attributes and methods
Film_genres: Property = Property(name="genres", type=FilmGenreEnum)
Film.attributes={Film_genres}

# PersonalInformation class attributes and methods
PersonalInformation_sexuality: Property = Property(name="sexuality", type=StringType)
PersonalInformation_gender: Property = Property(name="gender", type=GenderEnum)
PersonalInformation_age: Property = Property(name="age", type=StringType)
PersonalInformation_address: Property = Property(name="address", type=StringType)
PersonalInformation_politicalBelief: Property = Property(name="politicalBelief", type=StringType)
PersonalInformation_lastName: Property = Property(name="lastName", type=StringType)
PersonalInformation_firstName: Property = Property(name="firstName", type=StringType)
PersonalInformation_nationality_iso3166: Property = Property(name="nationality_iso3166", type=StringType)
PersonalInformation.attributes={PersonalInformation_sexuality, PersonalInformation_gender, PersonalInformation_age, PersonalInformation_address, PersonalInformation_politicalBelief, PersonalInformation_lastName, PersonalInformation_firstName, PersonalInformation_nationality_iso3166}

# Hobby class attributes and methods
Hobby_weeklyTime: Property = Property(name="weeklyTime", type=StringType)
Hobby.attributes={Hobby_weeklyTime}

# Sport class attributes and methods
Sport_disciplines: Property = Property(name="disciplines", type=SportEnum)
Sport.attributes={Sport_disciplines}

# Other class attributes and methods
Other_name: Property = Property(name="name", type=StringType)
Other_description: Property = Property(name="description", type=StringType)
Other.attributes={Other_name, Other_description}

# Recreation class attributes and methods
Recreation_types: Property = Property(name="types", type=RecreationEnum)
Recreation.attributes={Recreation_types}

# Environment class attributes and methods
Environment_topics: Property = Property(name="topics", type=EnvironmentEnum)
Environment.attributes={Environment_topics}

# Interest class attributes and methods

# Topic class attributes and methods

# VideoGames class attributes and methods
VideoGames_genres: Property = Property(name="genres", type=GameGenreEnum)
VideoGames.attributes={VideoGames_genres}

# Relationships
PersonalInformation_Interest_association_1: BinaryAssociation = BinaryAssociation(
    name="PersonalInformation_Interest_association_1",
    ends={
        Property(name="Interest_end", type=Interest, multiplicity=Multiplicity(0, 9999)),
        Property(name="PersonalInformation_end", type=PersonalInformation, multiplicity=Multiplicity(1, 1))
    }
)
Interest_Topic_association: BinaryAssociation = BinaryAssociation(
    name="Interest_Topic_association",
    ends={
        Property(name="Topic_end", type=Topic, multiplicity=Multiplicity(1, 1)),
        Property(name="Interest_end", type=Interest, multiplicity=Multiplicity(1, 1))
    }
)
PersonalInformation_Interest_association: BinaryAssociation = BinaryAssociation(
    name="PersonalInformation_Interest_association",
    ends={
        Property(name="PersonalInformation_end", type=PersonalInformation, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Interest_end", type=Interest, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_Environment_Topic = Generalization(general=Topic, specific=Environment)
gen_Recreation_Topic = Generalization(general=Topic, specific=Recreation)
gen_Sport_Topic = Generalization(general=Topic, specific=Sport)
gen_VideoGames_Topic = Generalization(general=Topic, specific=VideoGames)
gen_Music_Topic = Generalization(general=Topic, specific=Music)
gen_Hobby_Interest = Generalization(general=Interest, specific=Hobby)
gen_Film_Topic = Generalization(general=Topic, specific=Film)
gen_Other_Topic = Generalization(general=Topic, specific=Other)
gen_Science_Topic = Generalization(general=Topic, specific=Science)

# Domain Model
domain_model = DomainModel(
    name="Generated Model",
    types={Music, Science, Film, PersonalInformation, Hobby, Sport, Other, Recreation, Environment, Interest, Topic, VideoGames, GenderEnum, ScienceFieldEnum, RecreationEnum, MusicGenreEnum, SexualityEnum, SportEnum, PoliticalEnum, FilmGenreEnum, EnvironmentEnum, GameGenreEnum},
    associations={PersonalInformation_Interest_association_1, Interest_Topic_association, PersonalInformation_Interest_association},
    generalizations={gen_Environment_Topic, gen_Recreation_Topic, gen_Sport_Topic, gen_VideoGames_Topic, gen_Music_Topic, gen_Hobby_Interest, gen_Film_Topic, gen_Other_Topic, gen_Science_Topic}
)
