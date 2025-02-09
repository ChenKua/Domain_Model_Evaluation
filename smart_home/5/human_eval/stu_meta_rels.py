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
    {
        "dsl": "1 Address associate  1 SmartHome",
        "score": 0.5,
        "counterpart": "1 SmartHome contain 0..1 Address",
    },
    {
        "dsl": "1 SmartHome contain  * Room",
        "score": 1,
        "counterpart": "1 SmartHome contain * Room",
    },
    {
        "dsl": "1 SmartHome contain 1 ActivityLog",
        "score": 0.5,
        "counterpart": "1 SmartHome contain 0..1 ActivityLog",
    },
    {
        "dsl": "1 Room contain  * Device",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1 ActivityLog associate  * SensorReading",
        "score": 0.5,
        "counterpart": "1 ActivityLog contain * SensorReading",
    },
    {
        "dsl": "1 ActivityLog associate  * ControlCommand",
        "score": 0.5,
        "counterpart": "1 ActivityLog contain * ControlCommand",
    },
    {
        "dsl": "* SensorReading associate  1 Sensor",
        "score": 1,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "1 Actuator associate  * ControlCommand",
        "score": 1,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "1 AutomationRule contain 1 PreCondition",
        "score": 0.5,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
    },
    {
        "dsl": "1 AutomationRule contain 1  Action",
        "score": 0.5,
        "counterpart": "1 AlertRule contain * CommandSequence",
    },
    {
        "dsl": "* BooleanRelationalTerm associate  1 PreCondition",
        "score": 0.5,
        "counterpart": "0..1 BinaryExpression associate 1 BooleanExpression",
    },
    {
        "dsl": "0..1 Action associate  * ControlCommand",
        "score": 0.5,
        "counterpart": "1 CommandSequence contain 0..1 ControlCommand",
    },
    {
        "dsl": "Sensor inherit  Device",
        "score": 1,
        "counterpart": "SensorDevice inherit Device",
    },
    {
        "dsl": "Actuator inherit  Device",
        "score": 1,
        "counterpart": "ActuatorDevice inherit Device",
    },
    {"dsl": "1 User contain * AutomationRule", "score": 0, "counterpart": None},
    {
        "dsl": "0..1 AutomationRule associate  * AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "0..1 AutomationRule associate  * AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "* AtomicRelationalTerm associate  1 PreCondition",
        "score": 0,
        "counterpart": None,
    },
]
