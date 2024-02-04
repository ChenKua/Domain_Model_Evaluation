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
        "counterpart": "Status",
        "attributes": {
            "Requested": {"score": 1, "counterpart": ("Requested", "Status")},
            "Completed": {"score": 1, "counterpart": ("Completed", "Status")},
            "Failed": {"score": 1, "counterpart": ("Failed", "Status")},
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
                "counterpart": ("boolean activated", "AutomationRule"),
            },
            "deactivated": {"score": 0, "counterpart": None},
        },
    },
    "BinaryOp": {
        "score": 1,
        "type": "enum",
        "dsl": "BinaryOp (AND, OR )",
        "counterpart": "Operator",
        "attributes": {
            "AND": {"score": 1, "counterpart": ("and", "Operator")},
            "OR": {"score": 1, "counterpart": ("or", "Operator")},
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
        "attributes": {"string name": {"score": 0, "counterpart": None}},
    },
    "Address": {
        "score": 0,
        "type": "regular",
        "dsl": "Address(string city, string postalCode, string street, string aptNumber)",
        "counterpart": None,
        "attributes": {
            "string city": {
                "score": 0.5,
                "counterpart": ("string address", "SmartHome"),
            },
            "string postalCode": {
                "score": 0.5,
                "counterpart": ("string address", "SmartHome"),
            },
            "string street": {
                "score": 0.5,
                "counterpart": ("string address", "SmartHome"),
            },
            "string aptNumber": {
                "score": 0.5,
                "counterpart": ("string address", "SmartHome"),
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
            "DeviceStatus deviceStatus": {"score": 0, "counterpart": None},
            "int deviceID": {"score": 1, "counterpart": ("int id", "abstract Device")},
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
        "score": 1,
        "type": "abstract",
        "dsl": "abstract RuntimeElement(time timestamp)",
        "counterpart": "abstract Dependency",
        "attributes": {
            "time timestamp": {
                "score": 0.5,
                "counterpart": ("DateTime timestamp", "SensorReading"),
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
            "CommandType commandType": {"score": 0, "counterpart": None},
            "CommandStatus commandStatus": {
                "score": 1,
                "counterpart": ("Status status", "ControlCommand"),
            },
        },
    },
    "AlertRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AlertRule (RuleStatus ruleStatus)",
        "counterpart": "AutomationRule",
        "attributes": {"RuleStatus ruleStatus": {"score": 0, "counterpart": None}},
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
        "counterpart": ("not", "BinaryOp"),
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
                "counterpart": ("Operator operator", "BooleanOperator"),
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
