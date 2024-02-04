[
    {
        "dsl": "1 SHAS contain * User",
        "score": 1,
        "counterpart": "1 SHAS contain * User",
    },
    {
        "dsl": "1 SmartHome contain 1 Address",
        "score": 0.5,
        "counterpart": "1 SmartHome contain 0..1 Address",
    },
    {
        "dsl": "1 SmartHome contain * Room",
        "score": 1,
        "counterpart": "1 SmartHome contain * Room",
    },
    {
        "dsl": "1 SmartHome contain 1 ActivityLog",
        "score": 0.5,
        "counterpart": "1 SmartHome contain 0..1 ActivityLog",
    },
    {
        "dsl": "1 Room contain * Device",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1 ActivityLog associate * SensorReading",
        "score": 0.5,
        "counterpart": "1 ActivityLog contain * SensorReading",
    },
    {
        "dsl": "1 ActivityLog associate * ControlCommand",
        "score": 0.5,
        "counterpart": "1 ActivityLog contain * ControlCommand",
    },
    {
        "dsl": "1 Sensor associate 1 SensorReading",
        "score": 0.5,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "1..* Actuator  associate 1 ControlCommand",
        "score": 0.5,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "1 AutomationRule contain 1 Precondition",
        "score": 0,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
    },
    {
        "dsl": "1 AutomationRule contain 1 Action",
        "score": 0,
        "counterpart": "1 AlertRule contain * CommandSequence",
    },
    {
        "dsl": "1 Action contain 1..* ControlCommand",
        "score": 0.5,
        "counterpart": "1 CommandSequence contain 0..1 ControlCommand",
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
    {"dsl": "1 User contain 0..1 Owner", "score": 0, "counterpart": None},
    {"dsl": "1 Owner contain * SmartHome", "score": 0, "counterpart": None},
    {"dsl": "1 SmartHome contain * SensorReading", "score": 0, "counterpart": None},
    {"dsl": "1 SmartHome contain * AutomationRule", "score": 0, "counterpart": None},
    {
        "dsl": "1 AutomationRule contain * AutomationRuleLog",
        "score": 0,
        "counterpart": None,
    },
]
