{
    "DeviceStatus": {
        "score": 0,
        "type": "enum",
        "dsl": "DeviceStatus(Activated, Deactivated)",
        "counterpart": None,
        "attributes": {
            "Activated": {
                "score": 0.5,
                "counterpart": ("boolean activated", "abstract Device"),
            },
            "Deactivated": {"score": 0, "counterpart": None},
        },
    },
    "CommandType": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandType (lockDoor, turnOnHeating)",
        "counterpart": "ControllerType",
        "attributes": {
            "lockDoor": {
                "score": 1,
                "counterpart": ("LockController", "ControllerType"),
            },
            "turnOnHeating": {
                "score": 1,
                "counterpart": ("LightController", "ControllerType"),
            },
        },
    },
    "CommandStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandStatus (Requested, Completed, Failed)",
        "counterpart": "ControllerStatus",
        "attributes": {
            "Requested": {"score": 1, "counterpart": ("Requested", "ControllerStatus")},
            "Completed": {"score": 1, "counterpart": ("Completed", "ControllerStatus")},
            "Failed": {"score": 1, "counterpart": ("Failed", "ControllerStatus")},
        },
    },
    "RuleStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "RuleStatus (created, edited, activated, deactivated )",
        "counterpart": "AutomationRuleStatus",
        "attributes": {
            "created": {"score": 1, "counterpart": ("Created", "AutomationRuleStatus")},
            "edited": {"score": 1, "counterpart": ("Edited", "AutomationRuleStatus")},
            "activated": {
                "score": 1,
                "counterpart": ("Activated", "AutomationRuleStatus"),
            },
            "deactivated": {
                "score": 1,
                "counterpart": ("Deactivated", "AutomationRuleStatus"),
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
        "score": 0,
        "type": "regular",
        "dsl": "User(string name)",
        "counterpart": None,
        "attributes": {"string name": {"score": 0, "counterpart": None}},
    },
    "Address": {
        "score": 0.5,
        "type": "regular",
        "dsl": "Address(string city, string postalCode, string street, string aptNumber)",
        "counterpart": ("address", "SmartHome"),
        "attributes": {
            "string city": {"score": 0, "counterpart": None},
            "string postalCode": {"score": 0, "counterpart": None},
            "string street": {"score": 0, "counterpart": None},
            "string aptNumber": {"score": 0, "counterpart": None},
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
                "score": 0,
                "counterpart": None,
            },
            "int deviceID": {
                "score": 1,
                "counterpart": ("unique Integer id", "abstract Device"),
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
        "score": 0,
        "type": "regular",
        "dsl": "ActivityLog()",
        "counterpart": None,
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
                "counterpart": ("Time timestamp", "ControlCommand"),
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
                "counterpart": ("int measuredValue", "SensorReading"),
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
                "counterpart": ("ControllerType type", "ActuatorDevice"),
            },
            "CommandStatus commandStatus": {
                "score": 1,
                "counterpart": ("ControllerStatus status", "ControlCommand"),
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
                "score": 1,
                "counterpart": ("AutomationRuleStatus status", "AutomationRule"),
            }
        },
    },
    "abstract BooleanExpression": {
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract BooleanExpression()",
        "counterpart": ("boolean precondition", "AutomationRule"),
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
        "score": 0,
        "type": "regular",
        "dsl": "CommandSequence()",
        "counterpart": None,
        "attributes": {},
    },
}
