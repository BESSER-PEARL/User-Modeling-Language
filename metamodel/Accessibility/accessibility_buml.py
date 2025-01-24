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
Accessibility = Class(name="Accessibility")
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
Memory_workingMemory: Property = Property(name="workingMemory", type=StringType)
Memory_sensoryMemory: Property = Property(name="sensoryMemory", type=StringType)
Memory_longTermMemory: Property = Property(name="longTermMemory", type=StringType)
Memory.attributes={Memory_workingMemory, Memory_sensoryMemory, Memory_longTermMemory}

# spinalColumn class attributes and methods
spinalColumn_rightLateralFlexion: Property = Property(name="rightLateralFlexion", type=IntegerType)
spinalColumn_leftLateralFlexion: Property = Property(name="leftLateralFlexion", type=IntegerType)
spinalColumn_leftLateralRotation: Property = Property(name="leftLateralRotation", type=IntegerType)
spinalColumn_rightLateralRotation: Property = Property(name="rightLateralRotation", type=IntegerType)
spinalColumn.attributes={spinalColumn_rightLateralFlexion, spinalColumn_leftLateralFlexion, spinalColumn_leftLateralRotation, spinalColumn_rightLateralRotation}

# Neck class attributes and methods
Neck_leftLateralFlexion: Property = Property(name="leftLateralFlexion", type=IntegerType)
Neck_rightLateralRotation: Property = Property(name="rightLateralRotation", type=IntegerType)
Neck_rightLateralFlexion: Property = Property(name="rightLateralFlexion", type=IntegerType)
Neck_leftLateralRotation: Property = Property(name="leftLateralRotation", type=IntegerType)
Neck.attributes={Neck_leftLateralFlexion, Neck_rightLateralRotation, Neck_rightLateralFlexion, Neck_leftLateralRotation}

# Speech class attributes and methods

# Prosody class attributes and methods
Prosody_lipMovementCoordination: Property = Property(name="lipMovementCoordination", type=StringType)
Prosody_jawMovement: Property = Property(name="jawMovement", type=FloatType)
Prosody_vocalStress: Property = Property(name="vocalStress", type=FloatType)
Prosody.attributes={Prosody_lipMovementCoordination, Prosody_jawMovement, Prosody_vocalStress}

# Motoric class attributes and methods
Motoric_handPrecision: Property = Property(name="handPrecision", type=StringType)
Motoric_handEyeCoordination: Property = Property(name="handEyeCoordination", type=StringType)
Motoric_fingerPrecision: Property = Property(name="fingerPrecision", type=StringType)
Motoric_clenchGrip: Property = Property(name="clenchGrip", type=FloatType)
Motoric_contactGrip: Property = Property(name="contactGrip", type=FloatType)
Motoric_pinchGrip: Property = Property(name="pinchGrip", type=FloatType)
Motoric_armPrecision: Property = Property(name="armPrecision", type=StringType)
Motoric.attributes={Motoric_handPrecision, Motoric_handEyeCoordination, Motoric_fingerPrecision, Motoric_clenchGrip, Motoric_contactGrip, Motoric_pinchGrip, Motoric_armPrecision}

# lowerLimbAnthropometric class attributes and methods
lowerLimbAnthropometric_tighCircumferenceInMeters: Property = Property(name="tighCircumferenceInMeters", type=FloatType)
lowerLimbAnthropometric_kneeHeightInMeters: Property = Property(name="kneeHeightInMeters", type=FloatType)
lowerLimbAnthropometric_footLengthInMeters: Property = Property(name="footLengthInMeters", type=FloatType)
lowerLimbAnthropometric_footBreadthInMeters: Property = Property(name="footBreadthInMeters", type=FloatType)
lowerLimbAnthropometric_hipBreadthInMeters: Property = Property(name="hipBreadthInMeters", type=FloatType)
lowerLimbAnthropometric_calfCirumferenceInMeters: Property = Property(name="calfCirumferenceInMeters", type=FloatType)
lowerLimbAnthropometric_ankleHeightInMeters: Property = Property(name="ankleHeightInMeters", type=FloatType)
lowerLimbAnthropometric_buttockKneeInMeters: Property = Property(name="buttockKneeInMeters", type=FloatType)
lowerLimbAnthropometric.attributes={lowerLimbAnthropometric_tighCircumferenceInMeters, lowerLimbAnthropometric_kneeHeightInMeters, lowerLimbAnthropometric_footLengthInMeters, lowerLimbAnthropometric_footBreadthInMeters, lowerLimbAnthropometric_hipBreadthInMeters, lowerLimbAnthropometric_calfCirumferenceInMeters, lowerLimbAnthropometric_ankleHeightInMeters, lowerLimbAnthropometric_buttockKneeInMeters}

