[
    {
        "dsl": "1 SHAS contain * SmartHome",
        "score": 0.5,
        "counterpart": "0..1 SHAS contain  0..1 Infrastructure_Map",
    },
    {
        "dsl": "1 SHAS contain * User",
        "score": 1,
        "counterpart": "1 SHAS contain  * User",
    },
    {"dsl": "1 SmartHome contain 0..1 Address", "score": 0, "counterpart": None},
    {
        "dsl": "1 SmartHome contain * Room",
        "score": 1,
        "counterpart": "1 Infrastructure_Map associate  * Room",
    },
    {"dsl": "1 SmartHome contain 0..1 ActivityLog", "score": 0, "counterpart": None},
    {"dsl": "* SmartHome associate * User", "score": 0, "counterpart": None},
    {"dsl": "1  SmartHome contain  * AlertRule", "score": 0, "counterpart": None},
    {"dsl": "1 Room contain * SensorDevice", "score": 0, "counterpart": None},
    {"dsl": "1 Room contain * ActuatorDevice", "score": 0, "counterpart": None},
    {
        "dsl": "1 ActivityLog contain * SensorReading",
        "score": 0.5,
        "counterpart": "1 Activity_Log associate  * Sensor_Reading",
    },
    {
        "dsl": "1 ActivityLog contain * ControlCommand",
        "score": 0.5,
        "counterpart": "1 Activity_Log associate  * Control_Command",
    },
    {
        "dsl": "* SensorReading associate 1 SensorDevice",
        "score": 0.5,
        "counterpart": "1 Sensor_Device contain  * Sensor_Reading",
    },
    {
        "dsl": "* ControlCommand associate 1 ActuatorDevice",
        "score": 0.5,
        "counterpart": "1 Actuator_Device contain  * Control_Command",
    },
    {
        "dsl": "1 AlertRule contain 0..1 BooleanExpression",
        "score": 0.5,
        "counterpart": "1 Automation_Rule contain  1 Precondition",
    },
    {
        "dsl": "1 AlertRule contain * CommandSequence",
        "score": 0.5,
        "counterpart": "1 Automation_Rule contain  1 Action",
    },
    {
        "dsl": "* RelationalTerm associate 0..1  Room",
        "score": 0.5,
        "counterpart": "0..1 Rational_Term associate  * Room",
    },
    {
        "dsl": "* RelationalTerm associate 0..1  SensorDevice",
        "score": 0.5,
        "counterpart": "0..1 Rational_Term associate  * Sensor_Device",
    },
    {
        "dsl": "* RelationalTerm associate 0..1  ActuatorDevice",
        "score": 0.5,
        "counterpart": "0..1 Rational_Term associate  * Actuator_Device",
    },
    {
        "dsl": "* RelationalTerm associate 0..1  SensorReading",
        "score": 0.5,
        "counterpart": "0..1 Rational_Term associate  * Sensor_Reading",
    },
    {
        "dsl": "* RelationalTerm associate 0..1  ControlCommand",
        "score": 0.5,
        "counterpart": "0..1 Rational_Term associate  * Control_Command",
    },
    {
        "dsl": "0..1 NotExpression associate 1 BooleanExpression",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "0..1 BinaryExpression associate 1 BooleanExpression",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "0..1 BinaryExpression associate 1 BooleanExpression",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "* CommandSequence associate 0..1 CommandSequence",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1 CommandSequence contain 0..1 ControlCommand",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "SensorReading inherit RuntimeElement", "score": 0, "counterpart": None},
    {"dsl": "ControlCommand inherit RuntimeElement", "score": 0, "counterpart": None},
    {"dsl": "NotExpression inherit BooleanExpression", "score": 0, "counterpart": None},
    {
        "dsl": "BinaryExpression inherit BooleanExpression",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "RelationalTerm inherit BooleanExpression",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "SensorDevice inherit Device",
        "score": 1,
        "counterpart": "Sensor_Device inherit  Device",
    },
    {
        "dsl": "ActuatorDevice inherit Device",
        "score": 1,
        "counterpart": "Actuator_Device inherit  Device",
    },
]
