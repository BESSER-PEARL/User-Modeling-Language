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
RelationshipTypeEnum: Enumeration = Enumeration(
    name="RelationshipTypeEnum",
    literals={
            EnumerationLiteral(name="relative"),
			EnumerationLiteral(name="friend"),
			EnumerationLiteral(name="partner"),
			EnumerationLiteral(name="other"),
			EnumerationLiteral(name="colleague")
    }
)

RelationshipQualityEnum: Enumeration = Enumeration(
    name="RelationshipQualityEnum",
    literals={
            EnumerationLiteral(name="slightly negative"),
			EnumerationLiteral(name="positive"),
			EnumerationLiteral(name="negative"),
			EnumerationLiteral(name="strongly negative"),
			EnumerationLiteral(name="slightly positive"),
			EnumerationLiteral(name="strongly positive")
    }
)

# Classes
Competence = Class(name="Competence")
Accessibility = Class(name="Accessibility")
PersonalInformation = Class(name="Personal Information")
User = Class(name="User")
Personality = Class(name="Personality")
Goal = Class(name="Goal")
Preference = Class(name="Preference")
EmotionStatus = Class(name="EmotionStatus")
Culture = Class(name="Culture")
Relationship = Class(name="Relationship")
MoodStatus = Class(name="MoodStatus")
Topic = Class(name="Topic")
# Competence class attributes and methods

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
Skill = Class(name="Skill")
Language = Class(name="Language")
Experience = Class(name="Experience")

# Knowledge class attributes and methods
Knowledge_score: Property = Property(name="score", type=StringType)
Knowledge.attributes={Knowledge_score}

# Education class attributes and methods
Education_fieldOfDegree: Property = Property(name="fieldOfDegree", type=StringType)
Education_degreeName: Property = Property(name="degreeName", type=StringType, multiplicity=Multiplicity(0, 1))
Education_degreeType: Property = Property(name="degreeType", type=DegreeEnum)
Education_providedBy: Property = Property(name="providedBy", type=StringType, multiplicity=Multiplicity(0, 1))
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
Experience_endDate: Property = Property(name="endDate", type=DateTimeType, multiplicity=Multiplicity(0, 1))
Experience_roleName: Property = Property(name="roleName", type=StringType)
Experience_startDate: Property = Property(name="startDate", type=DateTimeType, multiplicity=Multiplicity(0, 1))
Experience_companyName: Property = Property(name="companyName", type=StringType, multiplicity=Multiplicity(0, 1))
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




# Accessibility class attributes and methods and relationships

# Enumerations
ColorBlindnessEnum: Enumeration = Enumeration(
    name="ColorBlindnessEnum",
    literals={
            EnumerationLiteral(name="Tritanopia"),
			EnumerationLiteral(name="Protanomaly"),
			EnumerationLiteral(name="Deuteranopia"),
			EnumerationLiteral(name="Deuteranomaly"),
			EnumerationLiteral(name="Achromatopsia"),
			EnumerationLiteral(name="Protanopia"),
			EnumerationLiteral(name="Tritanomaly"),
			EnumerationLiteral(name="Rod Monochromacy")
    }
)

AspectsEnum: Enumeration = Enumeration(
    name="AspectsEnum",
    literals={
            EnumerationLiteral(name="Mobility"),
			EnumerationLiteral(name="Learning"),
			EnumerationLiteral(name="Cognitive"),
			EnumerationLiteral(name="Hearing"),
			EnumerationLiteral(name="Sight"),
			EnumerationLiteral(name="Speech"),
			EnumerationLiteral(name="Memory"),
			EnumerationLiteral(name="Social Relationships"),
			EnumerationLiteral(name="Mental Health")
    }
)

# Classes
Memory = Class(name="Memory")
spinalColumn = Class(name="spinalColumn")
Neck = Class(name="Neck")
Speech = Class(name="Speech")
Prosody = Class(name="Prosody")
Motoric = Class(name="Motoric")
lowerLimbAnthropometric = Class(name="lowerLimbAnthropometric")
PhysiologicalState = Class(name="Physiological State")
Attention = Class(name="Attention")
EmotionalIntelligence = Class(name="EmotionalIntelligence")
Anthropometric = Class(name="Anthropometric")
hyperExtension = Class(name="hyperExtension")
shoulder = Class(name="shoulder")
finger = Class(name="finger")
thigh = Class(name="thigh")
wrist = Class(name="wrist")
extension = Class(name="extension")
flexion = Class(name="flexion")
Disability = Class(name="Disability")
toe = Class(name="toe")
Hearing = Class(name="Hearing")
upperLimbAnthropometric = Class(name="upperLimbAnthropometric")
knee = Class(name="knee")
Sight = Class(name="Sight")
elbow = Class(name="elbow")
hand = Class(name="hand")
forearm = Class(name="forearm")
Cognitive = Class(name="Cognitive")
lowerLimb = Class(name="lowerLimb")
hip = Class(name="hip")
Phonation = Class(name="Phonation")
Gait = Class(name="Gait")
UpperLimp = Class(name="UpperLimp")
Mobility = Class(name="Mobility")

# Memory class attributes and methods
Memory_workingMemory: Property = Property(name="workingMemory", type=IntegerType, multiplicity=Multiplicity(0, 1))
Memory_sensoryMemory: Property = Property(name="sensoryMemory", type=IntegerType, multiplicity=Multiplicity(0, 1))
Memory_longTermMemory: Property = Property(name="longTermMemory", type=IntegerType, multiplicity=Multiplicity(0, 1))
Memory.attributes={Memory_workingMemory, Memory_sensoryMemory, Memory_longTermMemory}

# spinalColumn class attributes and methods
spinalColumn_rightLateralFlexion: Property = Property(name="rightLateralFlexion", type=IntegerType, multiplicity=Multiplicity(0, 1))
spinalColumn_leftLateralFlexion: Property = Property(name="leftLateralFlexion", type=IntegerType, multiplicity=Multiplicity(0, 1))
spinalColumn_leftLateralRotation: Property = Property(name="leftLateralRotation", type=IntegerType, multiplicity=Multiplicity(0, 1))
spinalColumn_rightLateralRotation: Property = Property(name="rightLateralRotation", type=IntegerType, multiplicity=Multiplicity(0, 1))
spinalColumn.attributes={spinalColumn_rightLateralFlexion, spinalColumn_leftLateralFlexion, spinalColumn_leftLateralRotation, spinalColumn_rightLateralRotation}

# Neck class attributes and methods
Neck_leftLateralFlexion: Property = Property(name="leftLateralFlexion", type=IntegerType, multiplicity=Multiplicity(0, 1))
Neck_rightLateralRotation: Property = Property(name="rightLateralRotation", type=IntegerType, multiplicity=Multiplicity(0, 1))
Neck_rightLateralFlexion: Property = Property(name="rightLateralFlexion", type=IntegerType, multiplicity=Multiplicity(0, 1))
Neck_leftLateralRotation: Property = Property(name="leftLateralRotation", type=IntegerType, multiplicity=Multiplicity(0, 1))
Neck.attributes={Neck_leftLateralFlexion, Neck_rightLateralRotation, Neck_rightLateralFlexion, Neck_leftLateralRotation}

# Speech class attributes and methods

# Prosody class attributes and methods
Prosody_lipMovementCoordination: Property = Property(name="lipMovementCoordination", type=IntegerType, multiplicity=Multiplicity(0, 1))
Prosody_jawMovement: Property = Property(name="jawMovement", type=FloatType, multiplicity=Multiplicity(0, 1))
Prosody_vocalStress: Property = Property(name="vocalStress", type=FloatType, multiplicity=Multiplicity(0, 1))
Prosody.attributes={Prosody_lipMovementCoordination, Prosody_jawMovement, Prosody_vocalStress}

# Motoric class attributes and methods
Motoric_handPrecision: Property = Property(name="handPrecision", type=IntegerType, multiplicity=Multiplicity(0, 1))
Motoric_handEyeCoordination: Property = Property(name="handEyeCoordination", type=IntegerType, multiplicity=Multiplicity(0, 1))
Motoric_fingerPrecision: Property = Property(name="fingerPrecision", type=IntegerType, multiplicity=Multiplicity(0, 1))
Motoric_clenchGrip: Property = Property(name="clenchGrip", type=FloatType, multiplicity=Multiplicity(0, 1))
Motoric_contactGrip: Property = Property(name="contactGrip", type=FloatType, multiplicity=Multiplicity(0, 1))
Motoric_pinchGrip: Property = Property(name="pinchGrip", type=FloatType, multiplicity=Multiplicity(0, 1))
Motoric_armPrecision: Property = Property(name="armPrecision", type=IntegerType, multiplicity=Multiplicity(0, 1))
Motoric.attributes={Motoric_handPrecision, Motoric_handEyeCoordination, Motoric_fingerPrecision, Motoric_clenchGrip, Motoric_contactGrip, Motoric_pinchGrip, Motoric_armPrecision}