# Physiological State class attributes and methods
PhysiologicalState_fatigue: Property = Property(name="fatigue", type=IntegerType)
PhysiologicalState_injury: Property = Property(name="injury", type=BooleanType)
PhysiologicalState_temperature: Property = Property(name="temperature", type=FloatType)
PhysiologicalState_bloodPressure: Property = Property(name="bloodPressure", type=IntegerType)
PhysiologicalState_heartbeat: Property = Property(name="heartbeat", type=IntegerType)
PhysiologicalState_perspiration: Property = Property(name="perspiration", type=IntegerType)
PhysiologicalState_pupilsDilation: Property = Property(name="pupilsDilation", type=IntegerType)
PhysiologicalState_nourishment: Property = Property(name="nourishment", type=IntegerType)
PhysiologicalState_respiration: Property = Property(name="respiration", type=IntegerType)
PhysiologicalState_arousal: Property = Property(name="arousal", type=BooleanType)
PhysiologicalState.attributes={PhysiologicalState_fatigue, PhysiologicalState_injury, PhysiologicalState_temperature, PhysiologicalState_bloodPressure, PhysiologicalState_heartbeat, PhysiologicalState_perspiration, PhysiologicalState_pupilsDilation, PhysiologicalState_nourishment, PhysiologicalState_respiration, PhysiologicalState_arousal}

# Attention class attributes and methods
Attention_dividingAttention: Property = Property(name="dividingAttention", type=StringType)
Attention_shiftingAttention: Property = Property(name="shiftingAttention", type=StringType)
Attention_sharingAttention: Property = Property(name="sharingAttention", type=StringType)
Attention_sustainingAttention: Property = Property(name="sustainingAttention", type=StringType)
Attention.attributes={Attention_dividingAttention, Attention_shiftingAttention, Attention_sharingAttention, Attention_sustainingAttention}

# EmotionalIntelligence class attributes and methods
EmotionalIntelligence_socialAwareness: Property = Property(name="socialAwareness", type=StringType)
EmotionalIntelligence_relationshipManagement: Property = Property(name="relationshipManagement", type=StringType)
EmotionalIntelligence_selfManagement: Property = Property(name="selfManagement", type=StringType)
EmotionalIntelligence_selfAwareness: Property = Property(name="selfAwareness", type=StringType)
EmotionalIntelligence.attributes={EmotionalIntelligence_socialAwareness, EmotionalIntelligence_relationshipManagement, EmotionalIntelligence_selfManagement, EmotionalIntelligence_selfAwareness}

# Anthropometric class attributes and methods
Anthropometric_weightInKg: Property = Property(name="weightInKg", type=FloatType)
Anthropometric_headBreadthInMeters: Property = Property(name="headBreadthInMeters", type=FloatType)
Anthropometric_headLengthInMeters: Property = Property(name="headLengthInMeters", type=FloatType)
Anthropometric_bideltoidBreadthInMeters: Property = Property(name="bideltoidBreadthInMeters", type=FloatType)
Anthropometric_statureInMeters: Property = Property(name="statureInMeters", type=FloatType)
Anthropometric_sittingHeightInMeters: Property = Property(name="sittingHeightInMeters", type=FloatType)
Anthropometric_waistCircumferenceInMeters: Property = Property(name="waistCircumferenceInMeters", type=FloatType)
Anthropometric.attributes={Anthropometric_weightInKg, Anthropometric_headBreadthInMeters, Anthropometric_headLengthInMeters, Anthropometric_bideltoidBreadthInMeters, Anthropometric_statureInMeters, Anthropometric_sittingHeightInMeters, Anthropometric_waistCircumferenceInMeters}

