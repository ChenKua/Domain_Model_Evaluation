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
        "dsl": "1 SmartHome contain 0..1 Address",
        "score": 0.5,
        "counterpart": "1 Address associate  1 SmartHome",
    },
    {
        "dsl": "1 SmartHome contain * Room",
        "score": 1,
        "counterpart": "1 SmartHome contain  * Room",
    },
    {
        "dsl": "1 SmartHome contain 0..1 ActivityLog",
        "score": 0.5,
        "counterpart": "1 SmartHome contain 1 ActivityLog",
    },
    {"dsl": "* SmartHome associate * User", "score": 0, "counterpart": None},
    {"dsl": "1  SmartHome contain  * AlertRule", "score": 0, "counterpart": None},
    {
        "dsl": "1 Room contain * SensorDevice",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1 Room contain * ActuatorDevice",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1 ActivityLog contain * SensorReading",
        "score": 0.5,
        "counterpart": "1 ActivityLog associate  * SensorReading",
    },
    {
        "dsl": "1 ActivityLog contain * ControlCommand",
        "score": 0.5,
        "counterpart": "1 ActivityLog associate  * ControlCommand",
    },
    {
        "dsl": "* SensorReading associate 1 SensorDevice",
        "score": 1,
        "counterpart": "* SensorReading associate  1 Sensor",
    },
    {
        "dsl": "* ControlCommand associate 1 ActuatorDevice",
        "score": 1,
        "counterpart": "1 Actuator associate  * ControlCommand",
    },
    {
        "dsl": "1 AlertRule contain 0..1 BooleanExpression",
        "score": 0.5,
        "counterpart": "1 AutomationRule contain 1 PreCondition",
    },
    {
        "dsl": "1 AlertRule contain * CommandSequence",
        "score": 0.5,
        "counterpart": "1 AutomationRule contain 1  Action",
    },
    {"dsl": "* RelationalTerm associate 0..1  Room", "score": 0, "counterpart": None},
    {
        "dsl": "* RelationalTerm associate 0..1  SensorDevice",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "* RelationalTerm associate 0..1  ActuatorDevice",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "* RelationalTerm associate 0..1  SensorReading",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "* RelationalTerm associate 0..1  ControlCommand",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "0..1 NotExpression associate 1 BooleanExpression",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "0..1 BinaryExpression associate 1 BooleanExpression",
        "score": 0.5,
        "counterpart": "* BooleanRelationalTerm associate  1 PreCondition",
    },
    {
        "dsl": "0..1 BinaryExpression associate 1 BooleanExpression",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "* CommandSequence associate 0..1 CommandSequence",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1 CommandSequence contain 0..1 ControlCommand",
        "score": 0.5,
        "counterpart": "0..1 Action associate  * ControlCommand",
    },
    {"dsl": "SensorReading inherit RuntimeElement", "score": 0, "counterpart": None},
    {"dsl": "ControlCommand inherit RuntimeElement", "score": 0, "counterpart": None},
    {"dsl": "NotExpression inherit BooleanExpression", "score": 0, "counterpart": None},
    {
        "dsl": "BinaryExpression inherit BooleanExpression",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "RelationalTerm inherit BooleanExpression",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "SensorDevice inherit Device",
        "score": 1,
        "counterpart": "Sensor inherit  Device",
    },
    {
        "dsl": "ActuatorDevice inherit Device",
        "score": 1,
        "counterpart": "Actuator inherit  Device",
    },
]
