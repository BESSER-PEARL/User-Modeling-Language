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
OutputEnum: Enumeration = Enumeration(
    name="OutputEnum",
    literals={
            EnumerationLiteral(name="video"),
			EnumerationLiteral(name="text"),
			EnumerationLiteral(name="image"),
			EnumerationLiteral(name="audio")
    }
)

StylesEnum: Enumeration = Enumeration(
    name="StylesEnum",
    literals={
            EnumerationLiteral(name="formal"),
			EnumerationLiteral(name="informal")
    }
)

InputEnum: Enumeration = Enumeration(
    name="InputEnum",
    literals={
            EnumerationLiteral(name="image"),
			EnumerationLiteral(name="voice"),
			EnumerationLiteral(name="video"),
			EnumerationLiteral(name="click"),
			EnumerationLiteral(name="text")
    }
)

# Classes
Preference = Class(name="Preference")
PreferredLanguage = Class(name="PreferredLanguage")
Output_Modality = Class(name="Output_Modality")
Input_Modality = Class(name="Input_Modality")
Content = Class(name="Content")
Design = Class(name="Design")
Interaction_Modality = Class(name="Interaction_Modality")
Item = Class(name="Item")

# Preference class attributes and methods

# PreferredLanguage class attributes and methods
PreferredLanguage_style: Property = Property(name="style", type=StylesEnum)
PreferredLanguage_iso639_1: Property = Property(name="iso639_1", type=StringType)
PreferredLanguage.attributes={PreferredLanguage_style, PreferredLanguage_iso639_1}

# Output_Modality class attributes and methods
Output_Modality_value: Property = Property(name="value", type=OutputEnum)
Output_Modality.attributes={Output_Modality_value}

# Input_Modality class attributes and methods
Input_Modality_value: Property = Property(name="value", type=InputEnum)
Input_Modality.attributes={Input_Modality_value}

# Content class attributes and methods

# Design class attributes and methods
Design_contentContrast: Property = Property(name="contentContrast", type=StringType)
Design_brightness: Property = Property(name="brightness", type=StringType)
Design_textSize: Property = Property(name="textSize", type=IntegerType)
Design_colorScheme: Property = Property(name="colorScheme", type=StringType)
Design_police: Property = Property(name="police", type=StringType)
Design.attributes={Design_contentContrast, Design_brightness, Design_textSize, Design_colorScheme, Design_police}

# Interaction_Modality class attributes and methods

# Item class attributes and methods
Item_preferenceScore: Property = Property(name="preferenceScore", type=StringType)
Item_name: Property = Property(name="name", type=StringType)
Item.attributes={Item_preferenceScore, Item_name}

# Relationships
Preference_Interaction_Modality_association: BinaryAssociation = BinaryAssociation(
    name="Preference_Interaction_Modality_association",
    ends={
        Property(name="Interaction_Modality_end", type=Interaction_Modality, multiplicity=Multiplicity(0, 9999)),
        Property(name="Preference_end", type=Preference, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Preference_Content_association_1: BinaryAssociation = BinaryAssociation(
    name="Preference_Content_association_1",
    ends={
        Property(name="Preference_end", type=Preference, multiplicity=Multiplicity(1, 1)),
        Property(name="Content_end", type=Content, multiplicity=Multiplicity(0, 1))
    }
)
Content_PreferredLanguage_association: BinaryAssociation = BinaryAssociation(
    name="Content_PreferredLanguage_association",
    ends={
        Property(name="Content_end", type=Content, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="PreferredLanguage_end", type=PreferredLanguage, multiplicity=Multiplicity(0, 1))
    }
)
Content_Item_association_1: BinaryAssociation = BinaryAssociation(
    name="Content_Item_association_1",
    ends={
        Property(name="Content_end", type=Content, multiplicity=Multiplicity(1, 1)),
        Property(name="*", type=Item, multiplicity=Multiplicity(1, 1))
    }
)
Preference_Design_association_1: BinaryAssociation = BinaryAssociation(
    name="Preference_Design_association_1",
    ends={
        Property(name="Preference_end", type=Preference, multiplicity=Multiplicity(1, 1)),
        Property(name="Design_end", type=Design, multiplicity=Multiplicity(0, 1))
    }
)
Content_Item_association: BinaryAssociation = BinaryAssociation(
    name="Content_Item_association",
    ends={
        Property(name="Content_end", type=Content, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="*", type=Item, multiplicity=Multiplicity(1, 1))
    }
)
Output_Modality_Interaction_Modality_non_navigable: BinaryAssociation = BinaryAssociation(
    name="Output_Modality_Interaction_Modality_non_navigable",
    ends={
        Property(name="Output_Modality_end", type=Output_Modality, multiplicity=Multiplicity(1, 1)),
        Property(name="Interaction_Modality_end", type=Interaction_Modality, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Input_Modality_Interaction_Modality_non_navigable: BinaryAssociation = BinaryAssociation(
    name="Input_Modality_Interaction_Modality_non_navigable",
    ends={
        Property(name="Input_Modality_end", type=Input_Modality, multiplicity=Multiplicity(1, 1)),
        Property(name="Interaction_Modality_end", type=Interaction_Modality, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Preference_Content_association: BinaryAssociation = BinaryAssociation(
    name="Preference_Content_association",
    ends={
        Property(name="Preference_end", type=Preference, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Content_end", type=Content, multiplicity=Multiplicity(0, 1))
    }
)
Content_PreferredLanguage_association_1: BinaryAssociation = BinaryAssociation(
    name="Content_PreferredLanguage_association_1",
    ends={
        Property(name="PreferredLanguage_end", type=PreferredLanguage, multiplicity=Multiplicity(0, 1)),
        Property(name="Content_end", type=Content, multiplicity=Multiplicity(1, 1))
    }
)
Preference_Design_association: BinaryAssociation = BinaryAssociation(
    name="Preference_Design_association",
    ends={
        Property(name="Preference_end", type=Preference, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Design_end", type=Design, multiplicity=Multiplicity(0, 1))
    }
)
Preference_Interaction_Modality_association_1: BinaryAssociation = BinaryAssociation(
    name="Preference_Interaction_Modality_association_1",
    ends={
        Property(name="Interaction_Modality_end", type=Interaction_Modality, multiplicity=Multiplicity(0, 9999)),
        Property(name="Preference_end", type=Preference, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Generated Model",
    types={Preference, PreferredLanguage, Output_Modality, Input_Modality, Content, Design, Interaction_Modality, Item, OutputEnum, StylesEnum, InputEnum},
    associations={Preference_Interaction_Modality_association, Preference_Content_association_1, Content_PreferredLanguage_association, Content_Item_association_1, Preference_Design_association_1, Content_Item_association, Output_Modality_Interaction_Modality_non_navigable, Input_Modality_Interaction_Modality_non_navigable, Preference_Content_association, Content_PreferredLanguage_association_1, Preference_Design_association, Preference_Interaction_Modality_association_1},
    generalizations={}
)
