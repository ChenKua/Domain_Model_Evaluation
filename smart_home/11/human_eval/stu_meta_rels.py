[
    {
        "dsl": "1  SmartHome contain  * Room",
        "score": 1,
        "counterpart": "1 SmartHome contain * Room",
    },
    {
        "dsl": "1  SmartHome contain  * Activity",
        "score": 0.5,
        "counterpart": "1 SmartHome contain 0..1 ActivityLog",
    },
    {
        "dsl": "1  SmartHome contain  * Rule",
        "score": 1,
        "counterpart": "1  SmartHome contain  * AlertRule",
    },
    {
        "dsl": "*  Reading associate  1 Sensor",
        "score": 1,
        "counterpart": "1 SmartHome contain * Room",
    },
    {
        "dsl": "*  Command associate  1 Actuator",
        "score": 1,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {"dsl": "*  Action associate  1 Actuator", "score": 0, "counterpart": None},
    {
        "dsl": "1  Rule contain  1..* RuleElement",
        "score": 0.5,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
    },
    {
        "dsl": "1  Rule contain  1..* Action",
        "score": 0.5,
        "counterpart": "1 AlertRule contain * CommandSequence",
    },
    {
        "dsl": "BooleanOperator inherit  RuleElement",
        "score": 1,
        "counterpart": "BinaryExpression inherit BooleanExpression",
    },
    {
        "dsl": "RelationalTerm inherit  RuleElement",
        "score": 1,
        "counterpart": "RelationalTerm inherit BooleanExpression",
    },
    {
        "dsl": "Sensor inherit  RoomElement",
        "score": 1,
        "counterpart": "SensorDevice inherit Device",
    },
    {
        "dsl": "Actuator inherit  RoomElement",
        "score": 1,
        "counterpart": "ActuatorDevice inherit Device",
    },
    {"dsl": "Command inherit  Activity", "score": 0, "counterpart": None},
    {"dsl": "Reading inherit  Activity", "score": 0, "counterpart": None},
    {"dsl": "RuleTrigger inherit  Activity", "score": 0, "counterpart": None},
    {"dsl": "*  RuleTrigger associate  1 Rule", "score": 0, "counterpart": None},
    {"dsl": "SensorCheck inherit  RelationalTerm", "score": 0, "counterpart": None},
    {
        "dsl": "*  SensorCheck associate  1 Sensor",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "ActiveCheck inherit  RelationalTerm", "score": 0, "counterpart": None},
    {"dsl": "*  ActiveCheck associate  1 RoomElement", "score": 0, "counterpart": None},
]