# hyperExtension class attributes and methods
hyperExtension_maxValue: Property = Property(name="maxValue", type=IntegerType)
hyperExtension_minValue: Property = Property(name="minValue", type=IntegerType)
hyperExtension.attributes={hyperExtension_maxValue, hyperExtension_minValue}

# shoulder class attributes and methods
shoulder_externalRotation: Property = Property(name="externalRotation", type=IntegerType)
shoulder_internalRotation: Property = Property(name="internalRotation", type=IntegerType)
shoulder.attributes={shoulder_externalRotation, shoulder_internalRotation}

# finger class attributes and methods
finger_extensionB: Property = Property(name="extensionB", type=IntegerType)
finger_flexionC: Property = Property(name="flexionC", type=IntegerType)
finger_abductionA: Property = Property(name="abductionA", type=IntegerType)
finger_adductionB: Property = Property(name="adductionB", type=IntegerType)
finger_hyperExtensionC: Property = Property(name="hyperExtensionC", type=IntegerType)
finger_adductionA: Property = Property(name="adductionA", type=IntegerType)
finger_hyperExtensionB: Property = Property(name="hyperExtensionB", type=IntegerType)
finger_extensionA: Property = Property(name="extensionA", type=IntegerType)
finger_flexionB: Property = Property(name="flexionB", type=IntegerType)
finger_flexionA: Property = Property(name="flexionA", type=IntegerType)
finger_abductionB: Property = Property(name="abductionB", type=IntegerType)
finger_hyperExtensionA: Property = Property(name="hyperExtensionA", type=IntegerType)
finger.attributes={finger_extensionB, finger_flexionC, finger_abductionA, finger_adductionB, finger_hyperExtensionC, finger_adductionA, finger_hyperExtensionB, finger_extensionA, finger_flexionB, finger_flexionA, finger_abductionB, finger_hyperExtensionA}

# thigh class attributes and methods

# wrist class attributes and methods
wrist_urnalDeviation: Property = Property(name="&nbsp;urnalDeviation", type=IntegerType)
wrist_radialDeviation: Property = Property(name="radialDeviation", type=IntegerType)
wrist.attributes={wrist_urnalDeviation, wrist_radialDeviation}

# extension class attributes and methods
extension_minValue: Property = Property(name="minValue", type=IntegerType)
extension_maxValue: Property = Property(name="maxValue", type=IntegerType)
extension.attributes={extension_minValue, extension_maxValue}

# flexion class attributes and methods
flexion_maxValue: Property = Property(name="maxValue", type=IntegerType)
flexion_minValue: Property = Property(name="minValue", type=IntegerType)
flexion.attributes={flexion_maxValue, flexion_minValue}

# Disability class attributes and methods
Disability_description: Property = Property(name="description", type=StringType)
Disability_affects: Property = Property(name="affects", type=AspectsEnum)
Disability_name: Property = Property(name="name", type=StringType)
Disability.attributes={Disability_description, Disability_affects, Disability_name}

# Accessibility class attributes and methods

# toe class attributes and methods

