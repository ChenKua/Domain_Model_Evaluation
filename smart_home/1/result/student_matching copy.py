{
    "Status": {
        "score": 1,
        "type": "enum",
        "dsl": "Status (Requested, Completed, Failed)",
        "counterpart": "RuleStatus",
        "attributes": {
            "Requested": {"score": 0.5, "counterpart": ["Requested", "CommandStatus"]},
            "Completed": {"score": 0.5, "counterpart": ["Completed", "CommandStatus"]},
            "Failed": {"score": 0.5, "counterpart": ["Failed", "CommandStatus"]},
        },
    },
    "Operator": {
        "score": 1,
        "type": "enum",
        "dsl": "Operator (and, or, not)",
        "counterpart": "BinaryOp",
        "attributes": {
            "and": {"score": 1, "counterpart": ["AND", "BinaryOp"]},
            "or": {"score": 1, "counterpart": ["OR", "BinaryOp"]},
            "not": {"score": 0, "counterpart": null},
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
        "dsl": "SmartHome(string address)",
        "counterpart": "SmartHome",
        "attributes": {
            "string address": {"score": 0.5, "counterpart": ["string city", "Address"]}
        },
    },
    "User": {
        "score": 1,
        "type": "regular",
        "dsl": "User(boolean owner)",
        "counterpart": "User",
        "attributes": {
            "boolean owner": {"score": 1, "counterpart": ["string name", "User"]}
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
        "dsl": "abstract Device (int id)",
        "counterpart": "abstract Device",
        "attributes": {
            "int id": {"score": 1, "counterpart": ["int deviceID", "abstract Device"]}
        },
    },
    "Sensor": {
        "score": 1,
        "type": "regular",
        "dsl": "Sensor()",
        "counterpart": "SensorDevice",
        "attributes": {},
    },
    "Actuator": {
        "score": 1,
        "type": "regular",
        "dsl": "Actuator()",
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
    "abstract Dependency": {
        "score": 1,
        "type": "abstract",
        "dsl": "abstract Dependency ()",
        "counterpart": "abstract RuntimeElement",
        "attributes": {},
    },
    "SensorReading": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorReading(int measuredValue, DateTime timestamp)",
        "counterpart": "SensorReading",
        "attributes": {
            "int measuredValue": {
                "score": 1,
                "counterpart": ["double value", "SensorReading"],
            },
            "DateTime timestamp": {"score": 0, "counterpart": null},
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand(Status status)",
        "counterpart": "ControlCommand",
        "attributes": {
            "Status status": {
                "score": 1,
                "counterpart": ["CommandStatus commandStatus", "ControlCommand"],
            }
        },
    },
    "AutomationRule": {
        "score": 0,
        "type": "regular",
        "dsl": "AutomationRule(boolean activated)",
        "counterpart": null,
        "attributes": {
            "boolean activated": {
                "score": 0.5,
                "counterpart": ["activated", "RuleStatus"],
            }
        },
    },
    "Precondition": {
        "score": 1,
        "type": "regular",
        "dsl": "Precondition()",
        "counterpart": "NotExpression",
        "attributes": {},
    },
    "RelationalTerm": {
        "score": 1,
        "type": "regular",
        "dsl": "RelationalTerm()",
        "counterpart": "RelationalTerm",
        "attributes": {},
    },
    "TriggeredAutomationRule": {
        "score": 1,
        "type": "regular",
        "dsl": "TriggeredAutomationRule(DateTime timestamp)",
        "counterpart": "AlertRule",
        "attributes": {
            "DateTime timestamp": {
                "score": 0.5,
                "counterpart": ["time timestamp", "abstract RuntimeElement"],
            }
        },
    },
    "BooleanOperator": {
        "score": 0.5,
        "type": "regular",
        "dsl": "BooleanOperator(Operator operator)",
        "counterpart": "abstract BooleanExpression",
        "attributes": {"Operator operator": {"score": 0, "counterpart": null}},
    },
    "Action": {
        "score": 1,
        "type": "regular",
        "dsl": "Action()",
        "counterpart": "CommandSequence",
        "attributes": {},
    },
    "AtomicRelationalTerm": {
        "score": 1,
        "type": "regular",
        "dsl": "AtomicRelationalTerm()",
        "counterpart": "BinaryExpression",
        "attributes": {},
    },
}
