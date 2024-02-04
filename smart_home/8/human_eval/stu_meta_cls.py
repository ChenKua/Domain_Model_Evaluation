{
    "CommandType": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandType ( LockDoor, TurnOnHeating, TurnOnLights )",
        "counterpart": "CommandType",
        "attributes": {
            "LockDoor": {"score": 1, "counterpart": ("lockDoor", "CommandType")},
            "TurnOnHeating": {
                "score": 1,
                "counterpart": ("turnOnHeating", "CommandType"),
            },
            "TurnOnLights": {"score": 0, "counterpart": None},
        },
    },
    "CommandStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandStatus ( Requested, Completed, Failed )",
        "counterpart": "CommandStatus",
        "attributes": {
            "Requested": {"score": 1, "counterpart": ("Requested", "CommandStatus")},
            "Completed": {"score": 1, "counterpart": ("Completed", "CommandStatus")},
            "Failed": {"score": 1, "counterpart": ("Failed", "CommandStatus")},
        },
    },
    "Operator": {
        "score": 1,
        "type": "enum",
        "dsl": "Operator ( AND, OR, NOT)",
        "counterpart": "BinaryOp",
        "attributes": {
            "AND": {"score": 1, "counterpart": ("AND", "BinaryOp")},
            "OR": {"score": 1, "counterpart": ("OR", "BinaryOp")},
            "NOT": {"score": 0.5, "counterpart": (None, "NotExpression")},
        },
    },
    "SensorType": {
        "score":0,
        "type": "enum",
        "dsl": "SensorType ( Temperature, Movement )",
        "counterpart": None,
        "attributes": {
            "Temperature": {"score": 0, "counterpart": None},
            "Movement": {"score": 0, "counterpart": None},
        },
    },
    "ActuatorType": {
        "score": 0,
        "type": "enum",
        "dsl": "ActuatorType ( Light, Lock )",
        "counterpart": None,
        "attributes": {
            "Light": {"score": 0, "counterpart": None},
            "Lock": {"score": 0, "counterpart": None},
        },
    },
    "SHAS": {
        "score": 1,
        "type": "regular",
        "dsl": "SHAS()",
        "counterpart": "SHAS",
        "attributes": {},
    },
    "Room": {
        "score": 1,
        "type": "regular",
        "dsl": "Room()",
        "counterpart": "Room",
        "attributes": {},
    },
    "Device": {
        "score": 0.5,
        "type": "regular",
        "dsl": "Device( auto unique identifier, Boolean isActive)",
        "counterpart": "abstract Device",
        "attributes": {
            "auto unique identifier": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
            "Boolean isActive": {"score": 0.5, "counterpart": ("DeviceStatus deviceStatus","abstract Devices")},
        },
    },
    "Sensor": {
        "score": 1,
        "type": "regular",
        "dsl": "Sensor( SensorType type)",
        "counterpart": "SensorDevice",
        "attributes": {"SensorType type": {"score": 0, "counterpart": None}},
    },
    "Actuator": {
        "score": 1,
        "type": "regular",
        "dsl": "Actuator( ActuatorType type)",
        "counterpart": "ActuatorDevice",
        "attributes": {"ActuatorType type": {"score": 0, "counterpart": None}},
    },
    "ActivityLog": {
        "score": 1,
        "type": "regular",
        "dsl": "ActivityLog()",
        "counterpart": "ActivityLog",
        "attributes": {},
    },
    "Element": {
        "score": 0.5,
        "type": "regular",
        "dsl": "Element()",
        "counterpart": "abstract RuntimeElement",
        "attributes": {},
    },
    "SensorReading": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorReading( Double reading, Time timestamp, String readingType)",
        "counterpart": "SensorReading",
        "attributes": {
            "Double reading": {
                "score": 1,
                "counterpart": ("double value", "SensorReading"),
            },
            "Time timestamp": {"score": 0.5, "counterpart": ("time timestamp", "abstract RuntimeElement")},
            "String readingType": {
                "score": 0.5,
                "counterpart": ("string aptNumber", "Address"),
            },
        },
    },
    "ActuatorCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ActuatorCommand( CommandType type, Time timestamp, CommandStatus status)",
        "counterpart": "ControlCommand",
        "attributes": {
            "CommandType type": {
                "score": 1,
                "counterpart": ("CommandType commandType", "ControlCommand"),
            },
            "Time timestamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
            "CommandStatus status": {
                "score": 1,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            },
        },
    },
    "AutomationRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AutomationRule( Boolean isActive, Time activations)",
        "counterpart": "AlertRule",
        "attributes": {
            "Boolean isActive": {"score": 0.5, "counterpart": ("RuleStatus ruleStatus","AlertRule")},
            "Time activations": {"score": 0, "counterpart": None},
        },
    },
    "Precondition": {
        "score": 0.5,
        "type": "regular",
        "dsl": "Precondition( Boolean value)",
        "counterpart": "abstract BooleanExpression",
        "attributes": {
            "Boolean value": {"score": 0, "counterpart": None}
        },
    },
    "AtomicTerm": {
        "score": 1,
        "type": "regular",
        "dsl": "AtomicTerm( String expression, Boolean atomicValue)",
        "counterpart": "RelationalTerm",
        "attributes": {
            "String expression": {
                "score": 0,
                "counterpart": None,
            },
            "Boolean atomicValue": {"score": 0, "counterpart": None},
        },
    },
    "Relation": {
        "score": 1,
        "type": "regular",
        "dsl": "Relation( Operator op, Boolean value)",
        "counterpart": "BinaryExpression",
        "attributes": {
            "Operator op": {
                "score": 1,
                "counterpart": ("BinaryOp binaryOp", "BinaryExpression"),
            },
            "Boolean value": {"score": 0, "counterpart": None},
        },
    },
}
