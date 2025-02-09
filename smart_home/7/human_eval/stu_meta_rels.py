[
    {
        "dsl": "1 SHAS contain  1 SmartHome",
        "score": 0.5,
        "counterpart": "1 SHAS contain * SmartHome",
    },
    {
        "dsl": "1 SmartHome contain  1..* Room",
        "score": 0.5,
        "counterpart": "1 SmartHome contain * Room",
    },
    {"dsl": "1 SHAS contain  1  ActivityLog", "score": 0, "counterpart": None},
    {"dsl": "1 Room associate  * Device", "score": 0, "counterpart": None},
    {
        "dsl": "* SensorReading associate  1 Sensor",
        "score": 1,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "* Actuator associate  *  ControlCommand",
        "score": 0.5,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "1 Precondition associate  1 AutomationRule",
        "score": 0.5,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
    },
    {
        "dsl": "1 Action associate  1 AutomationRule",
        "score": 0.5,
        "counterpart": "1 AlertRule contain * CommandSequence",
    },
    {
        "dsl": "* RelationalTerm associate  * Precondition",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "* BooleanOperator associate  * Precondition",
        "score": 0.5,
        "counterpart": "0..1 BinaryExpression associate 1 BooleanExpression",
    },
    {
        "dsl": "* ControlCommand associate  1 Action",
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
    {"dsl": "1 Owner associate  * AutomationRule", "score": 0, "counterpart": None},
]
