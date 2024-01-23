{
    "DeviceStatus": {
        "score": 0.5,
        "type": "enum",
        "dsl": "DeviceStatus(Activated, Deactivated)",
        "counterpart": ("String status", "abstract Device"),
        "attributes": {
            "Activated": {
                "score": 0.5,
                "counterpart": ("boolean isActivated", "abstract Device"),
            },
            "Deactivated": {
                "score": 0.5,
                "counterpart": ("boolean isActivated", "abstract Device"),
            },
        },
    },
    "CommandType": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandType (lockDoor, turnOnHeating)",
        "counterpart": "Command",
        "attributes": {
            "lockDoor": {"score": 1, "counterpart": ("lockDoor", "Command")},
            "turnOnHeating": {"score": 1, "counterpart": ("turnOnHeating", "Command")},
        },
    },
    "CommandStatus": {
        "score": 0,
        "type": "enum",
        "dsl": "CommandStatus (Requested, Completed, Failed)",
        "counterpart": None,
        "attributes": {
            "Requested": {"score": 0, "counterpart": None},
            "Completed": {"score": 0, "counterpart": None},
            "Failed": {"score": 0, "counterpart": None},
        },
    },
    "RuleStatus": {
        "score": 0,
        "type": "enum",
        "dsl": "RuleStatus (created, edited, activated, deactivated )",
        "counterpart": None,
        "attributes": {
            "created": {"score": 0, "counterpart": None},
            "edited": {"score": 0, "counterpart": None},
            "activated": {
                "score": 0.5,
                "counterpart": ("boolean isActivated", "AutomationRule"),
            },
            "deactivated": {
                "score": 0.5,
                "counterpart": ("boolean isActivated", "AutomationRule"),
            },
        },
    },
    "BinaryOp": {
        "score": 0,
        "type": "enum",
        "dsl": "BinaryOp (AND, OR )",
        "counterpart": None,
        "attributes": {
            "AND": {"score": 0, "counterpart": None},
            "OR": {"score": 0, "counterpart": None},
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
        "dsl": "User(string name)",
        "counterpart": "User",
        "attributes": {
            "string name": {"score": 1, "counterpart": ("string name", "User")}
        },
    },
    "Address": {
        "score": 1,
        "type": "regular",
        "dsl": "Address(string city, string postalCode, string street, string aptNumber)",
        "counterpart": "Address",
        "attributes": {
            "string city": {"score": 1, "counterpart": ("string city", "Address")},
            "string postalCode": {
                "score": 1,
                "counterpart": ("string postalCode", "Address"),
            },
            "string street": {
                "score": 1,
                "counterpart": ("string province", "Address"),
            },
            "string aptNumber": {
                "score": 1,
                "counterpart": ("string streetAddress", "Address"),
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
        "dsl": "abstract Device(DeviceStatus deviceStatus, int deviceID)",
        "counterpart": "abstract Device",
        "attributes": {
            "DeviceStatus deviceStatus": {
                "score": 1,
                "counterpart": ("String status", "abstract Device"),
            },
            "int deviceID": {
                "score": 1,
                "counterpart": ("String identifier", "abstract Device"),
            },
        },
    },
    "SensorDevice": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorDevice()",
        "counterpart": "Sensor",
        "attributes": {},
    },
    "ActuatorDevice": {
        "score": 1,
        "type": "regular",
        "dsl": "ActuatorDevice()",
        "counterpart": "Actuator",
        "attributes": {},
    },
    "ActivityLog": {
        "score": 1,
        "type": "regular",
        "dsl": "ActivityLog()",
        "counterpart": "ActivityLog",
        "attributes": {},
    },
    "abstract RuntimeElement": {
        "score": 0,
        "type": "abstract",
        "dsl": "abstract RuntimeElement(time timestamp)",
        "counterpart": None,
        "attributes": {
            "time timestamp": {
                "score": 0.5,
                "counterpart": ("String timeStamp", "ControlCommand"),
            }
        },
    },
    "SensorReading": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorReading(double value)",
        "counterpart": "SensorReading",
        "attributes": {
            "double value": {
                "score": 1,
                "counterpart": ("string measuredValue", "SensorReading"),
            }
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand (CommandType commandType, CommandStatus commandStatus)",
        "counterpart": "ControlCommand",
        "attributes": {
            "CommandType commandType": {
                "score": 1,
                "counterpart": ("Command command", "ControlCommand"),
            },
            "CommandStatus commandStatus": {
                "score": 1,
                "counterpart": ("String status", "ControlCommand"),
            },
        },
    },
    "AlertRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AlertRule (RuleStatus ruleStatus)",
        "counterpart": "AutomationRule",
        "attributes": {
            "RuleStatus ruleStatus": {
                "score": 0.5,
                "counterpart": ("boolean isActivated", "AutomationRule"),
            }
        },
    },
    "abstract BooleanExpression": {
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract BooleanExpression()",
        "counterpart": "Precondition",
        "attributes": {},
    },
    "RelationalTerm": {
        "score": 0,
        "type": "regular",
        "dsl": "RelationalTerm()",
        "counterpart": None,
        "attributes": {},
    },
    "NotExpression": {
        "score": 0,
        "type": "regular",
        "dsl": "NotExpression()",
        "counterpart": None,
        "attributes": {},
    },
    "BinaryExpression": {
        "score": 0,
        "type": "regular",
        "dsl": "BinaryExpression(BinaryOp binaryOp)",
        "counterpart": None,
        "attributes": {"BinaryOp binaryOp": {"score": 0, "counterpart": None}},
    },
    "CommandSequence": {
        "score": 1,
        "type": "regular",
        "dsl": "CommandSequence()",
        "counterpart": "Action",
        "attributes": {},
    },
}