# Hearing class attributes and methods
Hearing_hearingAt2kHz: Property = Property(name="hearingAt2kHz", type=IntegerType)
Hearing_hearingAt1kHz: Property = Property(name="hearingAt1kHz", type=IntegerType)
Hearing_hearingAt500Hz: Property = Property(name="hearingAt500Hz", type=IntegerType)
Hearing_hearingAt8kHz: Property = Property(name="hearingAt8kHz", type=IntegerType)
Hearing_hearingAt250Hz: Property = Property(name="hearingAt250Hz", type=IntegerType)
Hearing_hearingAt4kHz: Property = Property(name="hearingAt4kHz", type=IntegerType)
Hearing.attributes={Hearing_hearingAt2kHz, Hearing_hearingAt1kHz, Hearing_hearingAt500Hz, Hearing_hearingAt8kHz, Hearing_hearingAt250Hz, Hearing_hearingAt4kHz}

# upperLimbAnthropometric class attributes and methods
upperLimbAnthropometric_shoulderElbowLengthInMeters: Property = Property(name="shoulderElbowLengthInMeters", type=FloatType)
upperLimbAnthropometric_bicepsCircumferenceRelaxedInMeters: Property = Property(name="bicepsCircumferenceRelaxedInMeters", type=FloatType)
upperLimbAnthropometric_forarmLengthInMeters: Property = Property(name="forarmLengthInMeters", type=FloatType)
upperLimbAnthropometric_bicepsCircumferenceFlexedInMeters: Property = Property(name="bicepsCircumferenceFlexedInMeters", type=FloatType)
upperLimbAnthropometric.attributes={upperLimbAnthropometric_shoulderElbowLengthInMeters, upperLimbAnthropometric_bicepsCircumferenceRelaxedInMeters, upperLimbAnthropometric_forarmLengthInMeters, upperLimbAnthropometric_bicepsCircumferenceFlexedInMeters}

# knee class attributes and methods
knee_flexionForce: Property = Property(name="flexionForce", type=IntegerType)
knee_extensionForce: Property = Property(name="extensionForce", type=IntegerType)
knee.attributes={knee_flexionForce, knee_extensionForce}

# Sight class attributes and methods
Sight_visualAcuity: Property = Property(name="visualAcuity", type=FloatType)
Sight_contrastSensitivity: Property = Property(name="contrastSensitivity", type=FloatType)
Sight_spectralSensitivity: Property = Property(name="spectralSensitivity", type=FloatType)
Sight_blindSpotCount: Property = Property(name="blindSpotCount", type=IntegerType)
Sight_nearVisualAcuity: Property = Property(name="nearVisualAcuity", type=FloatType)
Sight_glareSensitivity: Property = Property(name="glareSensitivity", type=FloatType)
Sight_blindSpotSize: Property = Property(name="blindSpotSize", type=FloatType)
Sight_blindSpotArea: Property = Property(name="blindSpotArea", type=FloatType)
Sight_blindSpotOpacity: Property = Property(name="blindSpotOpacity", type=StringType)
Sight_distorsion: Property = Property(name="distorsion", type=StringType)
Sight_colorBlindness: Property = Property(name="colorBlindness", type=ColorBlindnessEnum)
Sight.attributes={Sight_visualAcuity, Sight_contrastSensitivity, Sight_spectralSensitivity, Sight_blindSpotCount, Sight_nearVisualAcuity, Sight_glareSensitivity, Sight_blindSpotSize, Sight_blindSpotArea, Sight_blindSpotOpacity, Sight_distorsion, Sight_colorBlindness}

# elbow class attributes and methods

# hand class attributes and methods
hand_pronation: Property = Property(name="pronation", type=IntegerType)
hand_supination: Property = Property(name="supination", type=IntegerType)
hand.attributes={hand_pronation, hand_supination}

# forearm class attributes and methods
forearm_pronation: Property = Property(name="pronation", type=IntegerType)
forearm_supination: Property = Property(name="supination", type=IntegerType)
forearm.attributes={forearm_pronation, forearm_supination}

