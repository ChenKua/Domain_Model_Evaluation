{
    "DeviceStatus": {
        "score": 0,
        "type": "enum",
        "dsl": "DeviceStatus(Activated, Deactivated)",
        "counterpart": null,
        "attributes": {
            "Activated": {
                "score": 0.5,
                "counterpart": ["boolean isActivated", "abstract Device"],
            },
            "Deactivated": {"score": 0, "counterpart": null},
        },
    },
    "CommandType": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandType (lockDoor, turnOnHeating)",
        "counterpart": "Command",
        "attributes": {
            "lockDoor": {"score": 1, "counterpart": ["lockDoor", "Command"]},
            "turnOnHeating": {"score": 1, "counterpart": ["turnOnHeating", "Command"]},
        },
    },
    "CommandStatus": {
        "score": 0,
        "type": "enum",
        "dsl": "CommandStatus (Requested, Completed, Failed)",
        "counterpart": null,
        "attributes": {
            "Requested": {"score": 0, "counterpart": null},
            "Completed": {"score": 0, "counterpart": null},
            "Failed": {"score": 0, "counterpart": null},
        },
    },
    "RuleStatus": {
        "score": 0,
        "type": "enum",
        "dsl": "RuleStatus (created, edited, activated, deactivated )",
        "counterpart": null,
        "attributes": {
            "created": {"score": 0, "counterpart": null},
            "edited": {"score": 0, "counterpart": null},
            "activated": {
                "score": 0.5,
                "counterpart": ["boolean isActivated", "AutomationRule"],
            },
            "deactivated": {"score": 0, "counterpart": null},
        },
    },
    "BinaryOp": {
        "score": 0,
        "type": "enum",
        "dsl": "BinaryOp (AND, OR )",
        "counterpart": null,
        "attributes": {
            "AND": {"score": 0, "counterpart": null},
            "OR": {"score": 0, "counterpart": null},
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
            "string name": {"score": 1, "counterpart": ["string name", "User"]}
        },
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
                "counterpart": ["string postalCode", "Address"],
            },
            "string street": {
                "score": 1,
                "counterpart": ["string province", "Address"],
            },
            "string aptNumber": {
                "score": 1,
                "counterpart": ["string streetAddress", "Address"],
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
                "counterpart": ["String status", "abstract Device"],
            },
            "int deviceID": {
                "score": 1,
                "counterpart": ["String identifier", "abstract Device"],
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
                "counterpart": ["String timeStamp", "AutomationRuleLog"],
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
                "counterpart": ["string measuredValue", "SensorReading"],
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
                "counterpart": ["Command command", "ControlCommand"],
            },
            "CommandStatus commandStatus": {
                "score": 1,
                "counterpart": ["String status", "ControlCommand"],
            },
        },
    },
    "AlertRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AlertRule (RuleStatus ruleStatus)",
        "counterpart": "AutomationRuleLog",
        "attributes": {"RuleStatus ruleStatus": {"score": 0, "counterpart": null}},
    },
    "abstract BooleanExpression": {
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract BooleanExpression()",
        "counterpart": "AutomationRule",
        "attributes": {},
    },
    "RelationalTerm": {
        "score": 0,
        "type": "regular",
        "dsl": "RelationalTerm()",
        "counterpart": null,
        "attributes": {},
    },
    "NotExpression": {
        "score": 0.5,
        "type": "regular",
        "dsl": "NotExpression()",
        "counterpart": ["boolean isTriggered", "Precondition"],
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
        "score": 1,
        "type": "regular",
        "dsl": "CommandSequence()",
        "counterpart": "Action",
        "attributes": {},
    },
}
