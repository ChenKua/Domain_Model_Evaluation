{
    "Status": {
        "score": 1,
        "type": "enum",
        "dsl": "Status( Requested, Completed, Failed )",
        "counterpart": "CommandStatus",
        "attributes": {
            "Requested": {"score": 1, "counterpart": ("Requested", "CommandStatus")},
            "Completed": {"score": 1, "counterpart": ("Completed", "CommandStatus")},
            "Failed": {"score": 1, "counterpart": ("Failed", "CommandStatus")},
        },
    },
    "Operator": {
        "score": 1,
        "type": "enum",
        "dsl": "Operator(AND, OR, NOT)",
        "counterpart": "BinaryOp",
        "attributes": {
            "AND": {"score": 1, "counterpart": ("AND", "BinaryOp")},
            "OR": {"score": 1, "counterpart": ("OR", "BinaryOp")},
            "NOT": {"score": 0.5, "counterpart": (None, "NotExpression")},
        },
    },
    "comparisson": {
        "score": 0,
        "type": "enum",
        "dsl": "comparisson ( LessThan, GreaterThan, Equals )",
        "counterpart": None,
        "attributes": {
            "LessThan": {"score": 0, "counterpart": None},
            "GreaterThan": {"score": 0, "counterpart": None},
            "Equals": {"score": 0, "counterpart": None},
        },
    },
    "SmartHome": {
        "score": 1,
        "type": "regular",
        "dsl": "SmartHome ( String address)",
        "counterpart": "SmartHome",
        "attributes": {
            "String address": {"score": 0.5, "counterpart": ("string city", "Address")}
        },
    },
    "Room": {
        "score": 1,
        "type": "regular",
        "dsl": "Room ()",
        "counterpart": "Room",
        "attributes": {},
    },
    "RoomElement": {
        "score": 0.5,
        "type": "regular",
        "dsl": "RoomElement( boolean active, String id)",
        "counterpart": "abstract Device",
        "attributes": {
            "boolean active": {
                "score": 0.5,
                "counterpart": ("DeviceStatus deviceStatus", "abstract Device"),
            },
            "String id": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
        },
    },
    "Sensor": {
        "score": 1,
        "type": "regular",
        "dsl": "Sensor( double value)",
        "counterpart": "SensorDevice",
        "attributes": {
            "double value": {
                "score": 0,
                "counterpart": None,
            }
        },
    },
    "Actuator": {
        "score": 1,
        "type": "regular",
        "dsl": "Actuator()",
        "counterpart": "ActuatorDevice",
        "attributes": {},
    },
    "Activity": {
        "score": 1,
        "type": "regular",
        "dsl": "Activity( String timestamp)",
        "counterpart": "ActivityLog",
        "attributes": {
            "String timestamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            }
        },
    },
    "Reading": {
        "score": 1,
        "type": "regular",
        "dsl": "Reading ( double value)",
        "counterpart": "SensorReading",
        "attributes": {
            "double value": {
                "score": 1,
                "counterpart": ("double value", "SensorReading"),
            }
        },
    },
    "Command": {
        "score": 1,
        "type": "regular",
        "dsl": "Command( String command)",
        "counterpart": "ControlCommand",
        "attributes": {
            "String command": {
                "score": 0.5,
                "counterpart": ("CommandType commandType", "ControlCommand"),
            }
        },
    },
    "Rule": {
        "score": 1,
        "type": "regular",
        "dsl": "Rule( boolean active)",
        "counterpart": "AlertRule",
        "attributes": {
            "boolean active": {
                "score": 0.5,
                "counterpart": ("RuleStatus ruleStatus", "AlertRule"),
            }
        },
    },
    "RuleElement": {
        "score": 0.5,
        "type": "regular",
        "dsl": "RuleElement()",
        "counterpart": "abstract BooleanExpression",
        "attributes": {},
    },
    "RelationalTerm": {
        "score": 1,
        "type": "regular",
        "dsl": "RelationalTerm()",
        "counterpart": "RelationalTerm",
        "attributes": {},
    },
    "BooleanOperator": {
        "score": 1,
        "type": "regular",
        "dsl": "BooleanOperator()",
        "counterpart": "BinaryExpression",
        "attributes": {},
    },
    "Action": {
        "score": 1,
        "type": "regular",
        "dsl": "Action( String command)",
        "counterpart": "CommandSequence",
        "attributes": {
            "String command": {
                "score": 0.5,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            }
        },
    },
    "RuleTrigger": {
        "score": 0,
        "type": "regular",
        "dsl": "RuleTrigger()",
        "counterpart": None,
        "attributes": {},
    },
    "SensorCheck": {
        "score": 0,
        "type": "regular",
        "dsl": "SensorCheck( double target)",
        "counterpart": None,
        "attributes": {"double target": {"score": 0, "counterpart": None}},
    },
    "ActiveCheck": {
        "score": 0,
        "type": "regular",
        "dsl": "ActiveCheck ()",
        "counterpart": None,
        "attributes": {},
    },
}