# Cognitive class attributes and methods
Cognitive_ICTLiteracy: Property = Property(name="ICTLiteracy", type=StringType)
Cognitive_languageReception: Property = Property(name="languageReception", type=StringType)
Cognitive_ICTAnxiousness: Property = Property(name="ICTAnxiousness", type=StringType)
Cognitive_neuroCognitivePerformanceTest: Property = Property(name="neuroCognitivePerformanceTest", type=StringType)
Cognitive_languageProduction: Property = Property(name="languageProduction", type=StringType)
Cognitive_understandingAbstractSigns: Property = Property(name="understandingAbstractSigns", type=StringType)
Cognitive_trailMakingTest: Property = Property(name="trailMakingTest", type=StringType)
Cognitive_physiologicalArousal: Property = Property(name="physiologicalArousal", type=StringType)
Cognitive_valence: Property = Property(name="valence", type=StringType)
Cognitive_visuospatialAbilities: Property = Property(name="visuospatialAbilities", type=StringType)
Cognitive_emotionalIntelligence: Property = Property(name="emotionalIntelligence", type=StringType)
Cognitive_ProcessingSpeed: Property = Property(name="ProcessingSpeed", type=StringType)
Cognitive.attributes={Cognitive_ICTLiteracy, Cognitive_languageReception, Cognitive_ICTAnxiousness, Cognitive_neuroCognitivePerformanceTest, Cognitive_languageProduction, Cognitive_understandingAbstractSigns, Cognitive_trailMakingTest, Cognitive_physiologicalArousal, Cognitive_valence, Cognitive_visuospatialAbilities, Cognitive_emotionalIntelligence, Cognitive_ProcessingSpeed}

# lowerLimb class attributes and methods
lowerLimb_ankleEversion: Property = Property(name="ankleEversion", type=IntegerType)
lowerLimb_ankleDorsiFlexion: Property = Property(name="ankleDorsiFlexion", type=IntegerType)
lowerLimb_anklePlantarFlexion: Property = Property(name="anklePlantarFlexion", type=IntegerType)
lowerLimb.attributes={lowerLimb_ankleEversion, lowerLimb_ankleDorsiFlexion, lowerLimb_anklePlantarFlexion}

# hip class attributes and methods
hip_flexionTorque: Property = Property(name="flexionTorque", type=IntegerType)
hip_internalRotation: Property = Property(name="internalRotation", type=IntegerType)
hip_extensionTorque: Property = Property(name="extensionTorque", type=IntegerType)
hip_abduction: Property = Property(name="abduction", type=IntegerType)
hip_adduction: Property = Property(name="adduction", type=IntegerType)
hip_externalRotation: Property = Property(name="externalRotation", type=IntegerType)
hip.attributes={hip_flexionTorque, hip_internalRotation, hip_extensionTorque, hip_abduction, hip_adduction, hip_externalRotation}

# Phonation class attributes and methods
Phonation_voicePitch: Property = Property(name="voicePitch", type=FloatType)
Phonation_fundamentalFrequency: Property = Property(name="fundamentalFrequency", type=FloatType)
Phonation_syllableDuration: Property = Property(name="syllableDuration", type=FloatType)
Phonation.attributes={Phonation_voicePitch, Phonation_fundamentalFrequency, Phonation_syllableDuration}

# Gait class attributes and methods
Gait_stepLengthInMeters: Property = Property(name="stepLengthInMeters", type=FloatType)
Gait_stepWidthInMeters: Property = Property(name="stepWidthInMeters", type=FloatType)
Gait_stepAssymetry: Property = Property(name="stepAssymetry", type=IntegerType)
Gait_doubleSupport: Property = Property(name="doubleSupport", type=IntegerType)
Gait_footContact: Property = Property(name="footContact", type=IntegerType)
Gait_velocity: Property = Property(name="velocity", type=IntegerType)
Gait_cadence: Property = Property(name="cadence", type=IntegerType)
Gait_weightShift: Property = Property(name="weightShift", type=IntegerType)
Gait_gaitCycle: Property = Property(name="gaitCycle", type=IntegerType)
Gait_strideLengthInMeters: Property = Property(name="strideLengthInMeters", type=FloatType)
Gait.attributes={Gait_stepLengthInMeters, Gait_stepWidthInMeters, Gait_stepAssymetry, Gait_doubleSupport, Gait_footContact, Gait_velocity, Gait_cadence, Gait_weightShift, Gait_gaitCycle, Gait_strideLengthInMeters}

