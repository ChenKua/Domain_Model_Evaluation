{
    "Status": {
        "score": 1,
        "type": "enum",
        "dsl": "Status (Created, Edited, Activated, Deactivated)",
        "counterpart": "RuleStatus",
        "attributes": {
            "Created": {"score": 1, "counterpart": ("created", "RuleStatus")},
            "Edited": {"score": 1, "counterpart": ("edited", "RuleStatus")},
            "Activated": {"score": 1, "counterpart": ("activated", "RuleStatus")},
            "Deactivated": {"score": 1, "counterpart": ("deactivated", "RuleStatus")},
        },
    },
    "OperatorType": {
        "score": 1,
        "type": "enum",
        "dsl": "OperatorType ( AND, NOT, OR)",
        "counterpart": "BinaryOp",
        "attributes": {
            "AND": {"score": 1, "counterpart": ("AND", "BinaryOp")},
            "NOT": {"score": 0.5, "counterpart": (None, "NotExpression")},
            "OR": {"score": 1, "counterpart": ("OR", "BinaryOp")},
        },
    },
    "TermType": {
        "score": 0,
        "type": "enum",
        "dsl": "TermType ( Rooms, Sensors, Actuators, SensorReadings, ControlCommands)",
        "counterpart": None,
        "attributes": {
            "Rooms": {"score": 0, "counterpart": None},
            "Sensors": {"score": 0, "counterpart": None},
            "Actuators": {"score": 0, "counterpart": None},
            "SensorReadings": {"score": 0, "counterpart": None},
            "ControlCommands": {"score": 0, "counterpart": None},
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
        "dsl": "SmartHome( address)",
        "counterpart": "SmartHome",
        "attributes": {"address": {"score": 0.5, "counterpart": (None, "Address")}},
    },
    "Owner": {
        "score": 1,
        "type": "regular",
        "dsl": "Owner()",
        "counterpart": "User",
        "attributes": {},
    },
    "Room": {
        "score": 1,
        "type": "regular",
        "dsl": "Room()",
        "counterpart": "Room",
        "attributes": {},
    },
    "Device": {
        "score": 0.5,
        "type": "regular",
        "dsl": "Device( String identifier, Boolean active)",
        "counterpart": "abstract Device",
        "attributes": {
            "String identifier": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
            "Boolean active": {
                "score": 0.5,
                "counterpart": ("DeviceStatus deviceStatus", "abstract Device"),
            },
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
    "SensorReading": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorReading( Double measureValue, Time timeStamp)",
        "counterpart": "SensorReading",
        "attributes": {
            "Double measureValue": {
                "score": 1,
                "counterpart": ("double value", "SensorReading"),
            },
            "Time timeStamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand( String status, Time timeStamp, String command)",
        "counterpart": "ControlCommand",
        "attributes": {
            "String status": {
                "score": 1,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            },
            "Time timeStamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
            "String command": {
                "score": 1,
                "counterpart": ("CommandType commandType", "ControlCommand"),
            },
        },
    },
    "AutomationRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AutomationRule( Status status)",
        "counterpart": "AlertRule",
        "attributes": {
            "Status status": {
                "score": 1,
                "counterpart": ("RuleStatus ruleStatus", "AlertRule"),
            }
        },
    },
    "Precondition": {
        "score": 1,
        "type": "regular",
        "dsl": "Precondition()",
        "counterpart": "abstract BooleanExpression",
        "attributes": {},
    },
    "RelationalTerm": {
        "score": 1,
        "type": "regular",
        "dsl": "RelationalTerm( TermType termType)",
        "counterpart": "RelationalTerm",
        "attributes": {"TermType termType": {"score": 0, "counterpart": None}},
    },
    "BooleanOperator": {
        "score": 0.5,
        "type": "regular",
        "dsl": "BooleanOperator( OperatorType operatorType)",
        "counterpart": "BinaryExpression",
        "attributes": {
            "OperatorType operatorType": {
                "score": 1,
                "counterpart": ("BinaryOp binaryOp", "BinaryExpression"),
            }
        },
    },
    "Action": {
        "score": 1,
        "type": "regular",
        "dsl": "Action()",
        "counterpart": "CommandSequence",
        "attributes": {},
    },
}
