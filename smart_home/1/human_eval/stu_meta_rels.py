[
    {
        "dsl": "1 SHAS contain * SmartHome",
        "score": 1,
        "counterpart": "1 SHAS contain * SmartHome",
    },
    {
        "dsl": "1 SHAS contain * User",
        "score": 1,
        "counterpart": "1 SHAS contain * User",
    },
    {"dsl": "1 SHAS contain * ActivityLog", "score": 0, "counterpart": None},
    {"dsl": "1 User contain * AutomationRule", "score": 0, "counterpart": None},
    {
        "dsl": "1 SmartHome contain * Room",
        "score": 1,
        "counterpart": "1 SmartHome contain * Room",
    },
    {
        "dsl": "1 User associate * SmartHome",
        "score": 0.5,
        "counterpart": "* SmartHome associate * User",
    },
    {"dsl": "1 SmartHome contain * Device", "score": 0, "counterpart": None},
    {
        "dsl": "1 ActivityLog contain * SensorReading",
        "score": 1,
        "counterpart": "1 ActivityLog contain * SensorReading",
    },
    {
        "dsl": "1 ActivityLog contain * ControlCommand",
        "score": 1,
        "counterpart": "1 ActivityLog contain * ControlCommand",
    },
    {
        "dsl": "1 Sensor associate * SensorReading",
        "score": 1,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "1 Actuator associate * ControlCommand",
        "score": 1,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "1 AutomationRule contain * Precondition",
        "score": 0.5,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
    },
    {
        "dsl": "1 AutomationRule contain * Action",
        "score": 1,
        "counterpart": "1 AlertRule contain * CommandSequence",
    },
    {
        "dsl": "* ControlCommand associate * Action",
        "score": 0.5,
        "counterpart": "1 CommandSequence contain 0..1 ControlCommand",
    },
    {
        "dsl": "SensorReading inherit Dependency",
        "score": 1,
        "counterpart": "SensorReading inherit RuntimeElement",
    },
    {
        "dsl": "ControlCommand inherit Dependency",
        "score": 1,
        "counterpart": "ControlCommand inherit RuntimeElement",
    },
    {
        "dsl": "1 Precondition contain * BooleanOperator",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "Sensor inherit Device",
        "score": 1,
        "counterpart": "SensorDevice inherit Device",
    },
    {
        "dsl": "Actuator inherit Device",
        "score": 1,
        "counterpart": "ActuatorDevice inherit Device",
    },
    {"dsl": "Device inherit Dependency", "score": 0, "counterpart": None},
    {"dsl": "Room inherit Dependency", "score": 0, "counterpart": None},
    {
        "dsl": "* AtomicRelationalTerm associate 1 Dependency",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "AtomicRelationalTerm inherit RelationalTerm",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "AutomationRule inherit Dependency", "score": 0, "counterpart": None},
    {
        "dsl": "1 ActivityLog contain * TriggeredAutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "1 Precondition inherit * RelationalTerm", "score": 0, "counterpart": None},
    {
        "dsl": "1 AutomationRule associate * TriggeredAutomationRule",
        "score": 0,
        "counterpart": None,
    },
]
