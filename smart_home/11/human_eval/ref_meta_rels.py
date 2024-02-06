[
    {"dsl": "1 SHAS contain * SmartHome", "score": 0, "counterpart": None},
    {"dsl": "1 SHAS contain * User", "score": 0, "counterpart": None},
    {"dsl": "1 SmartHome contain 0..1 Address", "score": 0, "counterpart": None},
    {
        "dsl": "1 SmartHome contain * Room",
        "score": 1,
        "counterpart": "1  SmartHome contain  * Room",
    },
    {
        "dsl": "1 SmartHome contain 0..1 ActivityLog",
        "score": 0.5,
        "counterpart": "1  SmartHome contain  * Activity",
    },
    {"dsl": "* SmartHome associate * User", "score": 0, "counterpart": None},
    {
        "dsl": "1  SmartHome contain  * AlertRule",
        "score": 1,
        "counterpart": "1  SmartHome contain  * Rule",
    },
    {"dsl": "1 Room contain * SensorDevice", "score": 0, "counterpart": None},
    {"dsl": "1 Room contain * ActuatorDevice", "score": 0, "counterpart": None},
    {"dsl": "1 ActivityLog contain * SensorReading", "score": 0, "counterpart": None},
    {"dsl": "1 ActivityLog contain * ControlCommand", "score": 0, "counterpart": None},
    {
        "dsl": "* SensorReading associate 1 SensorDevice",
        "score": 1,
        "counterpart": "*  Reading associate  1 Sensor",
    },
    {
        "dsl": "* ControlCommand associate 1 ActuatorDevice",
        "score": 1,
        "counterpart": "*  Command associate  1 Actuator",
    },
    {
        "dsl": "1 AlertRule contain 0..1 BooleanExpression",
        "score": 0.5,
        "counterpart": "1  Rule contain  1..* RuleElement",
    },
    {
        "dsl": "1 AlertRule contain * CommandSequence",
        "score": 0.5,
        "counterpart": "1  Rule contain  1..* Action",
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
        "score": 0,
        "counterpart": None,
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
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "SensorReading inherit RuntimeElement", "score": 0, "counterpart": None},
    {"dsl": "ControlCommand inherit RuntimeElement", "score": 0, "counterpart": None},
    {"dsl": "NotExpression inherit BooleanExpression", "score": 0, "counterpart": None},
    {
        "dsl": "BinaryExpression inherit BooleanExpression",
        "score": 1,
        "counterpart": "BooleanOperator inherit  RuleElement",
    },
    {
        "dsl": "RelationalTerm inherit BooleanExpression",
        "score": 1,
        "counterpart": "RelationalTerm inherit  RuleElement",
    },
    {
        "dsl": "SensorDevice inherit Device",
        "score": 1,
        "counterpart": "Sensor inherit  RoomElement",
    },
    {
        "dsl": "ActuatorDevice inherit Device",
        "score": 1,
        "counterpart": "Actuator inherit  RoomElement",
    },
]
