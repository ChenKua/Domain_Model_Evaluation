[
    {"dsl": "1 SHAS contain  1..* Room", "score": 0, "counterpart": None},
    {"dsl": "1 SHAS contain  1 ActivityLog", "score": 0, "counterpart": None},
    {"dsl": "1 SHAS contain  * AutomationRule", "score": 0, "counterpart": None},
    {"dsl": "1 SHAS associate  * AutomationRule", "score": 0, "counterpart": None},
    {"dsl": "1 Room contain  * Device", "score": 0, "counterpart": None},
    {
        "dsl": "1 ActivityLog contain  * SensorReading",
        "score": 1,
        "counterpart": "1 ActivityLog contain * SensorReading",
    },
    {
        "dsl": "1 ActivityLog contain  * ActuatorCommand",
        "score": 1,
        "counterpart": "1 ActivityLog contain * ControlCommand",
    },
    {
        "dsl": "1 Sensor associate  * SensorReading",
        "score": 1,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "1 Actuator associate  * ActuatorCommand",
        "score": 1,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "1 AutomationRule associate  1 Precondition",
        "score": 0.5,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
    },
    {
        "dsl": "1 AutomationRule associate  * ActuatorCommand",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1 AtomicTerm associate  1..* Element",
        "score": 0.5,
        "counterpart": "* RelationalTerm associate 0..1  RuntimeElement",
    },
    {
        "dsl": "1 Precondition associate  1..* Relation",
        "score": 0.5,
        "counterpart": "0..1 BinaryExpression associate 1 BooleanExpression",
    },
    {
        "dsl": "SensorReading inherit  Element",
        "score": 1,
        "counterpart": "SensorReading inherit RuntimeElement",
    },
    {
        "dsl": "ActuatorCommand inherit  Element",
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
    {"dsl": "Room inherit  Element", "score": 0, "counterpart": None},
    {"dsl": "Device inherit  Element", "score": 0, "counterpart": None},
    {"dsl": "1 Relation associate  1 AtomicTerm", "score": 0, "counterpart": None},
    {"dsl": "1 Relation associate  0..1 AtomicTerm", "score": 0, "counterpart": None},
    {
        "dsl": "1 AutomationRule associate  * AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1 AutomationRule associate  * AutomationRule",
        "score": 0,
        "counterpart": None,
    },
]
