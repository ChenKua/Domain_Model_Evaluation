[
    {"dsl": "1  SHAS contain  1 SmartHome", "score": 0, "counterpart": None},
    {
        "dsl": "1  SHAS contain  * User",
        "score": 1,
        "counterpart": "1 SHAS contain * User",
    },
    {"dsl": "1  SHAS contain  1 ActivityLog", "score": 0, "counterpart": None},
    {
        "dsl": "1  SHAS contain  1 AutomationRecord",
        "score": 0.5,
        "counterpart": "1 SHAS contain * SmartHome",
    },
    {"dsl": "1  SHAS contain  1 InfrastructureMap", "score": 0, "counterpart": None},
    {"dsl": "1  SmartHome contain  * Room", "score": 0, "counterpart": None},
    {"dsl": "1  SmartHome contain  * RelevantAlert", "score": 0, "counterpart": None},
    {"dsl": "1  Room contain  * Device", "score": 0, "counterpart": None},
    {"dsl": "0..1Device associate  1 DeviceType", "score": 0, "counterpart": None},
    {
        "dsl": "1  Sensor associate  * SensorReading",
        "score": 1,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "1  Actuator associate  * ControlCommand",
        "score": 1,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "0..1  AutomationRule contain  1 Precondition",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "0..1  AutomationRule contain  1 Action", "score": 0, "counterpart": None},
    {
        "dsl": "0..1  AutomationRule associate  * AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "0..1  AutomationRule associate  * AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "0..1  Action associate  * ControlCommand",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "SensorReading inherit  DeviceActivity",
        "score": 1,
        "counterpart": "SensorReading inherit RuntimeElement",
    },
    {
        "dsl": "ControlCommand inherit  DeviceActivity",
        "score": 1,
        "counterpart": "ControlCommand inherit RuntimeElement",
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
    {"dsl": "1  User contain  * AutomationRule", "score": 0, "counterpart": None},
    {"dsl": "0..1  User associate  * RelevantAlert", "score": 0, "counterpart": None},
    {
        "dsl": "0..1  InfrastructureMap associate  * Device",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1  ActivityLog contain  * DeviceActivity",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "0..1  AutomationRecord associate  * AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "0..1  ControlCommand associate  1 CommandContent",
        "score": 0.5,
        "counterpart": "1 CommandSequence contain 0..1 ControlCommand",
    },
    {"dsl": "0..1  Precondition associate  * Room", "score": 0, "counterpart": None},
    {"dsl": "0..1  Precondition associate  * Device", "score": 0, "counterpart": None},
    {
        "dsl": "0..1  Precondition associate  * SensorReading",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "0..1  Precondition associate  * ControlCommand",
        "score": 0,
        "counterpart": None,
    },
]
