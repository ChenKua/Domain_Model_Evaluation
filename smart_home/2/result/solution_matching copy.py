{
    "DeviceStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "DeviceStatus(Activated, Deactivated)",
        "counterpart": "DeviceStatus",
        "attributes": {
            "Activated": {"score": 1, "counterpart": ["Activated", "DeviceStatus"]},
            "Deactivated": {"score": 1, "counterpart": ["Deactivated", "DeviceStatus"]},
        },
    },
    "CommandType": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandType (lockDoor, turnOnHeating)",
        "counterpart": "ControlCommand",
        "attributes": {
            "lockDoor": {"score": 1, "counterpart": ["LockDoor", "ControlCommand"]},
            "turnOnHeating": {
                "score": 1,
                "counterpart": ["TurnOnHeating", "ControlCommand"],
            },
        },
    },
    "CommandStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandStatus (Requested, Completed, Failed)",
        "counterpart": "Status",
        "attributes": {
            "Requested": {"score": 1, "counterpart": ["Requested", "Status"]},
            "Completed": {"score": 1, "counterpart": ["Completed", "Status"]},
            "Failed": {"score": 1, "counterpart": ["Failed", "Status"]},
        },
    },
    "RuleStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "RuleStatus (created, edited, activated, deactivated )",
        "counterpart": "RuleStatus",
        "attributes": {
            "created": {"score": 1, "counterpart": ["Created", "RuleStatus"]},
            "edited": {"score": 1, "counterpart": ["Edited", "RuleStatus"]},
            "activated": {"score": 1, "counterpart": ["Activated", "RuleStatus"]},
            "deactivated": {"score": 1, "counterpart": ["Deactivated", "RuleStatus"]},
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
            "string name": {
                "score": 0.5,
                "counterpart": ["String word", "SeparationWord"],
            }
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
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract Device(DeviceStatus deviceStatus, int deviceID)",
        "counterpart": "Device",
        "attributes": {
            "DeviceStatus deviceStatus": {
                "score": 0.5,
                "counterpart": ["DeviceStatus deviceStatus", "ChangeInState"],
            },
            "int deviceID": {
                "score": 1,
                "counterpart": ["string deviceIdentifier", "Device"],
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
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract RuntimeElement(time timestamp)",
        "counterpart": "TypeOfSensor",
        "attributes": {
            "time timestamp": {
                "score": 0.5,
                "counterpart": ["Time timeStamp", "AutomationRule"],
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
                "counterpart": ["float measuredValue", "SensorReading"],
            }
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand (CommandType commandType, CommandStatus commandStatus)",
        "counterpart": "Action",
        "attributes": {
            "CommandType commandType": {
                "score": 0.5,
                "counterpart": ["ControlCommand controlCommand", "ActuatorCommand"],
            },
            "CommandStatus commandStatus": {
                "score": 0.5,
                "counterpart": ["Status status", "ActuatorCommand"],
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
                "counterpart": ["RuleStatus ruleStatus", "AutomationRule"],
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
        "score": 0,
        "type": "regular",
        "dsl": "NotExpression()",
        "counterpart": null,
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
        "counterpart": "ActuatorCommand",
        "attributes": {},
    },
}
