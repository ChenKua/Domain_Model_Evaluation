[
    {
        "dsl": "1 Home contain * Room",
        "score": 1,
        "counterpart": "1 SmartHome contain * Room",
    },
    {
        "dsl": "1 Home contain 1 ActivityLog",
        "score": 0.5,
        "counterpart": "1 SmartHome contain 0..1 ActivityLog",
    },
    {
        "dsl": "1 Room contain * Device",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1 ActivityLog associate  * SensorReading",
        "score": 0.5,
        "counterpart": "1 ActivityLog contain * SensorReading",
    },
    {
        "dsl": "1 ActivityLog associate   * Command",
        "score": 0.5,
        "counterpart": "1 ActivityLog contain * ControlCommand",
    },
    {
        "dsl": "1 Sensor contain * SensorReading",
        "score": 0.5,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "1 Actuator contain * Command",
        "score": 0.5,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "1 AutomationRule contain  0..1 ComposedRelation",
        "score": 1,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
    },
    {
        "dsl": "* AtomicRelation associate  0..1 Room",
        "score": 1,
        "counterpart": "* RelationalTerm associate 0..1  Room",
    },
    {
        "dsl": "* AtomicRelation associate  0..1 Device",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "* AtomicRelation associate  0..1 Command",
        "score": 1,
        "counterpart": "* RelationalTerm associate 0..1  ControlCommand",
    },
    {
        "dsl": "1 ComposedRelation contain  2 AtomicRelation",
        "score": 0.5,
        "counterpart": "0..1 BinaryExpression associate 1 BooleanExpression",
    },
    {
        "dsl": "Sensor inherit Device",
        "score": 1,
        "counterpart": "SensorDevice inherit Device",
    },
    {
        "dsl": "Actuator inherit Device",
        "score": 1,
        "counterpart": "ActuatorDevice inherit Device",
    },
    {
        "dsl": "1 AutomationRule contain 0..1  AtomicRelation",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "1 User contain * AutomationRule", "score": 0, "counterpart": None},
]
