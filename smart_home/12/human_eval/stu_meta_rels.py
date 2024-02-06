[
    {
        "dsl": "1  SHAS associate  * SmartHome",
        "score": 0.5,
        "counterpart": "1 SHAS contain * SmartHome",
    },
    {"dsl": "1  SHAS contain  * Device", "score": 0, "counterpart": None},
    {"dsl": "1  SHAS contain  * SensorReading", "score": 0, "counterpart": None},
    {"dsl": "1  SHAS contain  * ControlCommand", "score": 0, "counterpart": None},
    {"dsl": "1  SHAS contain  * AutomationRule", "score": 0, "counterpart": None},
    {
        "dsl": "1  SmartHome contain  * Room",
        "score": 1,
        "counterpart": "1 SmartHome contain * Room",
    },
    {
        "dsl": "1  SmartHome contain  * Alert",
        "score": 1,
        "counterpart": "1  SmartHome contain  * AlertRule",
    },
    {"dsl": "1  Room associate  * Device", "score": 0, "counterpart": None},
    {
        "dsl": "*  AutomationRule associate  * SensorReading",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "*  SensorReading associate  1 SensorDevice",
        "score": 1,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "*  ControlCommand associate  1 ActuatorDevice",
        "score": 1,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "*  AutomationRule associate  * ControlCommand",
        "score": 0.5,
        "counterpart": "1 AlertRule contain * CommandSequence",
    },
    {
        "dsl": "*  AutomationRule associate  * SensorDevice",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "*  AutomationRule associate  * ActuatorDevice",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "*  AutomationRule associate  * Room", "score": 0, "counterpart": None},
    {"dsl": "*  AutomationRule associate  * Alert", "score": 0, "counterpart": None},
    {
        "dsl": "*  AutomationRule associate  * AutomationRule",
        "score": 0,
        "counterpart": None,
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
]
