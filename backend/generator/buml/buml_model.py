from besser.BUML.metamodel.structural import *  

# Primitive Data Types
int_type = PrimitiveDataType("int")
str_type = PrimitiveDataType("str")

# Enumerations
CEFR = Enumeration(name="CEFR", literals = {
			EnumerationLiteral(name="A1"),
			EnumerationLiteral(name="A2"),
			EnumerationLiteral(name="B1"),
			EnumerationLiteral(name="B2"),
			EnumerationLiteral(name="C1"),
			EnumerationLiteral(name="C2")})

# Classes
User: Class = Class(name="User")
StaticProperty: Class = Class(name="StaticProperty", is_abstract=True)
PersonalInformation: Class = Class(name="PersonalInformation")
Age: Class = Class(name="Age")
KnownLanguage: Class = Class(name="KnownLanguage")
Nationality: Class = Class(name="Nationality")
Hobby: Class = Class(name="Hobby")
Interest: Class = Class(name="Interest")

# User class attributes and methods
User_name: Property = Property(name="name", type=str_type)
User.attributes={User_name}

# StaticProperty class attributes and methods

# PersonalInformation class attributes and methods
PersonalInformation_name: Property = Property(name="name", type=str_type)
PersonalInformation_address: Property = Property(name="address", type=str_type)
PersonalInformation_gender: Property = Property(name="gender", type=str_type)
PersonalInformation.attributes={PersonalInformation_name, PersonalInformation_address, PersonalInformation_gender}

# Age class attributes and methods
Age_value: Property = Property(name="value", type=int_type)
Age.attributes={Age_value}

# KnownLanguage class attributes and methods
KnownLanguage_name: Property = Property(name="name", type=str_type)
KnownLanguage_level: Property = Property(name="level", type=CEFR)
KnownLanguage.attributes={KnownLanguage_name, KnownLanguage_level}

# Nationality class attributes and methods
Nationality_name: Property = Property(name="name", type=str_type)
Nationality.attributes={Nationality_name}

# Hobby class attributes and methods
Hobby_name: Property = Property(name="name", type=str_type)
Hobby.attributes={Hobby_name}

# Interest class attributes and methods
Interest_name: Property = Property(name="name", type=str_type)
Interest.attributes={Interest_name}

# Relationships
personalInformation: BinaryAssociation = BinaryAssociation(name="personalInformation", ends={
        Property(name="personalInformation", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False, is_composite=True),
        Property(name="personalInformation", type=PersonalInformation, multiplicity=Multiplicity(0, "*"))})
age: BinaryAssociation = BinaryAssociation(name="age", ends={
        Property(name="age", type=PersonalInformation, multiplicity=Multiplicity(1, 1), is_navigable=False, is_composite=True),
        Property(name="age", type=Age, multiplicity=Multiplicity(0, "*"))})
hobby: BinaryAssociation = BinaryAssociation(name="hobby", ends={
        Property(name="hobby", type=PersonalInformation, multiplicity=Multiplicity(1, 1), is_navigable=False, is_composite=True),
        Property(name="hobby", type=Hobby, multiplicity=Multiplicity(0, "*"))})
knownLanguage: BinaryAssociation = BinaryAssociation(name="knownLanguage", ends={
        Property(name="knownLanguage", type=PersonalInformation, multiplicity=Multiplicity(1, 1), is_navigable=False, is_composite=True),
        Property(name="knownLanguage", type=KnownLanguage, multiplicity=Multiplicity(0, "*"))})
nationality: BinaryAssociation = BinaryAssociation(name="nationality", ends={
        Property(name="nationality", type=PersonalInformation, multiplicity=Multiplicity(1, 1), is_navigable=False, is_composite=True),
        Property(name="nationality", type=Nationality, multiplicity=Multiplicity(0, "*"))})
interest: BinaryAssociation = BinaryAssociation(name="interest", ends={
        Property(name="interest", type=PersonalInformation, multiplicity=Multiplicity(1, 1), is_navigable=False, is_composite=True),
        Property(name="interest", type=Interest, multiplicity=Multiplicity(0, "*"))})

# Generalizations
gen_StaticProperty_PersonalInformation: Generalization = Generalization(general=StaticProperty, specific=PersonalInformation)


# Domain Model
domain: DomainModel = DomainModel(
				name="Domain Model",
				types={User, StaticProperty, PersonalInformation, Age, KnownLanguage, Nationality, Hobby, Interest},
				associations={personalInformation, age, hobby, knownLanguage, nationality, interest},
				generalizations={gen_StaticProperty_PersonalInformation},
				enumerations={CEFR}
				)
