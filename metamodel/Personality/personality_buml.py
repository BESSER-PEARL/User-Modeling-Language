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
CharacteristicsEnum: Enumeration = Enumeration(
    name="CharacteristicsEnum",
    literals={
            EnumerationLiteral(name="Unfriendly"),
			EnumerationLiteral(name="Tense"),
			EnumerationLiteral(name="Cold"),
			EnumerationLiteral(name="Disorderly"),
			EnumerationLiteral(name="Cooperative"),
			EnumerationLiteral(name="Retiring"),
			EnumerationLiteral(name="Assertive"),
			EnumerationLiteral(name="Helpful"),
			EnumerationLiteral(name="Shy"),
			EnumerationLiteral(name="Dominant"),
			EnumerationLiteral(name="Faultfinding"),
			EnumerationLiteral(name="Thorough"),
			EnumerationLiteral(name="Talkative"),
			EnumerationLiteral(name="Sympathetic"),
			EnumerationLiteral(name="Inventive"),
			EnumerationLiteral(name="Contended"),
			EnumerationLiteral(name="Quiet"),
			EnumerationLiteral(name="Efficient"),
			EnumerationLiteral(name="Stable"),
			EnumerationLiteral(name="Reserved"),
			EnumerationLiteral(name="Frivolous"),
			EnumerationLiteral(name="Reliable"),
			EnumerationLiteral(name="Careless"),
			EnumerationLiteral(name="Artistic"),
			EnumerationLiteral(name="Kind"),
			EnumerationLiteral(name="Warm"),
			EnumerationLiteral(name="Commonplace"),
			EnumerationLiteral(name="Anxious"),
			EnumerationLiteral(name="Imaginative"),
			EnumerationLiteral(name="Loyal"),
			EnumerationLiteral(name="Worrying"),
			EnumerationLiteral(name="Organised"),
			EnumerationLiteral(name="Moody"),
			EnumerationLiteral(name="Calm")
    }
)

TraitsEnum: Enumeration = Enumeration(
    name="TraitsEnum",
    literals={
            EnumerationLiteral(name="Introvert"),
			EnumerationLiteral(name="Closeminded"),
			EnumerationLiteral(name="Thinking"),
			EnumerationLiteral(name="Openminded"),
			EnumerationLiteral(name="Agreeable"),
			EnumerationLiteral(name="Controlled"),
			EnumerationLiteral(name="Excessive"),
			EnumerationLiteral(name="Feeling"),
			EnumerationLiteral(name="Disagreeable"),
			EnumerationLiteral(name="Intelligent"),
			EnumerationLiteral(name="Pessimistic"),
			EnumerationLiteral(name="Extravert"),
			EnumerationLiteral(name="Neurotic"),
			EnumerationLiteral(name="Optimistic"),
			EnumerationLiteral(name="Resilient"),
			EnumerationLiteral(name="Indulgent"),
			EnumerationLiteral(name="Tempered"),
			EnumerationLiteral(name="Sensing"),
			EnumerationLiteral(name="Perceiving"),
			EnumerationLiteral(name="Judging")
    }
)

# Classes
Interpersonal = Class(name="Interpersonal_Social_World")
Instrumental = Class(name="Instrumental_Material_World")
Bias = Class(name="Bias")
MotivationProfile = Class(name="MotivationProfile")
Trait = Class(name="Trait")
Characteristic = Class(name="Characteristic")
ThinkingToFeeling = Class(name="ThinkingToFeeling")
SensingToIntuition = Class(name="SensingToIntuition")
Personality = Class(name="Personality")
Attitude = Class(name="Attitude")
Neuroticism = Class(name="Neuroticism")
ExtraversionToIntroversion = Class(name="ExtraversionToIntroversion")
Big_Five_Traits = Class(name="Big_Five_Traits")
MyersBriggsTypeInventory = Class(name="MyersBriggsTypeInventory")
JudgingToPerceiving = Class(name="JudgingToPerceiving")
Other = Class(name="Other")
Extraversion = Class(name="Extraversion")
Openness = Class(name="Openness")
Topic = Class(name="Topic")
Conscientiousness = Class(name="Conscientiousness")
Agreeableness = Class(name="Agreeableness")
Intraphysic = Class(name="Intraphysic_Self")

# Interpersonal class attributes and methods
Interpersonal_belongingImportance: Property = Property(name="belongingImportance", type=StringType)
Interpersonal_nurturanceImportance: Property = Property(name="nurturanceImportance", type=StringType)
Interpersonal_esteemImportance: Property = Property(name="esteemImportance", type=StringType)
Interpersonal.attributes={Interpersonal_belongingImportance, Interpersonal_nurturanceImportance, Interpersonal_esteemImportance}

