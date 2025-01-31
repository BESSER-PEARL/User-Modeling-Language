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
CEFR: Enumeration = Enumeration(
    name="CEFR",
    literals={
            EnumerationLiteral(name="C1"),
			EnumerationLiteral(name="A2"),
			EnumerationLiteral(name="C2"),
			EnumerationLiteral(name="B2"),
			EnumerationLiteral(name="A1"),
			EnumerationLiteral(name="B1")
    }
)

DegreeEnum: Enumeration = Enumeration(
    name="DegreeEnum",
    literals={
            EnumerationLiteral(name="Bachelor's degree"),
			EnumerationLiteral(name="Certificate"),
			EnumerationLiteral(name="Master's degree"),
			EnumerationLiteral(name="High-school diploma"),
			EnumerationLiteral(name="Doctorate's degree")
    }
)

# Classes
Knowledge = Class(name="Knowledge")
Education = Class(name="Education")
Topic = Class(name="Topic")
Skill = Class(name="Skill")
Competence = Class(name="Competence")
Language = Class(name="Language")
Experience = Class(name="Experience")

# Knowledge class attributes and methods
Knowledge_score: Property = Property(name="score", type=StringType)
Knowledge.attributes={Knowledge_score}

# Education class attributes and methods
Education_fieldOfDegree: Property = Property(name="fieldOfDegree", type=StringType)
Education_degreeName: Property = Property(name="degreeName", type=StringType)
Education_degreeType: Property = Property(name="degreeType", type=DegreeEnum)
Education_providedBy: Property = Property(name="providedBy", type=StringType)
Education.attributes={Education_fieldOfDegree, Education_degreeName, Education_degreeType, Education_providedBy}

# Topic class attributes and methods

# Skill class attributes and methods
Skill_score: Property = Property(name="score", type=StringType)
Skill_name: Property = Property(name="name", type=StringType)
Skill.attributes={Skill_score, Skill_name}

# Competence class attributes and methods

# Language class attributes and methods
Language_level: Property = Property(name="level", type=CEFR)
Language_iso693_3: Property = Property(name="iso693_3", type=StringType)
Language.attributes={Language_level, Language_iso693_3}

# Experience class attributes and methods
Experience_endDate: Property = Property(name="endDate", type=DateTimeType)
Experience_roleName: Property = Property(name="roleName", type=StringType)
Experience_startDate: Property = Property(name="startDate", type=DateTimeType)
Experience_companyName: Property = Property(name="companyName", type=StringType)
Experience.attributes={Experience_endDate, Experience_roleName, Experience_startDate, Experience_companyName}

# Relationships
Competence_Skill_association_1: BinaryAssociation = BinaryAssociation(
    name="Competence_Skill_association_1",
    ends={
        Property(name="Skill_end", type=Skill, multiplicity=Multiplicity(0, 9999)),
        Property(name="Competence_end", type=Competence, multiplicity=Multiplicity(1, 1))
    }
)
Competence_Experience_association: BinaryAssociation = BinaryAssociation(
    name="Competence_Experience_association",
    ends={
        Property(name="Experience_end", type=Experience, multiplicity=Multiplicity(0, 9999)),
        Property(name="Competence_end", type=Competence, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Competence_Language_association: BinaryAssociation = BinaryAssociation(
    name="Competence_Language_association",
    ends={
        Property(name="Competence_end", type=Competence, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Language_end", type=Language, multiplicity=Multiplicity(0, 9999))
    }
)
Competence_Language_association_1: BinaryAssociation = BinaryAssociation(
    name="Competence_Language_association_1",
    ends={
        Property(name="Competence_end", type=Competence, multiplicity=Multiplicity(1, 1)),
        Property(name="Language_end", type=Language, multiplicity=Multiplicity(0, 9999))
    }
)
Competence_Knowledge_association: BinaryAssociation = BinaryAssociation(
    name="Competence_Knowledge_association",
    ends={
        Property(name="Competence_end", type=Competence, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Knowledge_end", type=Knowledge, multiplicity=Multiplicity(0, 9999))
    }
)
Competence_Education_association: BinaryAssociation = BinaryAssociation(
    name="Competence_Education_association",
    ends={
        Property(name="Competence_end", type=Competence, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Education_end", type=Education, multiplicity=Multiplicity(0, 9999))
    }
)
Competence_Experience_association_1: BinaryAssociation = BinaryAssociation(
    name="Competence_Experience_association_1",
    ends={
        Property(name="Experience_end", type=Experience, multiplicity=Multiplicity(0, 9999)),
        Property(name="Competence_end", type=Competence, multiplicity=Multiplicity(1, 1))
    }
)
Competence_Knowledge_association_1: BinaryAssociation = BinaryAssociation(
    name="Competence_Knowledge_association_1",
    ends={
        Property(name="Knowledge_end", type=Knowledge, multiplicity=Multiplicity(0, 9999)),
        Property(name="Competence_end", type=Competence, multiplicity=Multiplicity(1, 1))
    }
)
Competence_Education_association_1: BinaryAssociation = BinaryAssociation(
    name="Competence_Education_association_1",
    ends={
        Property(name="Education_end", type=Education, multiplicity=Multiplicity(0, 9999)),
        Property(name="Competence_end", type=Competence, multiplicity=Multiplicity(1, 1))
    }
)
Competence_Skill_association: BinaryAssociation = BinaryAssociation(
    name="Competence_Skill_association",
    ends={
        Property(name="Skill_end", type=Skill, multiplicity=Multiplicity(0, 9999)),
        Property(name="Competence_end", type=Competence, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Knowledge_Topic_association: BinaryAssociation = BinaryAssociation(
    name="Knowledge_Topic_association",
    ends={
        Property(name="Knowledge_end", type=Knowledge, multiplicity=Multiplicity(1, 1)),
        Property(name="knowledgeOn", type=Topic, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Generated Model",
    types={Knowledge, Education, Topic, Skill, Competence, Language, Experience, CEFR, DegreeEnum},
    associations={Competence_Skill_association_1, Competence_Experience_association, Competence_Language_association, Competence_Language_association_1, Competence_Knowledge_association, Competence_Education_association, Competence_Experience_association_1, Competence_Knowledge_association_1, Competence_Education_association_1, Competence_Skill_association, Knowledge_Topic_association},
    generalizations={}
)
