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
        "score": 1,
        "type": "enum",
        "dsl": "CommandType (lockDoor, turnOnHeating)",
        "counterpart": "CommandType",
        "attributes": {
            "lockDoor": {"score": 1, "counterpart": ["lockDoor", "CommandType"]},
            "turnOnHeating": {
                "score": 1,
                "counterpart": ["turnOnHeating", "CommandType"],
            },
        },
    },
    "CommandStatus": {
        "score": 0,
        "type": "enum",
        "dsl": "CommandStatus (Requested, Completed, Failed)",
        "counterpart": null,
        "attributes": {
            "Requested": {"score": 0.5, "counterpart": ["requested", "Status"]},
            "Completed": {"score": 0.5, "counterpart": ["completed", "Status"]},
            "Failed": {"score": 0.5, "counterpart": ["failed", "Status"]},
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
            "activated": {"score": 0, "counterpart": null},
            "deactivated": {"score": 0, "counterpart": null},
        },
    },
    "BinaryOp": {
        "score": 1,
        "type": "enum",
        "dsl": "BinaryOp (AND, OR )",
        "counterpart": "Operator",
        "attributes": {
            "AND": {"score": 1, "counterpart": ["AND", "Operator"]},
            "OR": {"score": 1, "counterpart": ["OR", "Operator"]},
        },
    },
    "SHAS": {
        "score": 0,
        "type": "regular",
        "dsl": "SHAS()",
        "counterpart": null,
        "attributes": {},
    },
    "SmartHome": {
        "score": 1,
        "type": "regular",
        "dsl": "SmartHome()",
        "counterpart": "Home",
        "attributes": {},
    },
    "User": {
        "score": 1,
        "type": "regular",
        "dsl": "User(string name)",
        "counterpart": "User",
        "attributes": {
            "string name": {"score": 1, "counterpart": ["string user", "User"]}
        },
    },
    "Address": {
        "score": 0,
        "type": "regular",
        "dsl": "Address(string city, string postalCode, string street, string aptNumber)",
        "counterpart": null,
        "attributes": {
            "string city": {"score": 0.5, "counterpart": ["string password", "User"]},
            "string postalCode": {
                "score": 0.5,
                "counterpart": ["string address", "Home"],
            },
            "string street": {
                "score": 0.5,
                "counterpart": ["string singleton", "Home"],
            },
            "string aptNumber": {"score": 0.5, "counterpart": ["string name", "Room"]},
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
            "DeviceStatus deviceStatus": {"score": 0, "counterpart": null},
            "int deviceID": {"score": 1, "counterpart": ["int uid", "Device"]},
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
        "counterpart": null,
        "attributes": {
            "time timestamp": {
                "score": 0.5,
                "counterpart": ["Time timeStamp", "Command"],
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
                "counterpart": ["double reading", "SensorReading"],
            }
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand (CommandType commandType, CommandStatus commandStatus)",
        "counterpart": "Command",
        "attributes": {
            "CommandType commandType": {
                "score": 1,
                "counterpart": ["commandType type", "Command"],
            },
            "CommandStatus commandStatus": {
                "score": 1,
                "counterpart": ["Status status", "Command"],
            },
        },
    },
    "AlertRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AlertRule (RuleStatus ruleStatus)",
        "counterpart": "AutomationRule",
        "attributes": {"RuleStatus ruleStatus": {"score": 0, "counterpart": null}},
    },
    "abstract BooleanExpression": {
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract BooleanExpression()",
        "counterpart": "ComposedRelation",
        "attributes": {},
    },
    "RelationalTerm": {
        "score": 1,
        "type": "regular",
        "dsl": "RelationalTerm()",
        "counterpart": "AtomicRelation",
        "attributes": {},
    },
    "NotExpression": {
        "score": 0.5,
        "type": "regular",
        "dsl": "NotExpression()",
        "counterpart": ["NOT", "Operator"],
        "attributes": {},
    },
    "BinaryExpression": {
        "score": 0,
        "type": "regular",
        "dsl": "BinaryExpression(BinaryOp binaryOp)",
        "counterpart": null,
        "attributes": {"BinaryOp binaryOp": {"score": 0, "counterpart": null}},
    },
    "CommandSequence": {
        "score": 0,
        "type": "regular",
        "dsl": "CommandSequence()",
        "counterpart": null,
        "attributes": {},
    },
}
