{
    "DeviceStatus": {
        "score": 0,
        "type": "enum",
        "dsl": "DeviceStatus(Activated, Deactivated)",
        "counterpart": None,
        "attributes": {
            "Activated": {"score": 0, "counterpart": None},
            "Deactivated": {"score": 0, "counterpart": None},
        },
    },
    "CommandType": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandType (lockDoor, turnOnHeating)",
        "counterpart": "CommandType",
        "attributes": {
            "lockDoor": {"score": 1, "counterpart": ("LockDoor", "CommandType")},
            "turnOnHeating": {
                "score": 1,
                "counterpart": ("TurnOnHeating", "CommandType"),
            },
        },
    },
    "CommandStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandStatus (Requested, Completed, Failed)",
        "counterpart": "CommandStatus",
        "attributes": {
            "Requested": {"score": 1, "counterpart": ("Requested", "CommandStatus")},
            "Completed": {"score": 1, "counterpart": ("Completed", "CommandStatus")},
            "Failed": {"score": 1, "counterpart": ("Failed", "CommandStatus")},
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
            "activated": {"score": 0, "counterpart": None},
            "deactivated": {"score": 0, "counterpart": None},
        },
    },
    "BinaryOp": {
        "score": 1,
        "type": "enum",
        "dsl": "BinaryOp (AND, OR )",
        "counterpart": "Operator",
        "attributes": {
            "AND": {"score": 1, "counterpart": ("AND", "Operator")},
            "OR": {"score": 1, "counterpart": ("OR", "Operator")},
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
        "score": 0,
        "type": "regular",
        "dsl": "SmartHome()",
        "counterpart": None,
        "attributes": {},
    },
    "User": {
        "score": 0,
        "type": "regular",
        "dsl": "User(string name)",
        "counterpart": None,
        "attributes": {
            "string name": {
                "score": 0,
                "counterpart": None,
            }
        },
    },
    "Address": {
        "score": 0,
        "type": "regular",
        "dsl": "Address(string city, string postalCode, string street, string aptNumber)",
        "counterpart": None,
        "attributes": {
            "string city": {
                "score": 0,
                "counterpart": None,
            },
            "string postalCode": {"score": 0, "counterpart": None},
            "string street": {"score": 0, "counterpart": None},
            "string aptNumber": {
                "score": 0,
                "counterpart": None,
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
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract Device(DeviceStatus deviceStatus, int deviceID)",
        "counterpart": "Device",
        "attributes": {
            "DeviceStatus deviceStatus": {"score": 0.5, "counterpart":  ("Boolean isActive", "Device")},
            "int deviceID": {
                "score": 1,
                "counterpart": ("auto unique identifier", "Device"),
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
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract RuntimeElement(time timestamp)",
        "counterpart": "Element",
        "attributes": {
            "time timestamp": {
                "score": 0.5,
                "counterpart": ("Time timestamp", "ActuatorCommand"),
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
                "counterpart": ("Double reading", "SensorReading"),
            }
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand (CommandType commandType, CommandStatus commandStatus)",
        "counterpart": "ActuatorCommand",
        "attributes": {
            "CommandType commandType": {
                "score": 1,
                "counterpart": ("CommandType type", "ActuatorCommand"),
            },
            "CommandStatus commandStatus": {
                "score": 1,
                "counterpart": ("CommandStatus status", "ActuatorCommand"),
            },
        },
    },
    "AlertRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AlertRule (RuleStatus ruleStatus)",
        "counterpart": "AutomationRule",
        "attributes": {"RuleStatus ruleStatus": {"score": 0.5, "counterpart": ("Boolean isActive", "AutomationRule")}},
    },
    "abstract BooleanExpression": {
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract BooleanExpression()",
        "counterpart": "Precondition",
        "attributes": {},
    },
    "RelationalTerm": {
        "score": 1,
        "type": "regular",
        "dsl": "RelationalTerm()",
        "counterpart": "AtomicTerm",
        "attributes": {},
    },
    "NotExpression": {
        "score": 0.5,
        "type": "regular",
        "dsl": "NotExpression()",
        "counterpart": ("NOT", "Operator"),
        "attributes": {},
    },
    "BinaryExpression": {
        "score": 1,
        "type": "regular",
        "dsl": "BinaryExpression(BinaryOp binaryOp)",
        "counterpart": "Relation",
        "attributes": {
            "BinaryOp binaryOp": {
                "score": 1,
                "counterpart": ("Operator op", "Relation"),
            }
        },
    },
    "CommandSequence": {
        "score": 0,
        "type": "regular",
        "dsl": "CommandSequence()",
        "counterpart": None,
        "attributes": {},
    },
}
