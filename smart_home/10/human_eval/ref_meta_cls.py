{
    "DeviceStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "DeviceStatus(Activated, Deactivated)",
        "counterpart": "Status",
        "attributes": {
            "Activated": {"score": 1, "counterpart": ("ON", "Status")},
            "Deactivated": {"score": 1, "counterpart": ("OFF", "Status")},
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
        "counterpart": "BooleanOperator",
        "attributes": {
            "AND": {"score": 1, "counterpart": ("AND", "BooleanOperator")},
            "OR": {"score": 1, "counterpart": ("OR", "BooleanOperator")},
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
            "DeviceStatus deviceStatus": {"score": 0, "counterpart": None},
            "int deviceID": {
                "score": 1,
                "counterpart": ("Integer uDI", "abstract Device"),
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
        "counterpart": "Controller",
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
                "counterpart": ("Date timestamp", "abstract Device"),
            }
        },
    },
    "SensorReading": {
        "score": 0.5,
        "type": "regular",
        "dsl": "SensorReading(double value)",
        "counterpart": ("Integer reading", "Sensor"),
        "attributes": {"double value": {"score": 0, "counterpart": None}},
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand (CommandType commandType, CommandStatus commandStatus)",
        "counterpart": "Command",
        "attributes": {
            "CommandType commandType": {"score": 0, "counterpart": None},
            "CommandStatus commandStatus": {
                "score": 1,
                "counterpart": ("ControllerStatus status", "Command"),
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
                "counterpart": ("Status status", "AutomationRule"),
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
        "score": 0.5,
        "type": "regular",
        "dsl": "RelationalTerm()",
        "counterpart": "abstract RelationalTerm",
        "attributes": {},
    },
    "NotExpression": {
        "score": 0.5,
        "type": "regular",
        "dsl": "NotExpression()",
        "counterpart": ("NOT", "BooleanOperator"),
        "attributes": {},
    },
    "BinaryExpression": {
        "score": 1,
        "type": "regular",
        "dsl": "BinaryExpression(BinaryOp binaryOp)",
        "counterpart": "Operator",
        "attributes": {
            "BinaryOp binaryOp": {
                "score": 1,
                "counterpart": ("BooleanOperator operator", "Operator"),
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
