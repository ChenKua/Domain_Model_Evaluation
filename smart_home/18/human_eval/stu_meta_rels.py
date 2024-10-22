[
    {
        "dsl": "1  SHAS  contain  * User",
        "score": 1,
        "counterpart": "1 SHAS contain * User",
    },
    {
        "dsl": "1  ActivityLog contain  * SensorReading",
        "score": 1,
        "counterpart": "1 ActivityLog contain * SensorReading",
    },
    {"dsl": "1  ActivityLog associate  * Device", "score": 0, "counterpart": None},
    {
        "dsl": "1  ActivityLog contain  * ControlCommand",
        "score": 1,
        "counterpart": "1 ActivityLog contain * ControlCommand",
    },
    {
        "dsl": "1  AutomationRule contain  1 PreCondition",
        "score": 0.5,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
    },
    {
        "dsl": "1  AutomationRule contain  1 Action",
        "score": 0.5,
        "counterpart": "1 AlertRule contain * CommandSequence",
    },
    {
        "dsl": "0..1  Action associate  * ControlCommand",
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
    {"dsl": "1  SHAS  contain  * Device", "score": 0, "counterpart": None},
    {"dsl": "1  SHAS  contain  1 ActivityLog", "score": 0, "counterpart": None},
    {"dsl": "1  SHAS  contain  1 Address", "score": 0, "counterpart": None},
    {"dsl": "1  SHAS  contain  * Room", "score": 0, "counterpart": None},
    {"dsl": "1  SHAS  contain  * AutomationRule", "score": 0, "counterpart": None},
    {
        "dsl": "*  PreCondition associate  1 ActivityLog",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "*  PreCondition associate  * Room",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "*  PreCondition associate  * Device", "score": 0, "counterpart": None},
]
