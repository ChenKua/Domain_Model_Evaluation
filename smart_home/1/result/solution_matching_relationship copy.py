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
    {"dsl": "1 SmartHome contain 0..1 Address", "score": 0, "counterpart": null},
    {
        "dsl": "1 SmartHome contain * Room",
        "score": 1,
        "counterpart": "1 SmartHome contain * Room",
    },
    {"dsl": "1 SmartHome contain 0..1 ActivityLog", "score": 0, "counterpart": null},
    {
        "dsl": "* SmartHome associate * User",
        "score": 0.5,
        "counterpart": "1 User associate * SmartHome",
    },
    {"dsl": "1 Room contain * SensorDevice", "score": 0, "counterpart": null},
    {"dsl": "1 Room contain * ActuatorDevice", "score": 0, "counterpart": null},
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
        "dsl": "* SensorReading associate 1 SensorDevice",
        "score": 1,
        "counterpart": "1 Sensor associate * SensorReading",
    },
    {
        "dsl": "* ControlCommand associate 1 ActuatorDevice",
        "score": 1,
        "counterpart": "1 Actuator associate * ControlCommand",
    },
    {
        "dsl": "1 AlertRule contain 0..1 BooleanExpression",
        "score": 0,
        "counterpart": null,
    },
    {"dsl": "1 AlertRule contain * CommandSequence", "score": 0, "counterpart": null},
    {"dsl": "* RelationalTerm associate 0..1  Room", "score": 0, "counterpart": null},
    {"dsl": "* RelationalTerm associate 0..1  Device", "score": 0, "counterpart": null},
    {
        "dsl": "* RelationalTerm associate 0..1  RuntimeElement",
        "score": 0,
        "counterpart": null,
    },
    {
        "dsl": "* RelationalTerm associate 0..1  ControlCommand",
        "score": 0,
        "counterpart": null,
    },
    {
        "dsl": "0..1 NotExpression associate 1 BooleanExpression",
        "score": 0.5,
        "counterpart": "1 Precondition contain * BooleanOperator",
    },
    {
        "dsl": "0..1 BinaryExpression associate 1 BooleanExpression",
        "score": 0,
        "counterpart": null,
    },
    {
        "dsl": "0..1 BinaryExpression associate 1 BooleanExpression",
        "score": 0,
        "counterpart": null,
    },
    {
        "dsl": "* CommandSequence associate 0..1 CommandSequence",
        "score": 0,
        "counterpart": null,
    },
    {
        "dsl": "1 CommandSequence contain 0..1 ControlCommand",
        "score": 0.5,
        "counterpart": "* ControlCommand associate * Action",
    },
    {
        "dsl": "SensorReading inherit RuntimeElement",
        "score": 1,
        "counterpart": "SensorReading inherit Dependency",
    },
    {
        "dsl": "ControlCommand inherit RuntimeElement",
        "score": 1,
        "counterpart": "ControlCommand inherit Dependency",
    },
    {"dsl": "NotExpression inherit BooleanExpression", "score": 0, "counterpart": null},
    {
        "dsl": "BinaryExpression inherit BooleanExpression",
        "score": 0,
        "counterpart": null,
    },
    {
        "dsl": "RelationalTerm inherit BooleanExpression",
        "score": 0,
        "counterpart": null,
    },
    {
        "dsl": "SensorDevice inherit Device",
        "score": 1,
        "counterpart": "Sensor inherit Device",
    },
    {
        "dsl": "ActuatorDevice inherit Device",
        "score": 1,
        "counterpart": "Actuator inherit Device",
    },
]