# Instrumental class attributes and methods
Instrumental_engagementImportance: Property = Property(name="engagementImportance", type=StringType)
Instrumental_achievementImportance: Property = Property(name="achievementImportance", type=StringType)
Instrumental_empowerementImportance: Property = Property(name="empowerementImportance", type=StringType)
Instrumental.attributes={Instrumental_engagementImportance, Instrumental_achievementImportance, Instrumental_empowerementImportance}

# Bias class attributes and methods

# MotivationProfile class attributes and methods

# Trait class attributes and methods
Trait_score: Property = Property(name="score", type=StringType)
Trait.attributes={Trait_score}

# Characteristic class attributes and methods
Characteristic_score: Property = Property(name="score", type=StringType)
Characteristic_name: Property = Property(name="name", type=CharacteristicsEnum)
Characteristic.attributes={Characteristic_score, Characteristic_name}

# ThinkingToFeeling class attributes and methods

# SensingToIntuition class attributes and methods

# Personality class attributes and methods

# Attitude class attributes and methods
Attitude_description: Property = Property(name="description", type=StringType)
Attitude_negative_to_positive: Property = Property(name="negative_to_positive", type=StringType)
Attitude.attributes={Attitude_description, Attitude_negative_to_positive}

# Neuroticism class attributes and methods

# ExtraversionToIntroversion class attributes and methods

# Big_Five_Traits class attributes and methods

# MyersBriggsTypeInventory class attributes and methods

# JudgingToPerceiving class attributes and methods

# Other class attributes and methods
Other_name: Property = Property(name="name", type=TraitsEnum)
Other.attributes={Other_name}

# Extraversion class attributes and methods

# Openness class attributes and methods

# Topic class attributes and methods

# Conscientiousness class attributes and methods

# Agreeableness class attributes and methods

# Intraphysic class attributes and methods
Intraphysic_securityImportance: Property = Property(name="securityImportance", type=StringType)
Intraphysic_masteryImportance: Property = Property(name="masteryImportance", type=StringType)
Intraphysic_identityImportance: Property = Property(name="identityImportance", type=StringType)
Intraphysic.attributes={Intraphysic_securityImportance, Intraphysic_masteryImportance, Intraphysic_identityImportance}

