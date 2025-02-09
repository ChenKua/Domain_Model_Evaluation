[
    {
        "dsl": "1  SmartHome contain  1 Address",
        "score": 0.5,
        "counterpart": "1 SmartHome contain 0..1 Address",
    },
    {
        "dsl": "1  SmartHome contain  * SmartRoom",
        "score": 1,
        "counterpart": "1 SmartHome contain * Room",
    },
    {
        "dsl": "1  SmartHome contain  1 ActivityLog",
        "score": 0.5,
        "counterpart": "1 SmartHome contain 0..1 ActivityLog",
    },
    {
        "dsl": "1  SmartHome contain  * AutomationRule",
        "score": 1,
        "counterpart": "1  SmartHome contain  * AlertRule",
    },
    {"dsl": "1  SmartRoom associate  * Device", "score": 0, "counterpart": None},
    {
        "dsl": "1  ActivityLog associate  * SensorReading",
        "score": 0.5,
        "counterpart": "1 ActivityLog contain * SensorReading",
    },
    {
        "dsl": "1  ActivityLog associate  * ControlCommand",
        "score": 0.5,
        "counterpart": "1 ActivityLog contain * ControlCommand",
    },
    {
        "dsl": "1  SensorDevice associate  * SensorReading",
        "score": 1,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "1  ActuatorDevice associate  * ControlCommand",
        "score": 1,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "*  AutomationRule associate  1 AutomationPrecondition",
        "score": 0.5,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
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
    {"dsl": "*  Device associate  1 DeviceType", "score": 0, "counterpart": None},
    {
        "dsl": "1  SensorReading associate  1 MeasuredValue measuredValue",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1  ActivityLog associate  * AutomationTrigger",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "*  AutomationRule associate  1..* ActuatorDevice",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "*  AutomationRule associate  0..1 AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "*  AutomationTrigger associate  1 AutomationRule",
        "score": 0.5,
        "counterpart": "1 AlertRule contain * CommandSequence",
    },
]
