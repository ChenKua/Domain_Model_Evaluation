[
    {
        "dsl": "1 SHAS contain * SmartHome",
        "score": 1,
        "counterpart": "1  SmartHomeApplicationSystem contain  * SmartHome",
    },
    {
        "dsl": "1 SHAS contain * User",
        "score": 1,
        "counterpart": "1  SmartHomeApplicationSystem contain  * User",
    },
    {
        "dsl": "1 SmartHome contain 0..1 Address",
        "score": 0.5,
        "counterpart": "1 SmartHome associate  1 Address",
    },
    {
        "dsl": "1 SmartHome contain * Room",
        "score": 0.5,
        "counterpart": "1 SmartHome contain  1..* Room",
    },
    {"dsl": "1 SmartHome contain 0..1 ActivityLog", "score": 0, "counterpart": None},
    {"dsl": "* SmartHome associate * User", "score": 0, "counterpart": None},
    {"dsl": "1  SmartHome contain  * AlertRule", "score": 0, "counterpart": None},
    {"dsl": "1 Room contain * SensorDevice", "score": 0, "counterpart": None},
    {"dsl": "1 Room contain * ActuatorDevice", "score": 0, "counterpart": None},
    {
        "dsl": "1 ActivityLog contain * SensorReading",
        "score": 1,
        "counterpart": "1  ActivityLog contain  * SensorReading",
    },
    {
        "dsl": "1 ActivityLog contain * ControlCommand",
        "score": 1,
        "counterpart": "1  ActivityLog contain  * ControlCommand",
    },
    {
        "dsl": "* SensorReading associate 1 SensorDevice",
        "score": 1,
        "counterpart": "1 SensorDevice associate  * SensorReading",
    },
    {
        "dsl": "* ControlCommand associate 1 ActuatorDevice",
        "score": 1,
        "counterpart": "1 ActuatorDevice associate  * ControlCommand",
    },
    {
        "dsl": "1 AlertRule contain 0..1 BooleanExpression",
        "score": 0.5,
        "counterpart": "1 AutomationRule contain  1 PreCondition",
    },
    {"dsl": "1 AlertRule contain * CommandSequence", "score": 0.5, "counterpart": "1 AutomationRule contain  1 Action"},
    {
        "dsl": "* RelationalTerm associate 0..1  Room",
        "score": 1,
        "counterpart": "* RelationalTerm associate 0..1 Room",
    },
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
        "score": 0.5,
        "counterpart": "1  PreCondition contain  * BooleanOperator",
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
        "counterpart": "SensorDevice inherit  Device",
    },
    {
        "dsl": "ActuatorDevice inherit Device",
        "score": 1,
        "counterpart": "ActuatorDevice inherit  Device",
    },
]
