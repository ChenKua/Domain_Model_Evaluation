{
    "ControllerStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "ControllerStatus (Requested, Completed, Failed)",
        "counterpart": "CommandStatus",
        "attributes": {
            "Requested": {"score": 1, "counterpart": ("Requested", "CommandStatus")},
            "Completed": {"score": 1, "counterpart": ("Completed", "CommandStatus")},
            "Failed": {"score": 1, "counterpart": ("Failed", "CommandStatus")},
        },
    },
    "BooleanOperator": {
        "score": 1,
        "type": "enum",
        "dsl": "BooleanOperator (AND, OR, NOT)",
        "counterpart": "BinaryOp",
        "attributes": {
            "AND": {"score": 1, "counterpart": ("AND", "BinaryOp")},
            "OR": {"score": 1, "counterpart": ("OR", "BinaryOp")},
            "NOT": {"score": 0.5, "counterpart": (None, "NotExpression")},
        },
    },
    "Status": {
        "score": 1,
        "type": "enum",
        "dsl": "Status (ON, OFF)",
        "counterpart": "DeviceStatus",
        "attributes": {
            "ON": {"score": 1, "counterpart": ("Activated", "DeviceStatus")},
            "OFF": {"score": 1, "counterpart": ("Deactivated", "DeviceStatus")},
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
    "Room": {
        "score": 1,
        "type": "regular",
        "dsl": "Room( name)",
        "counterpart": "Room",
        "attributes": {"name": {"score": 0.5, "counterpart": ("string name", "User")}},
    },
    "abstract Device": {
        "score": 1,
        "type": "abstract",
        "dsl": "abstract Device(  Integer uDI, Date timestamp)",
        "counterpart": "abstract Device",
        "attributes": {
            "Integer uDI": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
            "Date timestamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
        },
    },
    "Sensor": {
        "score": 1,
        "type": "regular",
        "dsl": "Sensor( Integer reading)",
        "counterpart": "SensorDevice",
        "attributes": {
            "Integer reading": {"score": 0.5, "counterpart": (None, "SensorReading")}
        },
    },
    "Controller": {
        "score": 1,
        "type": "regular",
        "dsl": "Controller()",
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
    "Command": {
        "score": 1,
        "type": "regular",
        "dsl": "Command( ControllerStatus status)",
        "counterpart": "ControlCommand",
        "attributes": {
            "ControllerStatus status": {
                "score": 1,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            }
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
        "score": 0.5,
        "type": "regular",
        "dsl": "Precondition()",
        "counterpart": "abstract BooleanExpression",
        "attributes": {},
    },
    "abstract RelationalTerm": {
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract RelationalTerm( )",
        "counterpart": "RelationalTerm",
        "attributes": {},
    },
    "Operator": {
        "score": 1,
        "type": "regular",
        "dsl": "Operator( BooleanOperator operator)",
        "counterpart": "BinaryExpression",
        "attributes": {
            "BooleanOperator operator": {
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
    "InfrastructureMap": {
        "score": 0,
        "type": "regular",
        "dsl": "InfrastructureMap()",
        "counterpart": None,
        "attributes": {},
    },
}
