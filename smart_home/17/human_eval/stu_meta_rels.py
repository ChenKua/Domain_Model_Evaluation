[
    {
        "dsl": "1 SHAS contain * SmartHome",
        "score": 1,
        "counterpart": "1 SHAS contain * SmartHome",
    },
    {
        "dsl": "1 SHAS contain * Owner",
        "score": 1,
        "counterpart": "1 SHAS contain * User",
    },
    {
        "dsl": "1..*  SmartHome associate  1..* Owner",
        "score": 0.5,
        "counterpart": "* SmartHome associate * User",
    },
    {"dsl": "1 SHAS contain * ActivityLog", "score": 0, "counterpart": None},
    {"dsl": "1 SHAS contain * InfrastructureMap", "score": 0, "counterpart": None},
    {"dsl": "1 SHAS contain * RelevantAlert", "score": 0, "counterpart": None},
    {"dsl": "*  RelevantAlert associate  * Owner", "score": 0, "counterpart": None},
    {
        "dsl": "1 SmartHome contain * Room",
        "score": 1,
        "counterpart": "1 SmartHome contain * Room",
    },
    {"dsl": "1 Room contain * Device", "score": 0, "counterpart": None},
    {
        "dsl": "*  Device associate  0..1 InfrastructureMap",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "*  SensorReading associate  0..1 ActivityLog",
        "score": 0.5,
        "counterpart": "1 ActivityLog contain * SensorReading",
    },
    {
        "dsl": "*  ControlCommand associate  0..1 ActivityLog",
        "score": 0.5,
        "counterpart": "1 ActivityLog contain * ControlCommand",
    },
    {
        "dsl": "1 Sensor contain * SensorReading",
        "score": 0.5,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "1 Actuator contain * ControlCommand",
        "score": 0.5,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "1 AutomationRule contain 1 PreCondition",
        "score": 0.5,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
    },
    {
        "dsl": "1 AutomationRule contain 1 Action",
        "score": 0.5,
        "counterpart": "1 AlertRule contain * CommandSequence",
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
    {
        "dsl": "1 RelevantAlert contain * AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "0..1 AutomationRule associate  * AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "*  AutomationRule associate  0..1 ActivityLog",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "*  PreCondition associate  * Room", "score": 0, "counterpart": None},
    {
        "dsl": "0..1  PreCondition associate  * PreCondition",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "0..1  Action associate  * Room", "score": 0, "counterpart": None},
]
