{
    "CommandType": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandType(lockDoor, turnOnHeating)",
        "counterpart": "CommandType",
        "attributes": {
            "lockDoor": {"score": 1, "counterpart": ("lockDoor", "CommandType")},
            "turnOnHeating": {
                "score": 1,
                "counterpart": ("turnOnHeating", "CommandType"),
            },
        },
    },
    "Status": {
        "score": 1,
        "type": "enum",
        "dsl": "Status(requested, completed, failed)",
        "counterpart": "CommandStatus",
        "attributes": {
            "requested": {"score": 1, "counterpart": ("Requested", "CommandStatus")},
            "completed": {"score": 1, "counterpart": ("Completed", "CommandStatus")},
            "failed": {"score": 1, "counterpart": ("Failed", "CommandStatus")},
        },
    },
    "Operator": {
        "score": 1,
        "type": "enum",
        "dsl": "Operator(NOT, AND, OR)",
        "counterpart": "BinaryOp",
        "attributes": {
            "NOT": {"score": 0.5, "counterpart": (None, "NotExpression")},
            "AND": {"score": 1, "counterpart": ("AND", "BinaryOp")},
            "OR": {"score": 1, "counterpart": ("OR", "BinaryOp")},
        },
    },
    "Home": {
        "score": 1,
        "type": "regular",
        "dsl": "Home( string address, string singleton)",
        "counterpart": "SmartHome",
        "attributes": {
            "string address": {
                "score": 0.5,
                "counterpart": ("string postalCode", "Address"),
            },
            "string singleton": {
                "score": 0,
                "counterpart": None,
            },
        },
    },
    "User": {
        "score": 1,
        "type": "regular",
        "dsl": "User( string user, string password)",
        "counterpart": "User",
        "attributes": {
            "string user": {"score": 1, "counterpart": ("string name", "User")},
            "string password": {
                "score": 0,
                "counterpart": None,
            },
        },
    },
    "Room": {
        "score": 1,
        "type": "regular",
        "dsl": "Room(string name)",
        "counterpart": "Room",
        "attributes": {
            "string name": {
                "score": 0,
                "counterpart": None,
            }
        },
    },
    "Device": {
        "score": 0.5,
        "type": "regular",
        "dsl": "Device( int uid, boolean isEnabled)",
        "counterpart": "abstract Device",
        "attributes": {
            "int uid": {"score": 1, "counterpart": ("int deviceID", "abstract Device")},
            "boolean isEnabled": {
                "score": 1,
                "counterpart": ("DeviceStatus deviceStatus", "abstract Device"),
            },
        },
    },
    "Sensor": {
        "score": 1,
        "type": "regular",
        "dsl": "Sensor()",
        "counterpart": "SensorDevice",
        "attributes": {},
    },
    "Actuator": {
        "score": 1,
        "type": "regular",
        "dsl": "Actuator()",
        "counterpart": "ActuatorDevice",
        "attributes": {},
    },
    "ActivityLog": {
        "score": 1,
        "type": "regular",
        "dsl": "ActivityLog()",
        "counterpart": "ActivityLog",
        "attributes": {},
    },
    "SensorReading": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorReading( double reading, Time timeStamp)",
        "counterpart": "SensorReading",
        "attributes": {
            "double reading": {
                "score": 1,
                "counterpart": ("double value", "SensorReading"),
            },
            "Time timeStamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
        },
    },
    "Command": {
        "score": 1,
        "type": "regular",
        "dsl": "Command( commandType type, Time timeStamp, Status status)",
        "counterpart": "ControlCommand",
        "attributes": {
            "commandType type": {
                "score": 1,
                "counterpart": ("CommandType commandType", "ControlCommand"),
            },
            "Time timeStamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
            "Status status": {
                "score": 1,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            },
        },
    },
    "AutomationRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AutomationRule()",
        "counterpart": "AlertRule",
        "attributes": {},
    },
    "ComposedRelation": {
        "score": 0.5,
        "type": "regular",
        "dsl": "ComposedRelation( Operator operator)",
        "counterpart": "abstract BooleanExpression",
        "attributes": {
            "Operator operator": {
                "score": 0.5,
                "counterpart": ("BinaryOp binaryOp", "BinaryExpression"),
            }
        },
    },
    "AtomicRelation": {
        "score": 1,
        "type": "regular",
        "dsl": "AtomicRelation( condition)",
        "counterpart": "RelationalTerm",
        "attributes": {"condition": {"score": 0, "counterpart": None}},
    },
}
