[
    {
        "dsl": "1 SHAS contain  * User",
        "score": 1,
        "counterpart": "1 SHAS contain * User",
    },
    {"dsl": "1 SHAS  contain  * Room", "score": 0, "counterpart": None},
    {"dsl": "0..1 SHAS contain  0..1 Activity_Log", "score": 0, "counterpart": None},
    {
        "dsl": "0..1 SHAS contain  0..1 Hierarchy",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "0..1 SHAS contain  0..1 Infrastructure_Map",
        "score": 0.5,
        "counterpart": "1 SHAS contain * SmartHome",
    },
    {
        "dsl": "1 Infrastructure_Map associate  * Room",
        "score": 0.5,
        "counterpart": "1 SmartHome contain * Room",
    },
    {
        "dsl": "1 Infrastructure_Map associate  * Device",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "1 Room contain  * Device", "score": 0, "counterpart": None},
    {
        "dsl": "1 Activity_Log associate  * Sensor_Reading",
        "score": 0.5,
        "counterpart": "1 ActivityLog contain * SensorReading",
    },
    {
        "dsl": "1 Activity_Log associate  * Control_Command",
        "score": 0.5,
        "counterpart": "1 ActivityLog contain * ControlCommand",
    },
    {
        "dsl": "1 Sensor_Device contain  * Sensor_Reading",
        "score": 0.5,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "1 Actuator_Device contain  * Control_Command",
        "score": 0.5,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "1 Automation_Rule contain  1 Precondition",
        "score": 0.5,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
    },
    {
        "dsl": "1 Automation_Rule contain  1 Action",
        "score": 0.5,
        "counterpart": "1 AlertRule contain * CommandSequence",
    },
    {
        "dsl": "1 Automation_Rule associate * Alert",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "0..1 Rational_Term associate  * Room",
        "score": 0.5,
        "counterpart": "* RelationalTerm associate 0..1  Room",
    },
    {
        "dsl": "0..1 Rational_Term associate  * Sensor_Device",
        "score": 0.5,
        "counterpart": "* RelationalTerm associate 0..1  SensorDevice",
    },
    {
        "dsl": "0..1 Rational_Term associate  * Actuator_Device",
        "score": 0.5,
        "counterpart": "* RelationalTerm associate 0..1  ActuatorDevice",
    },
    {
        "dsl": "0..1 Rational_Term associate  * Sensor_Reading",
        "score": 0.5,
        "counterpart": "* RelationalTerm associate 0..1  SensorReading",
    },
    {
        "dsl": "0..1 Rational_Term associate  * Control_Command",
        "score": 0.5,
        "counterpart": "* RelationalTerm associate 0..1  ControlCommand",
    },
    {"dsl": "1 Precondition contain  * Rational_Term", "score": 0, "counterpart": None},
    {
        "dsl": "Sensor_Device inherit  Device",
        "score": 1,
        "counterpart": "SensorDevice inherit Device",
    },
    {
        "dsl": "Actuator_Device inherit  Device",
        "score": 1,
        "counterpart": "ActuatorDevice inherit Device",
    },
    {"dsl": "1 Hierarchy contain  * Automation_Rule", "score": 0, "counterpart": None},
]
