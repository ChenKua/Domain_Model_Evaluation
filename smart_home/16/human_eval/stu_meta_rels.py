[
    {"dsl": "*  SHAS contain  1 Device", "score": 0, "counterpart": None},
    {"dsl": "1..*  SHAS  contain  1 Room", "score": 0, "counterpart": None},
    {
        "dsl": "*  SHAS  contain  1 AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "*  SHAS  contain  1 HistoryRuleTriggered",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "*  SHAS  contain  1 DeviceActivity", "score": 0, "counterpart": None},
    {"dsl": "1  Room  associate  * Device", "score": 0, "counterpart": None},
    {
        "dsl": "*  Sensor  contain  1 SensorReading",
        "score": 0.5,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "*  ControlCommand  associate  1 Actuator",
        "score": 1,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "1  AutomationRule  contain  1 Precondition",
        "score": 0.5,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
    },
    {
        "dsl": "1  AutomationRule  contain  1 Action",
        "score": 0.5,
        "counterpart": "1 AlertRule contain * CommandSequence",
    },
    {
        "dsl": "*  AutomationRule  associate  * AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "*  AutomationRule  associate  * AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "*  HistoryRuleTriggered  associate  1 AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "*  Action  associate  1..* ControlCommand",
        "score": 0.5,
        "counterpart": "1 CommandSequence contain 0..1 ControlCommand",
    },
    {
        "dsl": "SensorReading  inherit  DeviceActivity",
        "score": 1,
        "counterpart": "SensorReading inherit RuntimeElement",
    },
    {
        "dsl": "ControlCommand  inherit  DeviceActivity",
        "score": 1,
        "counterpart": "ControlCommand inherit RuntimeElement",
    },
    {
        "dsl": "Sensor  inherit  Device",
        "score": 1,
        "counterpart": "SensorDevice inherit Device",
    },
    {
        "dsl": "Actuator  inherit  Device",
        "score": 1,
        "counterpart": "ActuatorDevice inherit Device",
    },
    {
        "dsl": "*  Precondition  associate  * SensorReading",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "*  Precondition  associate  * Room", "score": 0, "counterpart": None},
    {"dsl": "*  Precondition  associate  * Device", "score": 0, "counterpart": None},
    {
        "dsl": "*  Precondition  associate  * ControlCommand",
        "score": 0,
        "counterpart": None,
    },
]
