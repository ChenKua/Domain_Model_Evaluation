{
    "DeviceStatus": {
        "score": 0,
        "type": "enum",
        "dsl": "DeviceStatus(Activated, Deactivated)",
        "counterpart": None,
        "attributes": {
            "Activated": {
                "score": 0.5,
                "counterpart": ("boolean isActivated", "abstract Device"),
            },
            "Deactivated": {"score": 0, "counterpart": None},
        },
    },
    "CommandType": {
        "score": 0,
        "type": "enum",
        "dsl": "CommandType (lockDoor, turnOnHeating)",
        "counterpart": None,
        "attributes": {
            "lockDoor": {"score": 0, "counterpart": None},
            "turnOnHeating": {"score": 0, "counterpart": None},
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
            "deactivated": {"score": 0, "counterpart": None},
        },
    },
    "BinaryOp": {
        "score": 1,
        "type": "enum",
        "dsl": "BinaryOp (AND, OR )",
        "counterpart": "RelationType",
        "attributes": {
            "AND": {"score": 1, "counterpart": ("AND", "RelationType")},
            "OR": {"score": 1, "counterpart": ("OR", "RelationType")},
        },
    },
    "SHAS": {
        "score": 0,
        "type": "regular",
        "dsl": "SHAS()",
        "counterpart": None,
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
        "score": 1,
        "type": "regular",
        "dsl": "Address(string city, string postalCode, string street, string aptNumber)",
        "counterpart": "Address",
        "attributes": {
            "string city": {"score": 1, "counterpart": ("String city", "Address")},
            "string postalCode": {
                "score": 1,
                "counterpart": ("String postalCode", "Address"),
            },
            "string street": {
                "score": 1,
                "counterpart": ("String streetName", "Address"),
            },
            "string aptNumber": {
                "score": 1,
                "counterpart": ("String streetNumber", "Address"),
            },
        },
    },
    "Room": {
        "score": 1,
        "type": "regular",
        "dsl": "Room()",
        "counterpart": "SmartRoom",
        "attributes": {},
    },
    "abstract Device": {
        "score": 1,
        "type": "abstract",
        "dsl": "abstract Device(DeviceStatus deviceStatus, int deviceID)",
        "counterpart": "abstract Device",
        "attributes": {
            "DeviceStatus deviceStatus": {"score": 0, "counterpart": None},
            "int deviceID": {
                "score": 1,
                "counterpart": ("autounique identifier", "abstract Device"),
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
    "abstract RuntimeElement": {
        "score": 0,
        "type": "abstract",
        "dsl": "abstract RuntimeElement(time timestamp)",
        "counterpart": None,
        "attributes": {
            "time timestamp": {
                "score": 0.5,
                "counterpart": ("Date timestamp", "ControlCommand"),
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
                "score": 0.5,
                "counterpart": ("String value", "MeasuredValue"),
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
                "score": 0.5,
                "counterpart": ("String commandName", "ControlCommand"),
            },
            "CommandStatus commandStatus": {
                "score": 0.5,
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
                "counterpart": (
                    "RelationType relationToNextPrecondition",
                    "AutomationPrecondition",
                ),
            }
        },
    },
    "abstract BooleanExpression": {
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract BooleanExpression()",
        "counterpart": "AutomationPrecondition",
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
        "score": 0.5,
        "type": "regular",
        "dsl": "NotExpression()",
        "counterpart": ("NOT", "RelationType"),
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
        "counterpart": "AutomationTrigger",
        "attributes": {},
    },
}
