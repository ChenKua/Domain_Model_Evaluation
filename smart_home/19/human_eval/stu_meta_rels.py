[
    {
        "dsl": "1  SmartHomeApplicationSystem contain  * SmartHome",
        "score": 1,
        "counterpart": "1 SHAS contain * SmartHome",
    },
    {
        "dsl": "1  SmartHomeApplicationSystem contain  * User",
        "score": 1,
        "counterpart": "1 SHAS contain * User",
    },
    {
        "dsl": "1 SmartHome associate  1 Address",
        "score": 0.5,
        "counterpart": "1 SmartHome contain 0..1 Address",
    },
    {
        "dsl": "1 SmartHome contain  1..* Room",
        "score": 0.5,
        "counterpart": "1 SmartHome contain * Room",
    },
    {"dsl": "1 Room contain  * Device", "score": 0, "counterpart": None},
    {
        "dsl": "1  ActivityLog contain  * SensorReading",
        "score": 1,
        "counterpart": "1 ActivityLog contain * SensorReading",
    },
    {
        "dsl": "1  ActivityLog contain  * ControlCommand",
        "score": 1,
        "counterpart": "1 ActivityLog contain * ControlCommand",
    },
    {
        "dsl": "1 SensorDevice associate  * SensorReading",
        "score": 1,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "1 ActuatorDevice associate  * ControlCommand",
        "score": 1,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "1 AutomationRule contain  1 PreCondition",
        "score": 0.5,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
    },
    {"dsl": "1 AutomationRule contain  1 Action", "score": 0.5, "counterpart": "1 AlertRule contain * CommandSequence"},
    {
        "dsl": "* RelationalTerm associate 0..1 Room",
        "score": 1,
        "counterpart": "* RelationalTerm associate 0..1  Room",
    },
    {
        "dsl": "1  PreCondition contain  * BooleanOperator",
        "score": 0.5,
        "counterpart": "0..1 BinaryExpression associate 1 BooleanExpression",
    },
    {
        "dsl": "SensorDevice inherit  Device",
        "score": 1,
        "counterpart": "SensorDevice inherit Device",
    },
    {
        "dsl": "ActuatorDevice inherit  Device",
        "score": 1,
        "counterpart": "ActuatorDevice inherit Device",
    },
    {
        "dsl": "1  SmartHomeApplicationSystem contain  1 ActivityLog",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1  SmartHomeApplicationSystem contain  * PredefinedCommand",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1  SmartHomeApplicationSystem contain  * AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "* PredefinedCommand associate  0..1 Room",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1 PredefinedCommand associate  * ControlCommand",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "0..1  Action associate  * PredefinedCommand",
        "score": 0,
        "counterpart": None,
    },
]
