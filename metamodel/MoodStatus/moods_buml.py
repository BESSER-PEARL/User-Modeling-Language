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
# Classes
MoodStatus = Class(name="MoodStatus")

# MoodStatus class attributes and methods
MoodStatus_tense_to_relaxed: Property = Property(name="tense_to_relaxed", type=IntegerType)
MoodStatus_bad_to_good: Property = Property(name="bad_to_good", type=IntegerType)
MoodStatus_tired_to_energetic: Property = Property(name="tired_to_energetic", type=IntegerType)
MoodStatus.attributes={MoodStatus_tense_to_relaxed, MoodStatus_bad_to_good, MoodStatus_tired_to_energetic}

# Domain Model
domain_model = DomainModel(
    name="Generated Model",
    types={MoodStatus},
    associations={},
    generalizations={}
)
