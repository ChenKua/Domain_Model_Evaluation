{
    "DeviceStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "DeviceStatus(Activated, Deactivated)",
        "counterpart": "DeviceState",
        "attributes": {
            "Activated": {"score": 1, "counterpart": ["activated", "DeviceState"]},
            "Deactivated": {"score": 1, "counterpart": ["deactivated", "DeviceState"]},
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
        "score": 1,
        "type": "enum",
        "dsl": "CommandStatus (Requested, Completed, Failed)",
        "counterpart": "CommandStatus",
        "attributes": {
            "Requested": {"score": 1, "counterpart": ["requested", "CommandStatus"]},
            "Completed": {"score": 1, "counterpart": ["completed", "CommandStatus"]},
            "Failed": {"score": 1, "counterpart": ["failed", "CommandStatus"]},
        },
    },
    "RuleStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "RuleStatus (created, edited, activated, deactivated )",
        "counterpart": "State",
        "attributes": {
            "created": {"score": 0, "counterpart": null},
            "edited": {"score": 0, "counterpart": null},
            "activated": {"score": 1, "counterpart": ["activated", "State"]},
            "deactivated": {"score": 1, "counterpart": ["deactivated", "State"]},
        },
    },
    "BinaryOp": {
        "score": 1,
        "type": "enum",
        "dsl": "BinaryOp (AND, OR )",
        "counterpart": "BooleanOps",
        "attributes": {
            "AND": {"score": 1, "counterpart": ["AND", "BooleanOps"]},
            "OR": {"score": 1, "counterpart": ["OR", "BooleanOps"]},
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
        "attributes": {"string name": {"score": 0, "counterpart": null}},
    },
    "Address": {
        "score": 1,
        "type": "regular",
        "dsl": "Address(string city, string postalCode, string street, string aptNumber)",
        "counterpart": "Address",
        "attributes": {
            "string city": {"score": 1, "counterpart": ["string city", "Address"]},
            "string postalCode": {
                "score": 1,
                "counterpart": ["int postalCode", "Address"],
            },
            "string street": {"score": 1, "counterpart": ["string street", "Address"]},
            "string aptNumber": {
                "score": 1,
                "counterpart": ["string country", "Address"],
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
                "counterpart": ["DeviceState state", "abstract Device"],
            },
            "int deviceID": {
                "score": 1,
                "counterpart": ["int deviceID", "abstract Device"],
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
        "counterpart": null,
        "attributes": {
            "time timestamp": {
                "score": 0.5,
                "counterpart": ["Time timeStamp", "ControlCommand"],
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
                "counterpart": ["Double measuredValue", "SensorReading"],
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
                "counterpart": ["CommandType commandType", "ControlCommand"],
            },
            "CommandStatus commandStatus": {
                "score": 1,
                "counterpart": ["CommandStatus commandStatus", "ControlCommand"],
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
                "counterpart": ["State ruleState", "AutomationRule"],
            }
        },
    },
    "abstract BooleanExpression": {
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract BooleanExpression()",
        "counterpart": "BooleanRelationalTerm",
        "attributes": {},
    },
    "RelationalTerm": {
        "score": 1,
        "type": "regular",
        "dsl": "RelationalTerm()",
        "counterpart": "AtomicRelationalTerm",
        "attributes": {},
    },
    "NotExpression": {
        "score": 1,
        "type": "regular",
        "dsl": "NotExpression()",
        "counterpart": "PreCondition",
        "attributes": {},
    },
    "BinaryExpression": {
        "score": 0,
        "type": "regular",
        "dsl": "BinaryExpression(BinaryOp binaryOp)",
        "counterpart": null,
        "attributes": {
            "BinaryOp binaryOp": {
                "score": 0.5,
                "counterpart": ["BooleanOps operator", "BooleanRelationalTerm"],
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
