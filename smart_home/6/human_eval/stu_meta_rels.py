[
    {
        "dsl": "1 SHAS contain  * User",
        "score": 1,
        "counterpart": "1 SHAS contain * User",
    },
    {"dsl": "1 SHAS contain  1..* Room", "score": 0, "counterpart": None},
    {"dsl": "1 SHAS contain  1 ActivityLog", "score": 0, "counterpart": None},
    {"dsl": "1 User contain  * AutomationRule", "score": 0, "counterpart": None},
    {"dsl": "1 Room contain  * Device", "score": 0, "counterpart": None},
    {
        "dsl": "1 Sensor associate  * SensorReading",
        "score": 1,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "1 Actuator associate * ControlCommand",
        "score": 1,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "1 AutomationRule contain  1 Precondition",
        "score": 0.5,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
    },
    {
        "dsl": "1 AutomationRule contain  1 Action",
        "score": 0.5,
        "counterpart": "1 AlertRule contain * CommandSequence",
    },
    {
        "dsl": "0..1 AutomationRule associate  0..1 AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1 Precondition contain  1..* RelationalTerm",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1 Precondition contain  * BooleanOperator",
        "score": 0.5,
        "counterpart": "0..1 BinaryExpression associate 1 BooleanExpression",
    },
    {
        "dsl": "1 ControlCommand associate  0..1 Action",
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
    {"dsl": "0..1 Precondition associate  1 Sensor", "score": 0, "counterpart": None},
]
