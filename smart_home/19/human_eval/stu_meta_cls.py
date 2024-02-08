{
    "CommandType": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandType(lockDoor,turnOnHeating)",
        "counterpart": "CommandType",
        "attributes": {
            "lockDoor": {"score": 1, "counterpart": ("lockDoor", "CommandType")},
            "turnOnHeating": {
                "score": 1,
                "counterpart": ("turnOnHeating", "CommandType"),
            },
        },
    },
    "Operator": {
        "score": 1,
        "type": "enum",
        "dsl": "Operator(And,Or,Not)",
        "counterpart": "BinaryOp",
        "attributes": {
            "And": {"score": 1, "counterpart": ("AND", "BinaryOp")},
            "Or": {"score": 1, "counterpart": ("OR", "BinaryOp")},
            "Not": {"score": 0, "counterpart": None},
        },
    },
    "DeviceType": {
        "score": 0,
        "type": "enum",
        "dsl": "DeviceType(TemperatureSenor,MovementSensor,LockController,LightController)",
        "counterpart": None,
        "attributes": {
            "TemperatureSenor": {"score": 0, "counterpart": None},
            "MovementSensor": {"score": 0, "counterpart": None},
            "LockController": {"score": 0, "counterpart": None},
            "LightController": {"score": 0, "counterpart": None},
        },
    },
    "SmartHomeApplicationSystem": {
        "score": 1,
        "type": "regular",
        "dsl": "SmartHomeApplicationSystem()",
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
        "dsl": "Address( String postalCode, String streetName, String city, Integer streetNumber, Integer apartmentNumber)",
        "counterpart": "Address",
        "attributes": {
            "String postalCode": {
                "score": 1,
                "counterpart": ("string postalCode", "Address"),
            },
            "String streetName": {
                "score": 1,
                "counterpart": ("string street", "Address"),
            },
            "String city": {"score": 1, "counterpart": ("string city", "Address")},
            "Integer streetNumber": {"score": 0, "counterpart": None},
            "Integer apartmentNumber": {
                "score": 1,
                "counterpart": ("string aptNumber", "Address"),
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
        "dsl": "abstract Device( boolean isActive, unique Integer id, DeviceType deviceType)",
        "counterpart": "abstract Device",
        "attributes": {
            "boolean isActive": {"score": 0.5, "counterpart": ("DeviceStatus deviceStatus", "abstract Device")},
            "unique Integer id": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
            "DeviceType deviceType": {
                "score": 0,
                "counterpart": None,
            },
        },
    },
    "SensorDevice": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorDevice()",
        "counterpart": "SensorDevice",
        "attributes": {},
    },
    "ActuatorDevice": {
        "score": 1,
        "type": "regular",
        "dsl": "ActuatorDevice()",
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
        "dsl": "SensorReading( Double measuredValue, String timeStamp)",
        "counterpart": "SensorReading",
        "attributes": {
            "Double measuredValue": {
                "score": 1,
                "counterpart": ("double value", "SensorReading"),
            },
            "String timeStamp": {"score": 0, "counterpart": None},
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand( String timeStamp, String commandStatus)",
        "counterpart": "ControlCommand",
        "attributes": {
            "String timeStamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
            "String commandStatus": {
                "score": 0.5,
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
    "PreCondition": {
        "score": 0.5,
        "type": "regular",
        "dsl": "PreCondition()",
        "counterpart": "abstract BooleanExpression",
        "attributes": {},
    },
    "RelationalTerm": {
        "score": 1,
        "type": "regular",
        "dsl": "RelationalTerm( String condition)",
        "counterpart": "RelationalTerm",
        "attributes": {
            "String condition": {"score": 0, "counterpart": None}
        },
    },
    "BooleanOperator": {
        "score": 1,
        "type": "regular",
        "dsl": "BooleanOperator( Operator operator)",
        "counterpart": "BinaryExpression",
        "attributes": {"Operator operator": {"score": 1, "counterpart": ("BinaryOp binaryOp","BinaryExpression")}},
    },
    "Action": {
        "score": 1,
        "type": "regular",
        "dsl": "Action()",
        "counterpart": "CommandSequence",
        "attributes": {},
    },
    "PredefinedCommand": {
        "score": 0,
        "type": "regular",
        "dsl": "PredefinedCommand( CommandType commandType)",
        "counterpart": None,
        "attributes": {
            "CommandType commandType": {
                "score": 0.5,
                "counterpart": ("CommandType commandType", "ControlCommand"),
            }
        },
    },
}
