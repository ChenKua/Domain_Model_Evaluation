{
    "DeviceState": {
        "score": 1,
        "type": "enum",
        "dsl": "DeviceState(activated,deactivated)",
        "counterpart": "DeviceStatus",
        "attributes": {
            "activated": {"score": 1, "counterpart": ("Activated", "DeviceStatus")},
            "deactivated": {"score": 1, "counterpart": ("Deactivated", "DeviceStatus")},
        },
    },
    "CommandType": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandType(lockDoor,turnOnHeating,other)",
        "counterpart": "CommandType",
        "attributes": {
            "lockDoor": {"score": 1, "counterpart": ("lockDoor", "CommandType")},
            "turnOnHeating": {
                "score": 1,
                "counterpart": ("turnOnHeating", "CommandType"),
            },
            "other": {"score": 0, "counterpart": None},
        },
    },
    "CommandStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandStatus(requested,completed,failed,pending,other)",
        "counterpart": "CommandStatus",
        "attributes": {
            "requested": {"score": 1, "counterpart": ("Requested", "CommandStatus")},
            "completed": {"score": 1, "counterpart": ("Completed", "CommandStatus")},
            "failed": {"score": 1, "counterpart": ("Failed", "CommandStatus")},
            "pending": {"score": 0, "counterpart": None},
            "other": {"score": 0, "counterpart": None},
        },
    },
    "State": {
        "score": 1,
        "type": "enum",
        "dsl": "State(activated,deactivated)",
        "counterpart": "RuleStatus",
        "attributes": {
            "activated": {"score": 1, "counterpart": ("activated", "RuleStatus")},
            "deactivated": {"score": 1, "counterpart": ("deactivated", "RuleStatus")},
        },
    },
    "BooleanOps": {
        "score": 1,
        "type": "enum",
        "dsl": "BooleanOps(AND,OR,NOT)",
        "counterpart": "BinaryOp",
        "attributes": {
            "AND": {"score": 1, "counterpart": ("AND", "BinaryOp")},
            "OR": {"score": 1, "counterpart": ("OR", "BinaryOp")},
            "NOT": {"score": 0.5, "counterpart": (None, "NotExpression")},
        },
    },
    "SensorType": {
        "score": 0,
        "type": "enum",
        "dsl": "SensorType(mouvement,temperature,other)",
        "counterpart": None,
        "attributes": {
            "mouvement": {"score": 0, "counterpart": None},
            "temperature": {"score": 0, "counterpart": None},
            "other": {"score": 0, "counterpart": None},
        },
    },
    "ActuatorType": {
        "score": 0,
        "type": "enum",
        "dsl": "ActuatorType(light,lock,other)",
        "counterpart": None,
        "attributes": {
            "light": {"score": 0, "counterpart": None},
            "lock": {"score": 0, "counterpart": None},
            "other": {"score": 0, "counterpart": None},
        },
    },
    "SHAS": {
        "score": 1,
        "type": "regular",
        "dsl": "SHAS()",
        "counterpart": "SHAS",
        "attributes": {},
    },
    "SmartHome": {
        "score": 1,
        "type": "regular",
        "dsl": "SmartHome()",
        "counterpart": "SmartHome",
        "attributes": {},
    },
    "User": {
        "score": 1,
        "type": "regular",
        "dsl": "User()",
        "counterpart": "User",
        "attributes": {},
    },
    "Address": {
        "score": 1,
        "type": "regular",
        "dsl": "Address( string street, string city, string country, int postalCode)",
        "counterpart": "Address",
        "attributes": {
            "string street": {"score": 1, "counterpart": ("string street", "Address")},
            "string city": {"score": 1, "counterpart": ("string city", "Address")},
            "string country": {
                "score": 1,
                "counterpart": ("string aptNumber", "Address"),
            },
            "int postalCode": {
                "score": 1,
                "counterpart": ("string postalCode", "Address"),
            },
        },
    },
    "Room": {
        "score": 1,
        "type": "regular",
        "dsl": "Room()",
        "counterpart": "Room",
        "attributes": {},
    },
    "abstract Device": {
        "score": 1,
        "type": "abstract",
        "dsl": "abstract Device( int deviceID, DeviceState state)",
        "counterpart": "abstract Device",
        "attributes": {
            "int deviceID": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
            "DeviceState state": {
                "score": 1,
                "counterpart": ("DeviceStatus deviceStatus", "abstract Device"),
            },
        },
    },
    "Sensor": {
        "score": 1,
        "type": "regular",
        "dsl": "Sensor( SensorType kind)",
        "counterpart": "SensorDevice",
        "attributes": {"SensorType kind": {"score": 0, "counterpart": None}},
    },
    "Actuator": {
        "score": 1,
        "type": "regular",
        "dsl": "Actuator( ActuatorType kind)",
        "counterpart": "ActuatorDevice",
        "attributes": {"ActuatorType kind": {"score": 0, "counterpart": None}},
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
        "dsl": "SensorReading( Double measuredValue, Time timeStamp)",
        "counterpart": "SensorReading",
        "attributes": {
            "Double measuredValue": {
                "score": 1,
                "counterpart": ("double value", "SensorReading"),
            },
            "Time timeStamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand( Time timeStamp, CommandType commandType, CommandStatus commandStatus)",
        "counterpart": "ControlCommand",
        "attributes": {
            "Time timeStamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
            "CommandType commandType": {
                "score": 1,
                "counterpart": ("CommandType commandType", "ControlCommand"),
            },
            "CommandStatus commandStatus": {
                "score": 1,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            },
        },
    },
    "AutomationRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AutomationRule( State ruleState)",
        "counterpart": "AlertRule",
        "attributes": {
            "State ruleState": {
                "score": 1,
                "counterpart": ("RuleStatus ruleStatus", "AlertRule"),
            }
        },
    },
    "PreCondition": {
        "score": 1,
        "type": "regular",
        "dsl": "PreCondition()",
        "counterpart": "abstract BooleanExpression",
        "attributes": {},
    },
    "AtomicRelationalTerm": {
        "score": 1,
        "type": "regular",
        "dsl": "AtomicRelationalTerm( Room room, Sensor sensor, Actuator actuator, ControlCommand controlCommand, SensorReading sensorReading)",
        "counterpart": "RelationalTerm",
        "attributes": {
            "Room room": {"score": 0, "counterpart": None},
            "Sensor sensor": {"score": 0, "counterpart": None},
            "Actuator actuator": {"score": 0, "counterpart": None},
            "ControlCommand controlCommand": {"score": 0, "counterpart": None},
            "SensorReading sensorReading": {"score": 0, "counterpart": None},
        },
    },
    "BooleanRelationalTerm": {
        "score": 1,
        "type": "regular",
        "dsl": "BooleanRelationalTerm( BooleanOps operator)",
        "counterpart": "BinaryExpression",
        "attributes": {
            "BooleanOps operator": {
                "score": 1,
                "counterpart": ("BinaryOp binaryOp", "BinaryExpression"),
            }
        },
    },
    "Action": {
        "score": 1,
        "type": "regular",
        "dsl": "Action()",
        "counterpart": "CommandSequence",
        "attributes": {},
    },
}
