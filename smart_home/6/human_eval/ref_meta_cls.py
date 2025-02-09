{
    "DeviceStatus": {
        "score": 0,
        "type": "enum",
        "dsl": "DeviceStatus(Activated, Deactivated)",
        "counterpart": None,
        "attributes": {
            "Activated": {
                "score": 0,
                "counterpart": None,
            },
            "Deactivated": {
                "score": 0,
                "counterpart": None,
            },
        },
    },
    "CommandType": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandType (lockDoor, turnOnHeating)",
        "counterpart": "ControlType",
        "attributes": {
            "lockDoor": {"score": 1, "counterpart": ("LockDoor", "ControlType")},
            "turnOnHeating": {
                "score": 1,
                "counterpart": ("TurnOnHeating", "ControlType"),
            },
        },
    },
    "CommandStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandStatus (Requested, Completed, Failed)",
        "counterpart": "ControlStatus",
        "attributes": {
            "Requested": {"score": 1, "counterpart": ("Requested", "ControlStatus")},
            "Completed": {"score": 1, "counterpart": ("Completed", "ControlStatus")},
            "Failed": {"score": 1, "counterpart": ("Failed", "ControlStatus")},
        },
    },
    "RuleStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "RuleStatus (created, edited, activated, deactivated )",
        "counterpart": "AutomationStatus",
        "attributes": {
            "created": {"score": 1, "counterpart": ("Created", "AutomationStatus")},
            "edited": {"score": 1, "counterpart": ("Edited", "AutomationStatus")},
            "activated": {
                "score": 1,
                "counterpart": ("Activated", "AutomationStatus"),
            },
            "deactivated": {
                "score": 1,
                "counterpart": ("Deactivated", "AutomationStatus"),
            },
        },
    },
    "BinaryOp": {
        "score": 1,
        "type": "enum",
        "dsl": "BinaryOp (AND, OR )",
        "counterpart": "ConnectingOperator",
        "attributes": {
            "AND": {"score": 1, "counterpart": ("AND", "ConnectingOperator")},
            "OR": {"score": 1, "counterpart": ("OR", "ConnectingOperator")},
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
        "score": 1,
        "type": "regular",
        "dsl": "User(string name)",
        "counterpart": "User",
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
            "string city": {"score": 0.5, "counterpart": ("String address", "SHAS")},
            "string postalCode": {
                "score": 0,
                "counterpart": ("String address", "SHAS"),
            },
            "string street": {"score": 0, "counterpart": ("String address", "SHAS")},
            "string aptNumber": {"score": 0, "counterpart": ("String address", "SHAS")},
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
                "score": 0.5,
                "counterpart": ("boolean activated", "abstract Device"),
            },
            "int deviceID": {
                "score": 1,
                "counterpart": ("unique int identifier", "abstract Device"),
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
                "counterpart": ("immutable int  measuredValue", "SensorReading"),
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
                "counterpart": ("ControlType controlType", "ControlCommand"),
            },
            "CommandStatus commandStatus": {
                "score": 1,
                "counterpart": ("ControlStatus controlStatus", "ControlCommand"),
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
                "counterpart": ("AutomationStatus automationStatus", "AutomationRule"),
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
        "score": 1,
        "type": "regular",
        "dsl": "RelationalTerm()",
        "counterpart": "RelationalTerm",
        "attributes": {},
    },
    "NotExpression": {
        "score": 0.5,
        "type": "regular",
        "dsl": "NotExpression()",
        "counterpart": ("NOT", "ConnectingOperator"),
        "attributes": {},
    },
    "BinaryExpression": {
        "score": 1,
        "type": "regular",
        "dsl": "BinaryExpression(BinaryOp binaryOp)",
        "counterpart": "BooleanOperator",
        "attributes": {
            "BinaryOp binaryOp": {
                "score": 1,
                "counterpart": ("connectingOperator", "ConnectingOperator"),
            }
        },
    },
    "CommandSequence": {
        "score": 1,
        "type": "regular",
        "dsl": "CommandSequence()",
        "counterpart": "Action",
        "attributes": {},
    },
}