# lowerLimbAnthropometric class attributes and methods
lowerLimbAnthropometric_tighCircumferenceInMeters: Property = Property(name="tighCircumferenceInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
lowerLimbAnthropometric_kneeHeightInMeters: Property = Property(name="kneeHeightInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
lowerLimbAnthropometric_footLengthInMeters: Property = Property(name="footLengthInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
lowerLimbAnthropometric_footBreadthInMeters: Property = Property(name="footBreadthInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
lowerLimbAnthropometric_hipBreadthInMeters: Property = Property(name="hipBreadthInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
lowerLimbAnthropometric_calfCirumferenceInMeters: Property = Property(name="calfCirumferenceInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
lowerLimbAnthropometric_ankleHeightInMeters: Property = Property(name="ankleHeightInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
lowerLimbAnthropometric_buttockKneeInMeters: Property = Property(name="buttockKneeInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
lowerLimbAnthropometric.attributes={lowerLimbAnthropometric_tighCircumferenceInMeters, lowerLimbAnthropometric_kneeHeightInMeters, lowerLimbAnthropometric_footLengthInMeters, lowerLimbAnthropometric_footBreadthInMeters, lowerLimbAnthropometric_hipBreadthInMeters, lowerLimbAnthropometric_calfCirumferenceInMeters, lowerLimbAnthropometric_ankleHeightInMeters, lowerLimbAnthropometric_buttockKneeInMeters}

# Physiological State class attributes and methods
PhysiologicalState_fatigue: Property = Property(name="fatigue", type=IntegerType, multiplicity=Multiplicity(0, 1))
PhysiologicalState_injury: Property = Property(name="injury", type=BooleanType, multiplicity=Multiplicity(0, 1))
PhysiologicalState_temperature: Property = Property(name="temperature", type=FloatType, multiplicity=Multiplicity(0, 1))
PhysiologicalState_bloodPressure: Property = Property(name="bloodPressure", type=IntegerType, multiplicity=Multiplicity(0, 1))
PhysiologicalState_heartbeat: Property = Property(name="heartbeat", type=IntegerType, multiplicity=Multiplicity(0, 1))
PhysiologicalState_perspiration: Property = Property(name="perspiration", type=IntegerType, multiplicity=Multiplicity(0, 1))
PhysiologicalState_pupilsDilation: Property = Property(name="pupilsDilation", type=IntegerType, multiplicity=Multiplicity(0, 1))
PhysiologicalState_nourishment: Property = Property(name="nourishment", type=IntegerType, multiplicity=Multiplicity(0, 1))
PhysiologicalState_respiration: Property = Property(name="respiration", type=IntegerType, multiplicity=Multiplicity(0, 1))
PhysiologicalState_arousal: Property = Property(name="arousal", type=BooleanType, multiplicity=Multiplicity(0, 1))
PhysiologicalState.attributes={PhysiologicalState_fatigue, PhysiologicalState_injury, PhysiologicalState_temperature, PhysiologicalState_bloodPressure, PhysiologicalState_heartbeat, PhysiologicalState_perspiration, PhysiologicalState_pupilsDilation, PhysiologicalState_nourishment, PhysiologicalState_respiration, PhysiologicalState_arousal}

# Attention class attributes and methods
Attention_dividingAttention: Property = Property(name="dividingAttention", type=IntegerType, multiplicity=Multiplicity(0, 1))
Attention_shiftingAttention: Property = Property(name="shiftingAttention", type=IntegerType, multiplicity=Multiplicity(0, 1))
Attention_sharingAttention: Property = Property(name="sharingAttention", type=IntegerType, multiplicity=Multiplicity(0, 1))
Attention_sustainingAttention: Property = Property(name="sustainingAttention", type=IntegerType, multiplicity=Multiplicity(0, 1))
Attention.attributes={Attention_dividingAttention, Attention_shiftingAttention, Attention_sharingAttention, Attention_sustainingAttention}

# EmotionalIntelligence class attributes and methods
EmotionalIntelligence_socialAwareness: Property = Property(name="socialAwareness", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionalIntelligence_relationshipManagement: Property = Property(name="relationshipManagement", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionalIntelligence_selfManagement: Property = Property(name="selfManagement", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionalIntelligence_selfAwareness: Property = Property(name="selfAwareness", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionalIntelligence.attributes={EmotionalIntelligence_socialAwareness, EmotionalIntelligence_relationshipManagement, EmotionalIntelligence_selfManagement, EmotionalIntelligence_selfAwareness}

# Anthropometric class attributes and methods
Anthropometric_weightInKg: Property = Property(name="weightInKg", type=FloatType, multiplicity=Multiplicity(0, 1))
Anthropometric_headBreadthInMeters: Property = Property(name="headBreadthInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
Anthropometric_headLengthInMeters: Property = Property(name="headLengthInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
Anthropometric_bideltoidBreadthInMeters: Property = Property(name="bideltoidBreadthInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
Anthropometric_statureInMeters: Property = Property(name="statureInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
Anthropometric_sittingHeightInMeters: Property = Property(name="sittingHeightInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
Anthropometric_waistCircumferenceInMeters: Property = Property(name="waistCircumferenceInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
Anthropometric.attributes={Anthropometric_weightInKg, Anthropometric_headBreadthInMeters, Anthropometric_headLengthInMeters, Anthropometric_bideltoidBreadthInMeters, Anthropometric_statureInMeters, Anthropometric_sittingHeightInMeters, Anthropometric_waistCircumferenceInMeters}

# hyperExtension class attributes and methods
hyperExtension_maxValue: Property = Property(name="maxValue", type=IntegerType, multiplicity=Multiplicity(0, 1))
hyperExtension_minValue: Property = Property(name="minValue", type=IntegerType, multiplicity=Multiplicity(0, 1))
hyperExtension.attributes={hyperExtension_maxValue, hyperExtension_minValue}

# shoulder class attributes and methods
shoulder_externalRotation: Property = Property(name="externalRotation", type=IntegerType, multiplicity=Multiplicity(0, 1))
shoulder_internalRotation: Property = Property(name="internalRotation", type=IntegerType, multiplicity=Multiplicity(0, 1))
shoulder.attributes={shoulder_externalRotation, shoulder_internalRotation}

# finger class attributes and methods
finger_extensionB: Property = Property(name="extensionB", type=IntegerType, multiplicity=Multiplicity(0, 1))
finger_flexionC: Property = Property(name="flexionC", type=IntegerType, multiplicity=Multiplicity(0, 1))
finger_abductionA: Property = Property(name="abductionA", type=IntegerType, multiplicity=Multiplicity(0, 1))
finger_adductionB: Property = Property(name="adductionB", type=IntegerType, multiplicity=Multiplicity(0, 1))
finger_hyperExtensionC: Property = Property(name="hyperExtensionC", type=IntegerType, multiplicity=Multiplicity(0, 1))
finger_adductionA: Property = Property(name="adductionA", type=IntegerType, multiplicity=Multiplicity(0, 1))
finger_hyperExtensionB: Property = Property(name="hyperExtensionB", type=IntegerType, multiplicity=Multiplicity(0, 1))
finger_extensionA: Property = Property(name="extensionA", type=IntegerType, multiplicity=Multiplicity(0, 1))
finger_flexionB: Property = Property(name="flexionB", type=IntegerType, multiplicity=Multiplicity(0, 1))
finger_flexionA: Property = Property(name="flexionA", type=IntegerType, multiplicity=Multiplicity(0, 1))
finger_abductionB: Property = Property(name="abductionB", type=IntegerType, multiplicity=Multiplicity(0, 1))
finger_hyperExtensionA: Property = Property(name="hyperExtensionA", type=IntegerType, multiplicity=Multiplicity(0, 1))
finger.attributes={finger_extensionB, finger_flexionC, finger_abductionA, finger_adductionB, finger_hyperExtensionC, finger_adductionA, finger_hyperExtensionB, finger_extensionA, finger_flexionB, finger_flexionA, finger_abductionB, finger_hyperExtensionA}

# thigh class attributes and methods

# wrist class attributes and methods
wrist_urnalDeviation: Property = Property(name="urnalDeviation", type=IntegerType, multiplicity=Multiplicity(0, 1))
wrist_radialDeviation: Property = Property(name="radialDeviation", type=IntegerType, multiplicity=Multiplicity(0, 1))
wrist.attributes={wrist_urnalDeviation, wrist_radialDeviation}

# extension class attributes and methods
extension_minValue: Property = Property(name="minValue", type=IntegerType, multiplicity=Multiplicity(0, 1))
extension_maxValue: Property = Property(name="maxValue", type=IntegerType, multiplicity=Multiplicity(0, 1))
extension.attributes={extension_minValue, extension_maxValue}

# flexion class attributes and methods
flexion_maxValue: Property = Property(name="maxValue", type=IntegerType, multiplicity=Multiplicity(0, 1))
flexion_minValue: Property = Property(name="minValue", type=IntegerType, multiplicity=Multiplicity(0, 1))
flexion.attributes={flexion_maxValue, flexion_minValue}

# Disability class attributes and methods
Disability_description: Property = Property(name="description", type=StringType, multiplicity=Multiplicity(0, 1))
Disability_affects: Property = Property(name="affects", type=AspectsEnum, multiplicity=Multiplicity(0, 1))
Disability_name: Property = Property(name="name", type=StringType)
Disability.attributes={Disability_description, Disability_affects, Disability_name}

# Accessibility class attributes and methods

# toe class attributes and methods

# Hearing class attributes and methods
Hearing_hearingAt2kHz: Property = Property(name="hearingAt2kHz", type=IntegerType, multiplicity=Multiplicity(0, 1))
Hearing_hearingAt1kHz: Property = Property(name="hearingAt1kHz", type=IntegerType, multiplicity=Multiplicity(0, 1))
Hearing_hearingAt500Hz: Property = Property(name="hearingAt500Hz", type=IntegerType, multiplicity=Multiplicity(0, 1))
Hearing_hearingAt8kHz: Property = Property(name="hearingAt8kHz", type=IntegerType, multiplicity=Multiplicity(0, 1))
Hearing_hearingAt250Hz: Property = Property(name="hearingAt250Hz", type=IntegerType, multiplicity=Multiplicity(0, 1))
Hearing_hearingAt4kHz: Property = Property(name="hearingAt4kHz", type=IntegerType, multiplicity=Multiplicity(0, 1))
Hearing.attributes={Hearing_hearingAt2kHz, Hearing_hearingAt1kHz, Hearing_hearingAt500Hz, Hearing_hearingAt8kHz, Hearing_hearingAt250Hz, Hearing_hearingAt4kHz}

# upperLimbAnthropometric class attributes and methods
upperLimbAnthropometric_shoulderElbowLengthInMeters: Property = Property(name="shoulderElbowLengthInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
upperLimbAnthropometric_bicepsCircumferenceRelaxedInMeters: Property = Property(name="bicepsCircumferenceRelaxedInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
upperLimbAnthropometric_forarmLengthInMeters: Property = Property(name="forarmLengthInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
upperLimbAnthropometric_bicepsCircumferenceFlexedInMeters: Property = Property(name="bicepsCircumferenceFlexedInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
upperLimbAnthropometric.attributes={upperLimbAnthropometric_shoulderElbowLengthInMeters, upperLimbAnthropometric_bicepsCircumferenceRelaxedInMeters, upperLimbAnthropometric_forarmLengthInMeters, upperLimbAnthropometric_bicepsCircumferenceFlexedInMeters}

# knee class attributes and methods
knee_flexionForce: Property = Property(name="flexionForce", type=IntegerType, multiplicity=Multiplicity(0, 1))
knee_extensionForce: Property = Property(name="extensionForce", type=IntegerType, multiplicity=Multiplicity(0, 1))
knee.attributes={knee_flexionForce, knee_extensionForce}

# Sight class attributes and methods
Sight_visualAcuity: Property = Property(name="visualAcuity", type=FloatType, multiplicity=Multiplicity(0, 1))
Sight_contrastSensitivity: Property = Property(name="contrastSensitivity", type=FloatType, multiplicity=Multiplicity(0, 1))
Sight_spectralSensitivity: Property = Property(name="spectralSensitivity", type=FloatType, multiplicity=Multiplicity(0, 1))
Sight_blindSpotCount: Property = Property(name="blindSpotCount", type=IntegerType, multiplicity=Multiplicity(0, 1))
Sight_nearVisualAcuity: Property = Property(name="nearVisualAcuity", type=FloatType, multiplicity=Multiplicity(0, 1))
Sight_glareSensitivity: Property = Property(name="glareSensitivity", type=FloatType, multiplicity=Multiplicity(0, 1))
Sight_blindSpotSize: Property = Property(name="blindSpotSize", type=FloatType, multiplicity=Multiplicity(0, 1))
Sight_blindSpotArea: Property = Property(name="blindSpotArea", type=FloatType, multiplicity=Multiplicity(0, 1))
Sight_blindSpotOpacity: Property = Property(name="blindSpotOpacity", type=IntegerType, multiplicity=Multiplicity(0, 1))
Sight_distorsion: Property = Property(name="distorsion", type=FloatType, multiplicity=Multiplicity(0, 1))
Sight_colorBlindness: Property = Property(name="colorBlindness", type=ColorBlindnessEnum, multiplicity=Multiplicity(0, 1))
Sight.attributes={Sight_visualAcuity, Sight_contrastSensitivity, Sight_spectralSensitivity, Sight_blindSpotCount, Sight_nearVisualAcuity, Sight_glareSensitivity, Sight_blindSpotSize, Sight_blindSpotArea, Sight_blindSpotOpacity, Sight_distorsion, Sight_colorBlindness}

# elbow class attributes and methods

# hand class attributes and methods
hand_pronation: Property = Property(name="pronation", type=IntegerType, multiplicity=Multiplicity(0, 1))
hand_supination: Property = Property(name="supination", type=IntegerType, multiplicity=Multiplicity(0, 1))
hand.attributes={hand_pronation, hand_supination}

# forearm class attributes and methods
forearm_pronation: Property = Property(name="pronation", type=IntegerType, multiplicity=Multiplicity(0, 1))
forearm_supination: Property = Property(name="supination", type=IntegerType, multiplicity=Multiplicity(0, 1))
forearm.attributes={forearm_pronation, forearm_supination}

# Cognitive class attributes and methods
Cognitive_ICTLiteracy: Property = Property(name="ICTLiteracy", type=IntegerType, multiplicity=Multiplicity(0, 1))
Cognitive_languageReception: Property = Property(name="languageReception", type=IntegerType, multiplicity=Multiplicity(0, 1))
Cognitive_ICTAnxiousness: Property = Property(name="ICTAnxiousness", type=IntegerType, multiplicity=Multiplicity(0, 1))
Cognitive_neuroCognitivePerformanceTest: Property = Property(name="neuroCognitivePerformanceTest", type=StringType)
Cognitive_languageProduction: Property = Property(name="languageProduction", type=IntegerType, multiplicity=Multiplicity(0, 1))
Cognitive_understandingAbstractSigns: Property = Property(name="understandingAbstractSigns", type=IntegerType, multiplicity=Multiplicity(0, 1))
Cognitive_trailMakingTest: Property = Property(name="trailMakingTest", type=IntegerType, multiplicity=Multiplicity(0, 1))
Cognitive_physiologicalArousal: Property = Property(name="physiologicalArousal", type=IntegerType, multiplicity=Multiplicity(0, 1))
Cognitive_valence: Property = Property(name="valence", type=IntegerType, multiplicity=Multiplicity(0, 1))
Cognitive_visuospatialAbilities: Property = Property(name="visuospatialAbilities", type=IntegerType, multiplicity=Multiplicity(0, 1))
Cognitive_emotionalIntelligence: Property = Property(name="emotionalIntelligence", type=IntegerType, multiplicity=Multiplicity(0, 1))
Cognitive_ProcessingSpeed: Property = Property(name="ProcessingSpeed", type=IntegerType, multiplicity=Multiplicity(0, 1))
Cognitive.attributes={Cognitive_ICTLiteracy, Cognitive_languageReception, Cognitive_ICTAnxiousness, Cognitive_neuroCognitivePerformanceTest, Cognitive_languageProduction, Cognitive_understandingAbstractSigns, Cognitive_trailMakingTest, Cognitive_physiologicalArousal, Cognitive_valence, Cognitive_visuospatialAbilities, Cognitive_emotionalIntelligence, Cognitive_ProcessingSpeed}

# lowerLimb class attributes and methods
lowerLimb_ankleEversion: Property = Property(name="ankleEversion", type=IntegerType, multiplicity=Multiplicity(0, 1))
lowerLimb_ankleDorsiFlexion: Property = Property(name="ankleDorsiFlexion", type=IntegerType, multiplicity=Multiplicity(0, 1))
lowerLimb_anklePlantarFlexion: Property = Property(name="anklePlantarFlexion", type=IntegerType, multiplicity=Multiplicity(0, 1))
lowerLimb.attributes={lowerLimb_ankleEversion, lowerLimb_ankleDorsiFlexion, lowerLimb_anklePlantarFlexion}

# hip class attributes and methods
hip_flexionTorque: Property = Property(name="flexionTorque", type=IntegerType, multiplicity=Multiplicity(0, 1))
hip_internalRotation: Property = Property(name="internalRotation", type=IntegerType, multiplicity=Multiplicity(0, 1))
hip_extensionTorque: Property = Property(name="extensionTorque", type=IntegerType, multiplicity=Multiplicity(0, 1))
hip_abduction: Property = Property(name="abduction", type=IntegerType, multiplicity=Multiplicity(0, 1))
hip_adduction: Property = Property(name="adduction", type=IntegerType, multiplicity=Multiplicity(0, 1))
hip_externalRotation: Property = Property(name="externalRotation", type=IntegerType, multiplicity=Multiplicity(0, 1))
hip.attributes={hip_flexionTorque, hip_internalRotation, hip_extensionTorque, hip_abduction, hip_adduction, hip_externalRotation}

# Phonation class attributes and methods
Phonation_voicePitch: Property = Property(name="voicePitch", type=FloatType, multiplicity=Multiplicity(0, 1))
Phonation_fundamentalFrequency: Property = Property(name="fundamentalFrequency", type=FloatType, multiplicity=Multiplicity(0, 1))
Phonation_syllableDuration: Property = Property(name="syllableDuration", type=FloatType, multiplicity=Multiplicity(0, 1))
Phonation.attributes={Phonation_voicePitch, Phonation_fundamentalFrequency, Phonation_syllableDuration}

# Gait class attributes and methods
Gait_stepLengthInMeters: Property = Property(name="stepLengthInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
Gait_stepWidthInMeters: Property = Property(name="stepWidthInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
Gait_stepAssymetry: Property = Property(name="stepAssymetry", type=IntegerType, multiplicity=Multiplicity(0, 1))
Gait_doubleSupport: Property = Property(name="doubleSupport", type=IntegerType, multiplicity=Multiplicity(0, 1))
Gait_footContact: Property = Property(name="footContact", type=IntegerType, multiplicity=Multiplicity(0, 1))
Gait_velocity: Property = Property(name="velocity", type=IntegerType, multiplicity=Multiplicity(0, 1))
Gait_cadence: Property = Property(name="cadence", type=IntegerType, multiplicity=Multiplicity(0, 1))
Gait_weightShift: Property = Property(name="weightShift", type=IntegerType, multiplicity=Multiplicity(0, 1))
Gait_gaitCycle: Property = Property(name="gaitCycle", type=IntegerType, multiplicity=Multiplicity(0, 1))
Gait_strideLengthInMeters: Property = Property(name="strideLengthInMeters", type=FloatType, multiplicity=Multiplicity(0, 1))
Gait.attributes={Gait_stepLengthInMeters, Gait_stepWidthInMeters, Gait_stepAssymetry, Gait_doubleSupport, Gait_footContact, Gait_velocity, Gait_cadence, Gait_weightShift, Gait_gaitCycle, Gait_strideLengthInMeters}

# UpperLimp class attributes and methods
UpperLimp_pushForce: Property = Property(name="pushForce", type=IntegerType, multiplicity=Multiplicity(0, 1))
UpperLimp_elbowTorque: Property = Property(name="elbowTorque", type=IntegerType, multiplicity=Multiplicity(0, 1))
UpperLimp_outForce: Property = Property(name="outForce", type=IntegerType, multiplicity=Multiplicity(0, 1))
UpperLimp_inForce: Property = Property(name="inForce", type=IntegerType, multiplicity=Multiplicity(0, 1))
UpperLimp_pullForce: Property = Property(name="pullForce", type=IntegerType, multiplicity=Multiplicity(0, 1))
UpperLimp.attributes={UpperLimp_pushForce, UpperLimp_elbowTorque, UpperLimp_outForce, UpperLimp_inForce, UpperLimp_pullForce}

# Mobility class attributes and methods

# Relationships
shoulder_UpperLimp_non_navigable: BinaryAssociation = BinaryAssociation(
    name="shoulder_UpperLimp_non_navigable",
    ends={
        Property(name="UpperLimp_end", type=UpperLimp, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="shoulder_end", type=shoulder, multiplicity=Multiplicity(0, 1))
    }
)
Phonation_Speech_non_navigable: BinaryAssociation = BinaryAssociation(
    name="Phonation_Speech_non_navigable",
    ends={
        Property(name="Phonation_end", type=Phonation, multiplicity=Multiplicity(1, 1)),
        Property(name="Speech_end", type=Speech, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
flexion_elbow_non_navigable: BinaryAssociation = BinaryAssociation(
    name="flexion_elbow_non_navigable",
    ends={
        Property(name="elbow_end", type=elbow, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="flexion_end", type=flexion, multiplicity=Multiplicity(0, 1))
    }
)
flexion_knee_non_navigable: BinaryAssociation = BinaryAssociation(
    name="flexion_knee_non_navigable",
    ends={
        Property(name="knee_end", type=knee, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="flexion_end", type=flexion, multiplicity=Multiplicity(0, 1))
    }
)
UpperLimp_Mobility_non_navigable_1: BinaryAssociation = BinaryAssociation(
    name="UpperLimp_Mobility_non_navigable_1",
    ends={
        Property(name="Mobility_end", type=Mobility, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="right", type=UpperLimp, multiplicity=Multiplicity(1, 1))
    }
)
Accessibility_Sight_association: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Sight_association",
    ends={
        Property(name="Sight_end", type=Sight, multiplicity=Multiplicity(0, 1)),
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Accessibility_Anthropometric_association: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Anthropometric_association",
    ends={
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="0..1", type=Anthropometric, multiplicity=Multiplicity(1, 1))
    }
)
Cognitive_Attention_association_1: BinaryAssociation = BinaryAssociation(
    name="Cognitive_Attention_association_1",
    ends={
        Property(name="0..1", type=Attention, multiplicity=Multiplicity(1, 1)),
        Property(name="Cognitive_end", type=Cognitive, multiplicity=Multiplicity(1, 1))
    }
)
hyperExtension_knee_non_navigable: BinaryAssociation = BinaryAssociation(
    name="hyperExtension_knee_non_navigable",
    ends={
        Property(name="knee_end", type=knee, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="hyperExtension_end", type=hyperExtension, multiplicity=Multiplicity(0, 1))
    }
)
Accessibility_Memory_association: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Memory_association",
    ends={
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Memory_end", type=Memory, multiplicity=Multiplicity(0, 1))
    }
)
Accessibility_Motoric_association: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Motoric_association",
    ends={
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Motoric_end", type=Motoric, multiplicity=Multiplicity(0, 1))
    }
)
wrist_UpperLimp_non_navigable: BinaryAssociation = BinaryAssociation(
    name="wrist_UpperLimp_non_navigable",
    ends={
        Property(name="wrist_end", type=wrist, multiplicity=Multiplicity(0, 1)),
        Property(name="UpperLimp_end", type=UpperLimp, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
lowerLimb_Mobility_non_navigable: BinaryAssociation = BinaryAssociation(
    name="lowerLimb_Mobility_non_navigable",
    ends={
        Property(name="right", type=lowerLimb, multiplicity=Multiplicity(1, 1)),
        Property(name="Mobility_end", type=Mobility, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Accessibility_Hearing_association_2: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Hearing_association_2",
    ends={
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Hearing_end", type=Hearing, multiplicity=Multiplicity(0, 1))
    }
)
extension_spinalColumn_non_navigable: BinaryAssociation = BinaryAssociation(
    name="extension_spinalColumn_non_navigable",
    ends={
        Property(name="spinalColumn_end", type=spinalColumn, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="extension_end", type=extension, multiplicity=Multiplicity(0, 1))
    }
)
flexion_hip_non_navigable: BinaryAssociation = BinaryAssociation(
    name="flexion_hip_non_navigable",
    ends={
        Property(name="flexion_end", type=flexion, multiplicity=Multiplicity(0, 1)),
        Property(name="hip_end", type=hip, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
extension_hip_non_navigable: BinaryAssociation = BinaryAssociation(
    name="extension_hip_non_navigable",
    ends={
        Property(name="hip_end", type=hip, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="extension_end", type=extension, multiplicity=Multiplicity(0, 1))
    }
)
spinalColumn_Mobility_non_navigable: BinaryAssociation = BinaryAssociation(
    name="spinalColumn_Mobility_non_navigable",
    ends={
        Property(name="Mobility_end", type=Mobility, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="spinalColumn_end", type=spinalColumn, multiplicity=Multiplicity(0, 1))
    }
)
Anthropometric_upperLimbAnthropometric_association_1: BinaryAssociation = BinaryAssociation(
    name="Anthropometric_upperLimbAnthropometric_association_1",
    ends={
        Property(name="Anthropometric_end", type=Anthropometric, multiplicity=Multiplicity(1, 1)),
        Property(name="upperLimbAnthropometric_end", type=upperLimbAnthropometric, multiplicity=Multiplicity(0, 1))
    }
)
Accessibility_Motoric_association_1: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Motoric_association_1",
    ends={
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1)),
        Property(name="Motoric_end", type=Motoric, multiplicity=Multiplicity(0, 1))
    }
)
Accessibility_Sight_association_2: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Sight_association_2",
    ends={
        Property(name="Sight_end", type=Sight, multiplicity=Multiplicity(0, 1)),
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
extension_shoulder_non_navigable: BinaryAssociation = BinaryAssociation(
    name="extension_shoulder_non_navigable",
    ends={
        Property(name="shoulder_end", type=shoulder, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="extension_end", type=extension, multiplicity=Multiplicity(0, 1))
    }
)
lowerLimb_thigh_association: BinaryAssociation = BinaryAssociation(
    name="lowerLimb_thigh_association",
    ends={
        Property(name="thigh_end", type=thigh, multiplicity=Multiplicity(0, 1)),
        Property(name="lowerLimb_end", type=lowerLimb, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Accessibility_Sight_association_1: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Sight_association_1",
    ends={
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1)),
        Property(name="Sight_end", type=Sight, multiplicity=Multiplicity(0, 1))
    }
)
hip_lowerLimb_non_navigable: BinaryAssociation = BinaryAssociation(
    name="hip_lowerLimb_non_navigable",
    ends={
        Property(name="hip_end", type=hip, multiplicity=Multiplicity(1, 1)),
        Property(name="lowerLimb_end", type=lowerLimb, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
UpperLimp_Mobility_non_navigable: BinaryAssociation = BinaryAssociation(
    name="UpperLimp_Mobility_non_navigable",
    ends={
        Property(name="left", type=UpperLimp, multiplicity=Multiplicity(1, 1)),
        Property(name="Mobility_end", type=Mobility, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
extension_wrist_non_navigable: BinaryAssociation = BinaryAssociation(
    name="extension_wrist_non_navigable",
    ends={
        Property(name="wrist_end", type=wrist, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="extension_end", type=extension, multiplicity=Multiplicity(0, 1))
    }
)
knee_wrist_non_navigable: BinaryAssociation = BinaryAssociation(
    name="knee_wrist_non_navigable",
    ends={
        Property(name="wrist_end", type=wrist, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="knee_end", type=knee, multiplicity=Multiplicity(0, 1))
    }
)
extension_toe_non_navigable: BinaryAssociation = BinaryAssociation(
    name="extension_toe_non_navigable",
    ends={
        Property(name="toe_end", type=toe, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="extension_end", type=extension, multiplicity=Multiplicity(0, 1))
    }
)
Neck_Mobility_non_navigable: BinaryAssociation = BinaryAssociation(
    name="Neck_Mobility_non_navigable",
    ends={
        Property(name="Mobility_end", type=Mobility, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Neck_end", type=Neck, multiplicity=Multiplicity(0, 1))
    }
)
Accessibility_Hearing_association: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Hearing_association",
    ends={
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Hearing_end", type=Hearing, multiplicity=Multiplicity(0, 1))
    }
)
Accessibility_Hearing_association_1: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Hearing_association_1",
    ends={
        Property(name="Hearing_end", type=Hearing, multiplicity=Multiplicity(0, 1)),
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1))
    }
)
Accessibility_PhysiologicalState_association: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Physiological State_association",
    ends={
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Physiological State_end", type=PhysiologicalState, multiplicity=Multiplicity(0, 1))
    }
)
extension_Neck_non_navigable: BinaryAssociation = BinaryAssociation(
    name="extension_Neck_non_navigable",
    ends={
        Property(name="extension_end", type=extension, multiplicity=Multiplicity(0, 1)),
        Property(name="Neck_end", type=Neck, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Accessibility_Speech_association_1: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Speech_association_1",
    ends={
        Property(name="Speech_end", type=Speech, multiplicity=Multiplicity(0, 1)),
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1))
    }
)
Accessibility_Sight_association_3: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Sight_association_3",
    ends={
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1)),
        Property(name="Sight_end", type=Sight, multiplicity=Multiplicity(0, 1))
    }
)
Accessibility_Anthropometric_association_1: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Anthropometric_association_1",
    ends={
        Property(name="0..1", type=Anthropometric, multiplicity=Multiplicity(1, 1)),
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1))
    }
)
Prosody_Speech_non_navigable: BinaryAssociation = BinaryAssociation(
    name="Prosody_Speech_non_navigable",
    ends={
        Property(name="Speech_end", type=Speech, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Prosody_end", type=Prosody, multiplicity=Multiplicity(1, 1))
    }
)
Gait_Mobility_non_navigable: BinaryAssociation = BinaryAssociation(
    name="Gait_Mobility_non_navigable",
    ends={
        Property(name="Mobility_end", type=Mobility, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Gait_end", type=Gait, multiplicity=Multiplicity(0, 1))
    }
)
Anthropometric_upperLimbAnthropometric_association: BinaryAssociation = BinaryAssociation(
    name="Anthropometric_upperLimbAnthropometric_association",
    ends={
        Property(name="upperLimbAnthropometric_end", type=upperLimbAnthropometric, multiplicity=Multiplicity(0, 1)),
        Property(name="Anthropometric_end", type=Anthropometric, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Accessibility_PhysiologicalState_association_1: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Physiological State_association_1",
    ends={
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1)),
        Property(name="Physiological State_end", type=PhysiologicalState, multiplicity=Multiplicity(0, 1))
    }
)
elbow_UpperLimp_non_navigable: BinaryAssociation = BinaryAssociation(
    name="elbow_UpperLimp_non_navigable",
    ends={
        Property(name="UpperLimp_end", type=UpperLimp, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="elbow_end", type=elbow, multiplicity=Multiplicity(0, 1))
    }
)
lowerLimb_thigh_association_1: BinaryAssociation = BinaryAssociation(
    name="lowerLimb_thigh_association_1",
    ends={
        Property(name="thigh_end", type=thigh, multiplicity=Multiplicity(0, 1)),
        Property(name="lowerLimb_end", type=lowerLimb, multiplicity=Multiplicity(1, 1))
    }
)
wrist_lowerLimb_non_navigable: BinaryAssociation = BinaryAssociation(
    name="wrist_lowerLimb_non_navigable",
    ends={
        Property(name="lowerLimb_end", type=lowerLimb, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="wrist_end", type=wrist, multiplicity=Multiplicity(0, 1))
    }
)
Accessibility_Cognitive_association_1: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Cognitive_association_1",
    ends={
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1)),
        Property(name="Cognitive_end", type=Cognitive, multiplicity=Multiplicity(0, 1))
    }
)
Cognitive_EmotionalIntelligence_association: BinaryAssociation = BinaryAssociation(
    name="Cognitive_EmotionalIntelligence_association",
    ends={
        Property(name="Cognitive_end", type=Cognitive, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="0..1", type=EmotionalIntelligence, multiplicity=Multiplicity(1, 1))
    }
)
hand_UpperLimp_non_navigable: BinaryAssociation = BinaryAssociation(
    name="hand_UpperLimp_non_navigable",
    ends={
        Property(name="UpperLimp_end", type=UpperLimp, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="hand_end", type=hand, multiplicity=Multiplicity(0, 1))
    }
)
flexion_shoulder_non_navigable: BinaryAssociation = BinaryAssociation(
    name="flexion_shoulder_non_navigable",
    ends={
        Property(name="flexion_end", type=flexion, multiplicity=Multiplicity(0, 1)),
        Property(name="shoulder_end", type=shoulder, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Anthropometric_lowerLimbAnthropometric_association: BinaryAssociation = BinaryAssociation(
    name="Anthropometric_lowerLimbAnthropometric_association",
    ends={
        Property(name="lowerLimbAnthropometric_end", type=lowerLimbAnthropometric, multiplicity=Multiplicity(0, 1)),
        Property(name="Anthropometric_end", type=Anthropometric, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Accessibility_Disability_association: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Disability_association",
    ends={
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Disability_end", type=Disability, multiplicity=Multiplicity(0, 9999))
    }
)
lowerLimb_Mobility_non_navigable_1: BinaryAssociation = BinaryAssociation(
    name="lowerLimb_Mobility_non_navigable_1",
    ends={
        Property(name="Mobility_end", type=Mobility, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="left", type=lowerLimb, multiplicity=Multiplicity(1, 1))
    }
)
Accessibility_Hearing_association_3: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Hearing_association_3",
    ends={
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1)),
        Property(name="Hearing_end", type=Hearing, multiplicity=Multiplicity(0, 1))
    }
)
flexion_toe_non_navigable: BinaryAssociation = BinaryAssociation(
    name="flexion_toe_non_navigable",
    ends={
        Property(name="flexion_end", type=flexion, multiplicity=Multiplicity(0, 1)),
        Property(name="toe_end", type=toe, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Accessibility_Mobility_association: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Mobility_association",
    ends={
        Property(name="Mobility_end", type=Mobility, multiplicity=Multiplicity(0, 1)),
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Cognitive_EmotionalIntelligence_association_1: BinaryAssociation = BinaryAssociation(
    name="Cognitive_EmotionalIntelligence_association_1",
    ends={
        Property(name="0..1", type=EmotionalIntelligence, multiplicity=Multiplicity(1, 1)),
        Property(name="Cognitive_end", type=Cognitive, multiplicity=Multiplicity(1, 1))
    }
)
forearm_UpperLimp_non_navigable: BinaryAssociation = BinaryAssociation(
    name="forearm_UpperLimp_non_navigable",
    ends={
        Property(name="forearm_end", type=forearm, multiplicity=Multiplicity(0, 1)),
        Property(name="UpperLimp_end", type=UpperLimp, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Accessibility_Cognitive_association: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Cognitive_association",
    ends={
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Cognitive_end", type=Cognitive, multiplicity=Multiplicity(0, 1))
    }
)
Accessibility_Mobility_association_1: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Mobility_association_1",
    ends={
        Property(name="Mobility_end", type=Mobility, multiplicity=Multiplicity(0, 1)),
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1))
    }
)
Anthropometric_lowerLimbAnthropometric_association_1: BinaryAssociation = BinaryAssociation(
    name="Anthropometric_lowerLimbAnthropometric_association_1",
    ends={
        Property(name="Anthropometric_end", type=Anthropometric, multiplicity=Multiplicity(1, 1)),
        Property(name="lowerLimbAnthropometric_end", type=lowerLimbAnthropometric, multiplicity=Multiplicity(0, 1))
    }
)
hyperExtension_elbow_non_navigable: BinaryAssociation = BinaryAssociation(
    name="hyperExtension_elbow_non_navigable",
    ends={
        Property(name="hyperExtension_end", type=hyperExtension, multiplicity=Multiplicity(0, 1)),
        Property(name="elbow_end", type=elbow, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Accessibility_Memory_association_1: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Memory_association_1",
    ends={
        Property(name="Memory_end", type=Memory, multiplicity=Multiplicity(0, 1)),
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1))
    }
)
Accessibility_Disability_association_1: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Disability_association_1",
    ends={
        Property(name="Disability_end", type=Disability, multiplicity=Multiplicity(0, 9999)),
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1))
    }
)
Cognitive_Attention_association: BinaryAssociation = BinaryAssociation(
    name="Cognitive_Attention_association",
    ends={
        Property(name="0..1", type=Attention, multiplicity=Multiplicity(1, 1)),
        Property(name="Cognitive_end", type=Cognitive, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
finger_hand_non_navigable: BinaryAssociation = BinaryAssociation(
    name="finger_hand_non_navigable",
    ends={
        Property(name="finger_end", type=finger, multiplicity=Multiplicity(0, 5)),
        Property(name="hand_end", type=hand, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
toe_lowerLimb_non_navigable: BinaryAssociation = BinaryAssociation(
    name="toe_lowerLimb_non_navigable",
    ends={
        Property(name="toe_end", type=toe, multiplicity=Multiplicity(0, 5)),
        Property(name="lowerLimb_end", type=lowerLimb, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
extension_thigh_non_navigable: BinaryAssociation = BinaryAssociation(
    name="extension_thigh_non_navigable",
    ends={
        Property(name="extension_end", type=extension, multiplicity=Multiplicity(0, 1)),
        Property(name="thigh_end", type=thigh, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Accessibility_Speech_association: BinaryAssociation = BinaryAssociation(
    name="Accessibility_Speech_association",
    ends={
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Speech_end", type=Speech, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model



# Personal Information class attributes and methods

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
Hobby = Class(name="Hobby")
Sport = Class(name="Sport")
Other = Class(name="Other")
Recreation = Class(name="Recreation")
Environment = Class(name="Environment")
Interest = Class(name="Interest")

VideoGames = Class(name="VideoGames")

# Music class attributes and methods
Music_genres: Property = Property(name="genres", type=MusicGenreEnum, multiplicity=Multiplicity(0,"*"))
Music.attributes={Music_genres}

# Science class attributes and methods
Science_fields: Property = Property(name="fields", type=ScienceFieldEnum, multiplicity=Multiplicity(0,"*"))
Science.attributes={Science_fields}

# Film class attributes and methods
Film_genres: Property = Property(name="genres", type=FilmGenreEnum, multiplicity=Multiplicity(0,"*"))
Film.attributes={Film_genres}

# PersonalInformation class attributes and methods
PersonalInformation_sexuality: Property = Property(name="sexuality", type=SexualityEnum, multiplicity=Multiplicity(0,1))
PersonalInformation_gender: Property = Property(name="gender", type=GenderEnum, multiplicity=Multiplicity(0,1))
PersonalInformation_age: Property = Property(name="age", type=IntegerType, multiplicity=Multiplicity(0,1))
PersonalInformation_address: Property = Property(name="address", type=StringType, multiplicity=Multiplicity(0,1))
PersonalInformation_politicalBelief: Property = Property(name="politicalBelief", type=PoliticalEnum, multiplicity=Multiplicity(0,1))
PersonalInformation_lastName: Property = Property(name="lastName", type=StringType, multiplicity=Multiplicity(0,1))
PersonalInformation_firstName: Property = Property(name="firstName", type=StringType, multiplicity=Multiplicity(0,1))
PersonalInformation_nationality_iso3166: Property = Property(name="nationality_iso3166", type=StringType, multiplicity=Multiplicity(0,"*"))
PersonalInformation.attributes={PersonalInformation_sexuality, PersonalInformation_gender, PersonalInformation_age, PersonalInformation_address, PersonalInformation_politicalBelief, PersonalInformation_lastName, PersonalInformation_firstName, PersonalInformation_nationality_iso3166}

# Hobby class attributes and methods
Hobby_weeklyTime: Property = Property(name="weeklyTime", type=IntegerType, multiplicity=Multiplicity(0,1))
Hobby.attributes={Hobby_weeklyTime}

# Sport class attributes and methods
Sport_disciplines: Property = Property(name="disciplines", type=SportEnum, multiplicity=Multiplicity(0,1))
Sport.attributes={Sport_disciplines}

# Other class attributes and methods
Other_name: Property = Property(name="name", type=StringType)
Other_description: Property = Property(name="description", type=StringType)
Other.attributes={Other_name, Other_description}

# Recreation class attributes and methods
Recreation_types: Property = Property(name="types", type=RecreationEnum, multiplicity=Multiplicity(0,1))
Recreation.attributes={Recreation_types}

# Environment class attributes and methods
Environment_topics: Property = Property(name="topics", type=EnvironmentEnum, multiplicity=Multiplicity(0,1))
Environment.attributes={Environment_topics}

# Interest class attributes and methods

# Topic class attributes and methods

# VideoGames class attributes and methods
VideoGames_genres: Property = Property(name="genres", type=GameGenreEnum, multiplicity=Multiplicity(0,1))
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


# User class attributes and methods

# Personality class attributes and methods
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
Attitude = Class(name="Attitude")
Neuroticism = Class(name="Neuroticism")
ExtraversionToIntroversion = Class(name="ExtraversionToIntroversion")
Big_Five_Traits = Class(name="Big_Five_Traits")
MyersBriggsTypeInventory = Class(name="MyersBriggsTypeInventory")
JudgingToPerceiving = Class(name="JudgingToPerceiving")
OtherTrait = Class(name="OtherTrait")
Extraversion = Class(name="Extraversion")
Openness = Class(name="Openness")
Conscientiousness = Class(name="Conscientiousness")
Agreeableness = Class(name="Agreeableness")
Intraphysic = Class(name="Intraphysic_Self")

# Interpersonal class attributes and methods
Interpersonal_belongingImportance: Property = Property(name="belongingImportance", type=IntegerType, multiplicity=Multiplicity(0,1))
Interpersonal_nurturanceImportance: Property = Property(name="nurturanceImportance", type=IntegerType, multiplicity=Multiplicity(0,1))
Interpersonal_esteemImportance: Property = Property(name="esteemImportance", type=IntegerType, multiplicity=Multiplicity(0,1))
Interpersonal.attributes={Interpersonal_belongingImportance, Interpersonal_nurturanceImportance, Interpersonal_esteemImportance}

# Instrumental class attributes and methods
Instrumental_engagementImportance: Property = Property(name="engagementImportance", type=IntegerType, multiplicity=Multiplicity(0,1))
Instrumental_achievementImportance: Property = Property(name="achievementImportance", type=IntegerType, multiplicity=Multiplicity(0,1))
Instrumental_empowerementImportance: Property = Property(name="empowerementImportance", type=IntegerType, multiplicity=Multiplicity(0,1))
Instrumental.attributes={Instrumental_engagementImportance, Instrumental_achievementImportance, Instrumental_empowerementImportance}

# Bias class attributes and methods

# MotivationProfile class attributes and methods

# Trait class attributes and methods
Trait_score: Property = Property(name="score", type=IntegerType)
Trait.attributes={Trait_score}

# Characteristic class attributes and methods
Characteristic_score: Property = Property(name="score", type=IntegerType)
Characteristic_name: Property = Property(name="name", type=CharacteristicsEnum)
Characteristic.attributes={Characteristic_score, Characteristic_name}

# ThinkingToFeeling class attributes and methods

# SensingToIntuition class attributes and methods

# Personality class attributes and methods

# Attitude class attributes and methods
Attitude_description: Property = Property(name="description", type=StringType, multiplicity=Multiplicity(0,1))
Attitude_negative_to_positive: Property = Property(name="negative_to_positive", type=IntegerType)
Attitude.attributes={Attitude_description, Attitude_negative_to_positive}

# Neuroticism class attributes and methods

# ExtraversionToIntroversion class attributes and methods

# Big_Five_Traits class attributes and methods

# MyersBriggsTypeInventory class attributes and methods

# JudgingToPerceiving class attributes and methods

# Other class attributes and methods
OtherTrait_name: Property = Property(name="name", type=TraitsEnum)
OtherTrait.attributes={Other_name}

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


# Goal class attributes and methods



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



# Preference class attributes and methods
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
PreferredLanguage = Class(name="PreferredLanguage")
Output_Modality = Class(name="Output_Modality")
Input_Modality = Class(name="Input_Modality")
Content = Class(name="Content")
Design = Class(name="Design")
Interaction_Modality = Class(name="Interaction_Modality")
Item = Class(name="Item")

# Preference class attributes and methods

# PreferredLanguage class attributes and methods
PreferredLanguage_style: Property = Property(name="style", type=StylesEnum, multiplicity=Multiplicity(0,1))
PreferredLanguage_iso639_1: Property = Property(name="iso639_1", type=StringType, multiplicity=Multiplicity(0,1))
PreferredLanguage.attributes={PreferredLanguage_style, PreferredLanguage_iso639_1}

# Output_Modality class attributes and methods
Output_Modality_value: Property = Property(name="value", type=OutputEnum)
Output_Modality.attributes={Output_Modality_value}

# Input_Modality class attributes and methods
Input_Modality_value: Property = Property(name="value", type=InputEnum)
Input_Modality.attributes={Input_Modality_value}

# Content class attributes and methods

# Design class attributes and methods
Design_contentContrast: Property = Property(name="contentContrast", type=IntegerType, multiplicity=Multiplicity(0,1))
Design_brightness: Property = Property(name="brightness", type=IntegerType, multiplicity=Multiplicity(0,1))
Design_textSize: Property = Property(name="textSize", type=IntegerType, multiplicity=Multiplicity(0,1))
Design_colorScheme: Property = Property(name="colorScheme", type=StringType, multiplicity=Multiplicity(0,1))
Design_police: Property = Property(name="police", type=StringType, multiplicity=Multiplicity(0,1))
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



# EmotionStatus class attributes and methods
# Enumerations
# Classes


# EmotionStatus class attributes and methods
EmotionStatus_anxiety: Property = Property(name="anxiety", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_dread: Property = Property(name="dread", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_worry: Property = Property(name="worry", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_boredom: Property = Property(name="boredom", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_fear: Property = Property(name="fear", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_hate: Property = Property(name="hate", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_joy: Property = Property(name="joy", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_satisfaction: Property = Property(name="satisfaction", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_happiness: Property = Property(name="happiness", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_love: Property = Property(name="love", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_relief: Property = Property(name="relief", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_hope: Property = Property(name="hope", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_confusion: Property = Property(name="confusion", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_pride: Property = Property(name="pride", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_sadness: Property = Property(name="sadness", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_disgust: Property = Property(name="disgust", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_anger: Property = Property(name="anger", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_shame: Property = Property(name="shame", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus_excitement: Property = Property(name="excitement", type=IntegerType, multiplicity=Multiplicity(0, 1))
EmotionStatus.attributes={EmotionStatus_anxiety, EmotionStatus_dread, EmotionStatus_worry, EmotionStatus_boredom, EmotionStatus_fear, EmotionStatus_hate, EmotionStatus_joy, EmotionStatus_satisfaction, EmotionStatus_happiness, EmotionStatus_love, EmotionStatus_relief, EmotionStatus_hope, EmotionStatus_confusion, EmotionStatus_pride, EmotionStatus_sadness, EmotionStatus_disgust, EmotionStatus_anger, EmotionStatus_shame, EmotionStatus_excitement}



# Culture class attributes and methods

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



# Culture class attributes and methods
Culture_powerDistance: Property = Property(name="powerDistance", type=IntegerType, multiplicity=Multiplicity(0, 1))
Culture_temporalOrientation: Property = Property(name="temporalOrientation", type=IntegerType, multiplicity=Multiplicity(0, 1))
Culture_restrain_to_indulgence: Property = Property(name="restrain_to_indulgence", type=IntegerType, multiplicity=Multiplicity(0, 1))
Culture_feminity_to_masculinity: Property = Property(name="feminity_to_masculinity", type=IntegerType, multiplicity=Multiplicity(0, 1))
Culture_religion: Property = Property(name="religion", type=ReligionEnum, multiplicity=Multiplicity(0, 1))
Culture_collectivism_to_individualism: Property = Property(name="collectivism_to_individualism", type=IntegerType, multiplicity=Multiplicity(0, 1))
Culture_uncertaintyAvoidance: Property = Property(name="uncertaintyAvoidance", type=IntegerType, multiplicity=Multiplicity(0, 1))
Culture.attributes={Culture_powerDistance, Culture_temporalOrientation, Culture_restrain_to_indulgence, Culture_feminity_to_masculinity, Culture_religion, Culture_collectivism_to_individualism, Culture_uncertaintyAvoidance}



# Relationship class attributes and methods
Relationship_quality: Property = Property(name="quality", type=RelationshipQualityEnum)
Relationship_type: Property = Property(name="type", type=RelationshipTypeEnum)
Relationship.attributes={Relationship_quality, Relationship_type}

# MoodStatus class attributes and methods
# Enumerations
# Classes

# MoodStatus class attributes and methods
MoodStatus_tense_to_relaxed: Property = Property(name="tense_to_relaxed", type=IntegerType)
MoodStatus_bad_to_good: Property = Property(name="bad_to_good", type=IntegerType)
MoodStatus_tired_to_energetic: Property = Property(name="tired_to_energetic", type=IntegerType)
MoodStatus.attributes={MoodStatus_tense_to_relaxed, MoodStatus_bad_to_good, MoodStatus_tired_to_energetic}





# Relationships
EmotionStatus_User_non_navigable: BinaryAssociation = BinaryAssociation(
    name="EmotionStatus_User_non_navigable",
    ends={
        Property(name="User_end", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="EmotionStatus_end", type=EmotionStatus, multiplicity=Multiplicity(0, 1))
    }
)
Culture_User_non_navigable: BinaryAssociation = BinaryAssociation(
    name="Culture_User_non_navigable",
    ends={
        Property(name="Culture_end", type=Culture, multiplicity=Multiplicity(0, 1)),
        Property(name="User_end", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
PersonalInformation_User_non_navigable: BinaryAssociation = BinaryAssociation(
    name="Personal Information_User_non_navigable",
    ends={
        Property(name="Personal Information_end", type=PersonalInformation, multiplicity=Multiplicity(0, 1)),
        Property(name="User_end", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
MoodStatus_User_non_navigable: BinaryAssociation = BinaryAssociation(
    name="MoodStatus_User_non_navigable",
    ends={
        Property(name="MoodStatus_end", type=MoodStatus, multiplicity=Multiplicity(0, 1)),
        Property(name="User_end", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
User_User_association: BinaryAssociation = BinaryAssociation(
    name="User_User_association",
    ends={
        Property(name="has", type=User, multiplicity=Multiplicity(0, 9999)),
        Property(name="User_end", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
Competence_User_non_navigable: BinaryAssociation = BinaryAssociation(
    name="Competence_User_non_navigable",
    ends={
        Property(name="Competence_end", type=Competence, multiplicity=Multiplicity(0, 1)),
        Property(name="User_end", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Preference_User_non_navigable: BinaryAssociation = BinaryAssociation(
    name="Preference_User_non_navigable",
    ends={
        Property(name="Preference_end", type=Preference, multiplicity=Multiplicity(0, 1)),
        Property(name="User_end", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
Accessibility_User_non_navigable: BinaryAssociation = BinaryAssociation(
    name="Accessibility_User_non_navigable",
    ends={
        Property(name="User_end", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Accessibility_end", type=Accessibility, multiplicity=Multiplicity(0, 1))
    }
)
Personality_User_non_navigable: BinaryAssociation = BinaryAssociation(
    name="Personality_User_non_navigable",
    ends={
        Property(name="User_end", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Personality_end", type=Personality, multiplicity=Multiplicity(0, 1))
    }
)
Goal_User_non_navigable: BinaryAssociation = BinaryAssociation(
    name="Goal_User_non_navigable",
    ends={
        Property(name="User_end", type=User, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Goal_end", type=Goal, multiplicity=Multiplicity(0, 9999))
    }
)









mood_types =  {MoodStatus}
culture_types = {Culture, ReligionEnum}
emotion_types = {EmotionStatus}
preference_types = {Preference, PreferredLanguage, Output_Modality, Input_Modality, Content, Design, Interaction_Modality, Item, OutputEnum, StylesEnum, InputEnum}
preference_associations = {Preference_Interaction_Modality_association, Preference_Content_association_1, Content_PreferredLanguage_association, Content_Item_association_1, Preference_Design_association_1, Content_Item_association, Output_Modality_Interaction_Modality_non_navigable, Input_Modality_Interaction_Modality_non_navigable, Preference_Content_association, Content_PreferredLanguage_association_1, Preference_Design_association, Preference_Interaction_Modality_association_1}
personality_types = {Interpersonal, Instrumental, Bias, MotivationProfile, Trait, Characteristic, ThinkingToFeeling, SensingToIntuition, Personality, Attitude, Neuroticism, ExtraversionToIntroversion, Big_Five_Traits, MyersBriggsTypeInventory, JudgingToPerceiving, Other, Extraversion, Openness, Topic, Conscientiousness, Agreeableness, Intraphysic, CharacteristicsEnum, TraitsEnum}
personality_associations = {Personality_MotivationProfile_association, Instrumental_MotivationProfile_non_navigable, Personality_Attitude_association_1, Interpersonal_MotivationProfile_non_navigable, Attitude_Topic_association, Personality_Trait_association, Personality_MotivationProfile_association_1, Personality_Trait_association_1, Intraphysic_MotivationProfile_non_navigable, Trait_Characteristic_association, Personality_Attitude_association, Trait_Characteristic_association_1}
personality_generalizations = {gen_Big_Five_Traits_Trait, gen_Neuroticism_Big_Five_Traits, gen_Bias_Attitude, gen_Agreeableness_Big_Five_Traits, gen_Extraversion_Big_Five_Traits, gen_Conscientiousness_Big_Five_Traits, gen_JudgingToPerceiving_MyersBriggsTypeInventory, gen_ThinkingToFeeling_MyersBriggsTypeInventory, gen_Openness_Big_Five_Traits, gen_Other_Trait, gen_SensingToIntuition_MyersBriggsTypeInventory, gen_MyersBriggsTypeInventory_Trait, gen_ExtraversionToIntroversion_MyersBriggsTypeInventory}
personal_information_types = {Music, Science, Film, PersonalInformation, Hobby, Sport, Other, Recreation, Environment, Interest, Topic, VideoGames, GenderEnum, ScienceFieldEnum, RecreationEnum, MusicGenreEnum, SexualityEnum, SportEnum, PoliticalEnum, FilmGenreEnum, EnvironmentEnum, GameGenreEnum}
personal_information_associations = {PersonalInformation_Interest_association_1, Interest_Topic_association, PersonalInformation_Interest_association}
personal_information_generalizations = {gen_Environment_Topic, gen_Recreation_Topic, gen_Sport_Topic, gen_VideoGames_Topic, gen_Music_Topic, gen_Hobby_Interest, gen_Film_Topic, gen_Other_Topic, gen_Science_Topic}
accessibility_types = {Memory, spinalColumn, Neck, Speech, Prosody, Motoric, lowerLimbAnthropometric, PhysiologicalState, Attention, EmotionalIntelligence, Anthropometric, hyperExtension, shoulder, finger, thigh, wrist, extension, flexion, Disability, Accessibility, toe, Hearing, upperLimbAnthropometric, knee, Sight, elbow, hand, forearm, Cognitive, lowerLimb, hip, Phonation, Gait, UpperLimp, Mobility, ColorBlindnessEnum, AspectsEnum}
accessibility_associations = {shoulder_UpperLimp_non_navigable, Phonation_Speech_non_navigable, flexion_elbow_non_navigable, flexion_knee_non_navigable, UpperLimp_Mobility_non_navigable_1, Accessibility_Sight_association, Accessibility_Anthropometric_association, Cognitive_Attention_association_1, hyperExtension_knee_non_navigable, Accessibility_Memory_association, Accessibility_Motoric_association, wrist_UpperLimp_non_navigable, lowerLimb_Mobility_non_navigable, Accessibility_Hearing_association_2, extension_spinalColumn_non_navigable, flexion_hip_non_navigable, extension_hip_non_navigable, spinalColumn_Mobility_non_navigable, Anthropometric_upperLimbAnthropometric_association_1, Accessibility_Motoric_association_1, Accessibility_Sight_association_2, extension_shoulder_non_navigable, lowerLimb_thigh_association, Accessibility_Sight_association_1, hip_lowerLimb_non_navigable, UpperLimp_Mobility_non_navigable, extension_wrist_non_navigable, knee_wrist_non_navigable, extension_toe_non_navigable, Neck_Mobility_non_navigable, Accessibility_Hearing_association, Accessibility_Hearing_association_1, Accessibility_PhysiologicalState_association, extension_Neck_non_navigable, Accessibility_Speech_association_1, Accessibility_Sight_association_3, Accessibility_Anthropometric_association_1, Prosody_Speech_non_navigable, Gait_Mobility_non_navigable, Anthropometric_upperLimbAnthropometric_association, Accessibility_PhysiologicalState_association_1, elbow_UpperLimp_non_navigable, lowerLimb_thigh_association_1, wrist_lowerLimb_non_navigable, Accessibility_Cognitive_association_1, Cognitive_EmotionalIntelligence_association, hand_UpperLimp_non_navigable, flexion_shoulder_non_navigable, Anthropometric_lowerLimbAnthropometric_association, Accessibility_Disability_association, lowerLimb_Mobility_non_navigable_1, Accessibility_Hearing_association_3, flexion_toe_non_navigable, Accessibility_Mobility_association, Cognitive_EmotionalIntelligence_association_1, forearm_UpperLimp_non_navigable, Accessibility_Cognitive_association, Accessibility_Mobility_association_1, Anthropometric_lowerLimbAnthropometric_association_1, hyperExtension_elbow_non_navigable, Accessibility_Memory_association_1, Accessibility_Disability_association_1, Cognitive_Attention_association, finger_hand_non_navigable, toe_lowerLimb_non_navigable, extension_thigh_non_navigable, Accessibility_Speech_association}
competence_types = {Knowledge, Education, Topic, Skill, Competence, Language, Experience, CEFR, DegreeEnum}
competence_associations = {Competence_Skill_association_1, Competence_Experience_association, Competence_Language_association, Competence_Language_association_1, Competence_Knowledge_association, Competence_Education_association, Competence_Experience_association_1, Competence_Knowledge_association_1, Competence_Education_association_1, Competence_Skill_association, Knowledge_Topic_association}
types= mood_types | culture_types | emotion_types | preference_types | personality_types | personal_information_types | accessibility_types | competence_types
associations =  preference_associations | personality_associations | personal_information_associations | accessibility_associations | competence_associations
generalizations = personality_generalizations | personal_information_generalizations
print(generalizations)
domain_model = DomainModel(
    name="Generated Model",
    types=types,
    associations=associations,
    generalizations=generalizations
)
