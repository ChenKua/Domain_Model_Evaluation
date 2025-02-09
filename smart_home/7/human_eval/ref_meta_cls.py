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
        "score": 1,
        "type": "enum",
        "dsl": "RuleStatus (created, edited, activated, deactivated )",
        "counterpart": "Status",
        "attributes": {
            "created": {"score": 1, "counterpart": ("Created", "Status")},
            "edited": {"score": 1, "counterpart": ("Edited", "Status")},
            "activated": {"score": 1, "counterpart": ("Activated", "Status")},
            "deactivated": {"score": 1, "counterpart": ("Deactivated", "Status")},
        },
    },
    "BinaryOp": {
        "score": 1,
        "type": "enum",
        "dsl": "BinaryOp (AND, OR )",
        "counterpart": "OperatorType",
        "attributes": {
            "AND": {"score": 1, "counterpart": ("AND", "OperatorType")},
            "OR": {"score": 1, "counterpart": ("OR", "OperatorType")},
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
        "counterpart": "Owner",
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
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract Device(DeviceStatus deviceStatus, int deviceID)",
        "counterpart": "Device",
        "attributes": {
            "DeviceStatus deviceStatus": {
                "score": 0.5,
                "counterpart": ("Boolean active", "Device"),
            },
            "int deviceID": {
                "score": 1,
                "counterpart": ("String identifier", "Device"),
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
                "counterpart": ("Time timeStamp", "ControlCommand"),
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
                "counterpart": ("Double measureValue", "SensorReading"),
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
                "counterpart": ("String command", "ControlCommand"),
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
                "score": 1,
                "counterpart": ("Status status", "AutomationRule"),
            }
        },
    },
    "abstract BooleanExpression": {
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract BooleanExpression()",
        "counterpart": "Precondition()",
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
        "counterpart": ("NOT", "OperatorType"),
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
                "counterpart": ("OperatorType operatorType", "BooleanOperator"),
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
