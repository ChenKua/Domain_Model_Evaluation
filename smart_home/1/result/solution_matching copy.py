{
    "DeviceStatus": {
        "score": 0,
        "type": "enum",
        "dsl": "DeviceStatus(Activated, Deactivated)",
        "counterpart": null,
        "attributes": {
            "Activated": {"score": 0, "counterpart": null},
            "Deactivated": {"score": 0, "counterpart": null},
        },
    },
    "CommandType": {
        "score": 0,
        "type": "enum",
        "dsl": "CommandType (lockDoor, turnOnHeating)",
        "counterpart": null,
        "attributes": {
            "lockDoor": {"score": 0, "counterpart": null},
            "turnOnHeating": {"score": 0, "counterpart": null},
        },
    },
    "CommandStatus": {
        "score": 0,
        "type": "enum",
        "dsl": "CommandStatus (Requested, Completed, Failed)",
        "counterpart": null,
        "attributes": {
            "Requested": {"score": 0.5, "counterpart": ["Requested", "Status"]},
            "Completed": {"score": 0.5, "counterpart": ["Completed", "Status"]},
            "Failed": {"score": 0.5, "counterpart": ["Failed", "Status"]},
        },
    },
    "RuleStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "RuleStatus (created, edited, activated, deactivated )",
        "counterpart": "Status",
        "attributes": {
            "created": {"score": 0, "counterpart": null},
            "edited": {"score": 0, "counterpart": null},
            "activated": {
                "score": 0.5,
                "counterpart": ["boolean activated", "AutomationRule"],
            },
            "deactivated": {"score": 0, "counterpart": null},
        },
    },
    "BinaryOp": {
        "score": 1,
        "type": "enum",
        "dsl": "BinaryOp (AND, OR )",
        "counterpart": "Operator",
        "attributes": {
            "AND": {"score": 1, "counterpart": ["and", "Operator"]},
            "OR": {"score": 1, "counterpart": ["or", "Operator"]},
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
            "string name": {"score": 1, "counterpart": ["boolean owner", "User"]}
        },
    },
    "Address": {
        "score": 0,
        "type": "regular",
        "dsl": "Address(string city, string postalCode, string street, string aptNumber)",
        "counterpart": null,
        "attributes": {
            "string city": {
                "score": 0.5,
                "counterpart": ["string address", "SmartHome"],
            },
            "string postalCode": {"score": 0, "counterpart": null},
            "string street": {"score": 0, "counterpart": null},
            "string aptNumber": {"score": 0, "counterpart": null},
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
            "DeviceStatus deviceStatus": {"score": 0, "counterpart": null},
            "int deviceID": {"score": 1, "counterpart": ["int id", "abstract Device"]},
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
                "counterpart": ["DateTime timestamp", "TriggeredAutomationRule"],
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
                "counterpart": ["int measuredValue", "SensorReading"],
            }
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand (CommandType commandType, CommandStatus commandStatus)",
        "counterpart": "ControlCommand",
        "attributes": {
            "CommandType commandType": {"score": 0, "counterpart": null},
            "CommandStatus commandStatus": {
                "score": 1,
                "counterpart": ["Status status", "ControlCommand"],
            },
        },
    },
    "AlertRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AlertRule (RuleStatus ruleStatus)",
        "counterpart": "TriggeredAutomationRule",
        "attributes": {"RuleStatus ruleStatus": {"score": 0, "counterpart": null}},
    },
    "abstract BooleanExpression": {
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract BooleanExpression()",
        "counterpart": "BooleanOperator",
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
        "score": 1,
        "type": "regular",
        "dsl": "NotExpression()",
        "counterpart": "Precondition",
        "attributes": {},
    },
    "BinaryExpression": {
        "score": 1,
        "type": "regular",
        "dsl": "BinaryExpression(BinaryOp binaryOp)",
        "counterpart": "AtomicRelationalTerm",
        "attributes": {"BinaryOp binaryOp": {"score": 0, "counterpart": null}},
    },
    "CommandSequence": {
        "score": 1,
        "type": "regular",
        "dsl": "CommandSequence()",
        "counterpart": "Action",
        "attributes": {},
    },
}
