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
ReligionEnum: Enumeration = Enumeration(
    name="ReligionEnum",
    literals={
            EnumerationLiteral(name="Other"),
			EnumerationLiteral(name="Buddhism"),
			EnumerationLiteral(name="Christianity"),
			EnumerationLiteral(name="Islam"),
			EnumerationLiteral(name="Folk Religion"),
			EnumerationLiteral(name="Hinduism"),
			EnumerationLiteral(name="Irreligion")
    }
)

# Classes
Culture = Class(name="Culture")

# Culture class attributes and methods
Culture_powerDistance: Property = Property(name="powerDistance", type=StringType)
Culture_temporalOrientation: Property = Property(name="temporalOrientation", type=StringType)
Culture_restrain_to_indulgence: Property = Property(name="restrain_to_indulgence", type=StringType)
Culture_feminity_to_masculinity: Property = Property(name="feminity_to_masculinity", type=StringType)
Culture_religion: Property = Property(name="religion", type=ReligionEnum)
Culture_collectivism_to_individualism: Property = Property(name="collectivism_to_individualism", type=StringType)
Culture_uncertaintyAvoidance: Property = Property(name="uncertaintyAvoidance", type=StringType)
Culture.attributes={Culture_powerDistance, Culture_temporalOrientation, Culture_restrain_to_indulgence, Culture_feminity_to_masculinity, Culture_religion, Culture_collectivism_to_individualism, Culture_uncertaintyAvoidance}

# Domain Model
domain_model = DomainModel(
    name="Generated Model",
    types={Culture, ReligionEnum},
    associations={},
    generalizations={}
)
