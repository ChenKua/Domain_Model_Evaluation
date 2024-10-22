[
    {
        "dsl": "1 SHASystem contain  * SmartHome",
        "score": 1,
        "counterpart": "1 SHAS contain * SmartHome",
    },
    {
        "dsl": "1 SHASystem contain  * User",
        "score": 1,
        "counterpart": "1 SHAS contain * User",
    },
    {"dsl": "1 SHASystem contain  * ActivityLog", "score": 0, "counterpart": None},
    {"dsl": "1 SHASystem contain  * AutomationRule", "score": 0, "counterpart": None},
    {"dsl": "1 SHASystem contain  * Alert", "score": 0, "counterpart": None},
    {
        "dsl": "1 SmartHome contain  * Room",
        "score": 1,
        "counterpart": "1 SmartHome contain * Room",
    },
    {
        "dsl": "1 User associate  1 SmartHome",
        "score": 0.5,
        "counterpart": "* SmartHome associate * User",
    },
    {
        "dsl": "1 SmartHome associate  * AutomationRule",
        "score": 0.5,
        "counterpart": "1  SmartHome contain  * AlertRule",
    },
    {"dsl": "1 Room contain  * Device", "score": 0, "counterpart": None},
    {"dsl": "*  Room associate  * Precondition", "score": 0, "counterpart": None},
    {"dsl": "* Device associate  1 ActivityLog", "score": 0, "counterpart": None},
    {
        "dsl": "1 SensorDevice contain  * SensorReading",
        "score": 0.5,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "1 ActuatorDevice contain  * ControlCommand",
        "score": 0.5,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "1  AutomationRule contain  1 Precondition",
        "score": 0.5,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
    },
    {
        "dsl": "1 AutomationRule contain  1 Action",
        "score": 0.5,
        "counterpart": "1 AlertRule contain * CommandSequence",
    },
    {
        "dsl": "*  AutomationRule associate  * AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1 Precondition contain  * BooleanOperator",
        "score": 0.5,
        "counterpart": "0..1 BinaryExpression associate 1 BooleanExpression",
    },
    {
        "dsl": "* ControlCommand associate  * Action",
        "score": 0.5,
        "counterpart": "1 CommandSequence contain 0..1 ControlCommand",
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
    {"dsl": "* Alert associate * AutomationRule", "score": 0, "counterpart": None},
]
