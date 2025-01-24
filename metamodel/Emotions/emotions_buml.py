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
EmotionStatus = Class(name="EmotionStatus")

# EmotionStatus class attributes and methods
EmotionStatus_anxiety: Property = Property(name="anxiety", type=IntegerType)
EmotionStatus_dread: Property = Property(name="dread", type=IntegerType)
EmotionStatus_worry: Property = Property(name="worry", type=IntegerType)
EmotionStatus_boredom: Property = Property(name="boredom", type=IntegerType)
EmotionStatus_fear: Property = Property(name="fear", type=IntegerType)
EmotionStatus_hate: Property = Property(name="hate", type=IntegerType)
EmotionStatus_joy: Property = Property(name="joy", type=IntegerType)
EmotionStatus_satisfaction: Property = Property(name="satisfaction", type=IntegerType)
EmotionStatus_happiness: Property = Property(name="happiness", type=IntegerType)
EmotionStatus_love: Property = Property(name="love", type=IntegerType)
EmotionStatus_relief: Property = Property(name="relief", type=IntegerType)
EmotionStatus_hope: Property = Property(name="hope", type=IntegerType)
EmotionStatus_confusion: Property = Property(name="confusion", type=IntegerType)
EmotionStatus_pride: Property = Property(name="pride", type=IntegerType)
EmotionStatus_sadness: Property = Property(name="sadness", type=IntegerType)
EmotionStatus_disgust: Property = Property(name="disgust", type=IntegerType)
EmotionStatus_anger: Property = Property(name="anger", type=IntegerType)
EmotionStatus_shame: Property = Property(name="shame", type=IntegerType)
EmotionStatus_excitement: Property = Property(name="excitement", type=IntegerType)
EmotionStatus.attributes={EmotionStatus_anxiety, EmotionStatus_dread, EmotionStatus_worry, EmotionStatus_boredom, EmotionStatus_fear, EmotionStatus_hate, EmotionStatus_joy, EmotionStatus_satisfaction, EmotionStatus_happiness, EmotionStatus_love, EmotionStatus_relief, EmotionStatus_hope, EmotionStatus_confusion, EmotionStatus_pride, EmotionStatus_sadness, EmotionStatus_disgust, EmotionStatus_anger, EmotionStatus_shame, EmotionStatus_excitement}

# Domain Model
domain_model = DomainModel(
    name="Generated Model",
    types={EmotionStatus},
    associations={},
    generalizations={}
)
