[
    {
        "dsl": "1  SHAS contain  1 SmartHome",
        "score": 0.5,
        "counterpart": "1 SHAS contain * SmartHome",
    },
    {"dsl": "1  SHAS contain  1 ActivityLog", "score": 0, "counterpart": None},
    {
        "dsl": "1  SmartHome associate  * Room",
        "score": 0.5,
        "counterpart": "1 SmartHome contain * Room",
    },
    {
        "dsl": "1  SmartHome associate  * AutomationRule",
        "score": 0.5,
        "counterpart": "1  SmartHome contain  * AlertRule",
    },
    {"dsl": "*  Command associate  1 Room", "score": 0, "counterpart": None},
    {"dsl": "1  ActivityLog associate  * Device", "score": 0, "counterpart": None},
    {
        "dsl": "1  ActivityLog associate  * AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "*  Command associate  1 Controller",
        "score": 1,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "1  AutomationRule associate  1 Precondition",
        "score": 0.5,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
    },
    {
        "dsl": "1  AutomationRule associate  1 Action",
        "score": 0.5,
        "counterpart": "1 AlertRule contain * CommandSequence",
    },
    {
        "dsl": "0..1  AutomationRule associate  0..1 AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1  Precondition associate  * RelationalTerm",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1  Precondition associate  * Operator",
        "score": 0.5,
        "counterpart": "0..1 BinaryExpression associate 1 BooleanExpression",
    },
    {
        "dsl": "1  Action associate  * Command",
        "score": 0.5,
        "counterpart": "1 CommandSequence contain 0..1 ControlCommand",
    },
    {
        "dsl": "Sensor inherit  Device",
        "score": 1,
        "counterpart": "SensorDevice inherit Device",
    },
    {
        "dsl": "Controller inherit  Device",
        "score": 1,
        "counterpart": "ActuatorDevice inherit Device",
    },
    {
        "dsl": "1  SHAS contain  1 InfrastructureMap",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "Room inherit  RelationalTerm", "score": 0, "counterpart": None},
    {
        "dsl": "1  InfrastructureMap associate  * Device",
        "score": 0,
        "counterpart": None,
    },
]
