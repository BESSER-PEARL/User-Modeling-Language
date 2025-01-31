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
Goal = Class(name="Goal")

# Goal class attributes and methods
Goal_name: Property = Property(name="name", type=StringType)
Goal_deadline: Property = Property(name="deadline", type=DateTimeType)
Goal_description: Property = Property(name="description", type=StringType)
Goal.attributes={Goal_name, Goal_deadline, Goal_description}

# Domain Model
domain_model = DomainModel(
    name="Generated Model",
    types={Goal},
    associations={},
    generalizations={}
)