# Relationships
Personality_MotivationProfile_association: BinaryAssociation = BinaryAssociation(
    name="Personality_MotivationProfile_association",
    ends={
        Property(name="MotivationProfile_end", type=MotivationProfile, multiplicity=Multiplicity(0, 1)),
        Property(name="Personality_end", type=Personality, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Instrumental_MotivationProfile_non_navigable: BinaryAssociation = BinaryAssociation(
    name="Instrumental_MotivationProfile_non_navigable",
    ends={
        Property(name="Instrumental_end", type=Instrumental, multiplicity=Multiplicity(1, 1)),
        Property(name="MotivationProfile_end", type=MotivationProfile, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Personality_Attitude_association_1: BinaryAssociation = BinaryAssociation(
    name="Personality_Attitude_association_1",
    ends={
        Property(name="Attitude_end", type=Attitude, multiplicity=Multiplicity(0, 9999)),
        Property(name="Personality_end", type=Personality, multiplicity=Multiplicity(1, 1))
    }
)
Interpersonal_MotivationProfile_non_navigable: BinaryAssociation = BinaryAssociation(
    name="Interpersonal_MotivationProfile_non_navigable",
    ends={
        Property(name="Interpersonal_end", type=Interpersonal, multiplicity=Multiplicity(1, 1)),
        Property(name="MotivationProfile_end", type=MotivationProfile, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Attitude_Topic_association: BinaryAssociation = BinaryAssociation(
    name="Attitude_Topic_association",
    ends={
        Property(name="Attitude_end", type=Attitude, multiplicity=Multiplicity(0, 9999)),
        Property(name="Topic_end", type=Topic, multiplicity=Multiplicity(1, 1))
    }
)
Personality_Trait_association: BinaryAssociation = BinaryAssociation(
    name="Personality_Trait_association",
    ends={
        Property(name="Trait_end", type=Trait, multiplicity=Multiplicity(0, 9999)),
        Property(name="Personality_end", type=Personality, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Personality_MotivationProfile_association_1: BinaryAssociation = BinaryAssociation(
    name="Personality_MotivationProfile_association_1",
    ends={
        Property(name="Personality_end", type=Personality, multiplicity=Multiplicity(1, 1)),
        Property(name="MotivationProfile_end", type=MotivationProfile, multiplicity=Multiplicity(0, 1))
    }
)
Personality_Trait_association_1: BinaryAssociation = BinaryAssociation(
    name="Personality_Trait_association_1",
    ends={
        Property(name="Personality_end", type=Personality, multiplicity=Multiplicity(1, 1)),
        Property(name="Trait_end", type=Trait, multiplicity=Multiplicity(0, 9999))
    }
)
Intraphysic_MotivationProfile_non_navigable: BinaryAssociation = BinaryAssociation(
    name="Intraphysic_MotivationProfile_non_navigable",
    ends={
        Property(name="Intraphysic_end", type=Intraphysic, multiplicity=Multiplicity(1, 1)),
        Property(name="MotivationProfile_end", type=MotivationProfile, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Trait_Characteristic_association: BinaryAssociation = BinaryAssociation(
    name="Trait_Characteristic_association",
    ends={
        Property(name="Trait_end", type=Trait, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Characteristic_end", type=Characteristic, multiplicity=Multiplicity(0, 9999))
    }
)
Personality_Attitude_association: BinaryAssociation = BinaryAssociation(
    name="Personality_Attitude_association",
    ends={
        Property(name="Personality_end", type=Personality, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Attitude_end", type=Attitude, multiplicity=Multiplicity(0, 9999))
    }
)
Trait_Characteristic_association_1: BinaryAssociation = BinaryAssociation(
    name="Trait_Characteristic_association_1",
    ends={
        Property(name="Trait_end", type=Trait, multiplicity=Multiplicity(1, 1)),
        Property(name="Characteristic_end", type=Characteristic, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_Big_Five_Traits_Trait = Generalization(general=Trait, specific=Big_Five_Traits)
gen_Neuroticism_Big_Five_Traits = Generalization(general=Big_Five_Traits, specific=Neuroticism)
gen_Bias_Attitude = Generalization(general=Attitude, specific=Bias)
gen_Agreeableness_Big_Five_Traits = Generalization(general=Big_Five_Traits, specific=Agreeableness)
gen_Extraversion_Big_Five_Traits = Generalization(general=Big_Five_Traits, specific=Extraversion)
gen_Conscientiousness_Big_Five_Traits = Generalization(general=Big_Five_Traits, specific=Conscientiousness)
gen_JudgingToPerceiving_MyersBriggsTypeInventory = Generalization(general=MyersBriggsTypeInventory, specific=JudgingToPerceiving)
gen_ThinkingToFeeling_MyersBriggsTypeInventory = Generalization(general=MyersBriggsTypeInventory, specific=ThinkingToFeeling)
gen_Openness_Big_Five_Traits = Generalization(general=Big_Five_Traits, specific=Openness)
gen_Other_Trait = Generalization(general=Trait, specific=Other)
gen_SensingToIntuition_MyersBriggsTypeInventory = Generalization(general=MyersBriggsTypeInventory, specific=SensingToIntuition)
gen_MyersBriggsTypeInventory_Trait = Generalization(general=Trait, specific=MyersBriggsTypeInventory)
gen_ExtraversionToIntroversion_MyersBriggsTypeInventory = Generalization(general=MyersBriggsTypeInventory, specific=ExtraversionToIntroversion)

# Domain Model
domain_model = DomainModel(
    name="Generated Model",
    types={Interpersonal, Instrumental, Bias, MotivationProfile, Trait, Characteristic, ThinkingToFeeling, SensingToIntuition, Personality, Attitude, Neuroticism, ExtraversionToIntroversion, Big_Five_Traits, MyersBriggsTypeInventory, JudgingToPerceiving, Other, Extraversion, Openness, Topic, Conscientiousness, Agreeableness, Intraphysic, CharacteristicsEnum, TraitsEnum},
    associations={Personality_MotivationProfile_association, Instrumental_MotivationProfile_non_navigable, Personality_Attitude_association_1, Interpersonal_MotivationProfile_non_navigable, Attitude_Topic_association, Personality_Trait_association, Personality_MotivationProfile_association_1, Personality_Trait_association_1, Intraphysic_MotivationProfile_non_navigable, Trait_Characteristic_association, Personality_Attitude_association, Trait_Characteristic_association_1},
    generalizations={gen_Big_Five_Traits_Trait, gen_Neuroticism_Big_Five_Traits, gen_Bias_Attitude, gen_Agreeableness_Big_Five_Traits, gen_Extraversion_Big_Five_Traits, gen_Conscientiousness_Big_Five_Traits, gen_JudgingToPerceiving_MyersBriggsTypeInventory, gen_ThinkingToFeeling_MyersBriggsTypeInventory, gen_Openness_Big_Five_Traits, gen_Other_Trait, gen_SensingToIntuition_MyersBriggsTypeInventory, gen_MyersBriggsTypeInventory_Trait, gen_ExtraversionToIntroversion_MyersBriggsTypeInventory}
)
