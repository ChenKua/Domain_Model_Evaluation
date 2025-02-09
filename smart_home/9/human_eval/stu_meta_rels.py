[
    {"dsl": "1 Address contain  * User", "score": 0, "counterpart": None},
    {"dsl": "1 SHAS contain 1 Address", "score": 0, "counterpart": None},
    {"dsl": "1 Address contain  * Room", "score": 0, "counterpart": None},
    {
        "dsl": "* Address associate  * InfrastructureMap",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "1 Room  contain * Device", "score": 0, "counterpart": None},
    {"dsl": "* Device associate  1 InfrastructureMap", "score": 0, "counterpart": None},
    {
        "dsl": "* ActivityLog associate  * SensorReading",
        "score": 0.5,
        "counterpart": "1 ActivityLog contain * SensorReading",
    },
    {
        "dsl": "* ActivityLog associate  * ControlCommand",
        "score": 0.5,
        "counterpart": "1 ActivityLog contain * ControlCommand",
    },
    {
        "dsl": "1 Sensor contain  * SensorReading",
        "score": 0.5,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "1 Actuator contain  * ControlCommand",
        "score": 0.5,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "* AutomationRule contain *Action",
        "score": 0.5,
        "counterpart": "1 AlertRule contain * CommandSequence",
    },
    {
        "dsl": "* AutomationRule associate  * SensorReading",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "* Action associate  * ControlCommand",
        "score": 0.5,
        "counterpart": "1 CommandSequence contain 0..1 ControlCommand",
    },
    {
        "dsl": "Sensor inherit  Device",
        "score": 1,
        "counterpart": "SensorDevice inherit Device",
    },
    {
        "dsl": "Actuator inherit  Device",
        "score": 1,
        "counterpart": "ActuatorDevice inherit Device",
    },
    {"dsl": "1 SensorReading associate  1 TimeStamp", "score": 0, "counterpart": None},
    {"dsl": "1 ControlCommand associate  1 TimeStamp", "score": 0, "counterpart": None},
    {"dsl": "* ActivityLog associate  * Address", "score": 0, "counterpart": None},
    {
        "dsl": "* Action associate  * Alert",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "1 Room contain * AutomationRule", "score": 0, "counterpart": None},
]