# UpperLimp class attributes and methods
UpperLimp_pushForce: Property = Property(name="pushForce", type=IntegerType)
UpperLimp_elbowTorque: Property = Property(name="elbowTorque", type=IntegerType)
UpperLimp_outForce: Property = Property(name="outForce", type=IntegerType)
UpperLimp_inForce: Property = Property(name="inForce", type=IntegerType)
UpperLimp_pullForce: Property = Property(name="pullForce", type=IntegerType)
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
domain_model = DomainModel(
    name="Generated Model",
    types={Memory, spinalColumn, Neck, Speech, Prosody, Motoric, lowerLimbAnthropometric, PhysiologicalState, Attention, EmotionalIntelligence, Anthropometric, hyperExtension, shoulder, finger, thigh, wrist, extension, flexion, Disability, Accessibility, toe, Hearing, upperLimbAnthropometric, knee, Sight, elbow, hand, forearm, Cognitive, lowerLimb, hip, Phonation, Gait, UpperLimp, Mobility, ColorBlindnessEnum, AspectsEnum},
    associations={shoulder_UpperLimp_non_navigable, Phonation_Speech_non_navigable, flexion_elbow_non_navigable, flexion_knee_non_navigable, UpperLimp_Mobility_non_navigable_1, Accessibility_Sight_association, Accessibility_Anthropometric_association, Cognitive_Attention_association_1, hyperExtension_knee_non_navigable, Accessibility_Memory_association, Accessibility_Motoric_association, wrist_UpperLimp_non_navigable, lowerLimb_Mobility_non_navigable, Accessibility_Hearing_association_2, extension_spinalColumn_non_navigable, flexion_hip_non_navigable, extension_hip_non_navigable, spinalColumn_Mobility_non_navigable, Anthropometric_upperLimbAnthropometric_association_1, Accessibility_Motoric_association_1, Accessibility_Sight_association_2, extension_shoulder_non_navigable, lowerLimb_thigh_association, Accessibility_Sight_association_1, hip_lowerLimb_non_navigable, UpperLimp_Mobility_non_navigable, extension_wrist_non_navigable, knee_wrist_non_navigable, extension_toe_non_navigable, Neck_Mobility_non_navigable, Accessibility_Hearing_association, Accessibility_Hearing_association_1, Accessibility_PhysiologicalState_association, extension_Neck_non_navigable, Accessibility_Speech_association_1, Accessibility_Sight_association_3, Accessibility_Anthropometric_association_1, Prosody_Speech_non_navigable, Gait_Mobility_non_navigable, Anthropometric_upperLimbAnthropometric_association, Accessibility_PhysiologicalState_association_1, elbow_UpperLimp_non_navigable, lowerLimb_thigh_association_1, wrist_lowerLimb_non_navigable, Accessibility_Cognitive_association_1, Cognitive_EmotionalIntelligence_association, hand_UpperLimp_non_navigable, flexion_shoulder_non_navigable, Anthropometric_lowerLimbAnthropometric_association, Accessibility_Disability_association, lowerLimb_Mobility_non_navigable_1, Accessibility_Hearing_association_3, flexion_toe_non_navigable, Accessibility_Mobility_association, Cognitive_EmotionalIntelligence_association_1, forearm_UpperLimp_non_navigable, Accessibility_Cognitive_association, Accessibility_Mobility_association_1, Anthropometric_lowerLimbAnthropometric_association_1, hyperExtension_elbow_non_navigable, Accessibility_Memory_association_1, Accessibility_Disability_association_1, Cognitive_Attention_association, finger_hand_non_navigable, toe_lowerLimb_non_navigable, extension_thigh_non_navigable, Accessibility_Speech_association},
    generalizations={}
)
