{
    "ActionStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "ActionStatus ( requested, completed, failed)",
        "counterpart": "CommandStatus",
        "attributes": {
            "requested": {"score": 1, "counterpart": ("Requested", "CommandStatus")},
            "completed": {"score": 1, "counterpart": ("Completed", "CommandStatus")},
            "failed": {"score": 1, "counterpart": ("Failed", "CommandStatus")},
        },
    },
    "RuleStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "RuleStatus (created, edited,activated, deactivated )",
        "counterpart": "RuleStatus",
        "attributes": {
            "created": {"score": 1, "counterpart": ("created", "RuleStatus")},
            "edited": {"score": 1, "counterpart": ("edited", "RuleStatus")},
            "activated": {"score": 1, "counterpart": ("activated", "RuleStatus")},
            "deactivated": {"score": 1, "counterpart": ("deactivated", "RuleStatus")},
        },
    },
    "SHAS": {
        "score": 1,
        "type": "regular",
        "dsl": "SHAS()",
        "counterpart": "SHAS",
        "attributes": {},
    },
    "User": {
        "score": 1,
        "type": "regular",
        "dsl": "User()",
        "counterpart": "User",
        "attributes": {},
    },
    "Address": {
        "score": 1,
        "type": "regular",
        "dsl": "Address()",
        "counterpart": "Address",
        "attributes": {},
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
        "dsl": "abstract Device( Integer uniqueId, Boolean activated, type)",
        "counterpart": "abstract Device",
        "attributes": {
            "Integer uniqueId": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
            "Boolean activated": {
                "score": 0.5,
                "counterpart": ("DeviceStatus deviceStatus", "abstract Device"),
            },
            "type": {"score": 0.5, "counterpart": (None, "CommandType")},
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
        "dsl": "SensorReading( Integer measuredValue)",
        "counterpart": "SensorReading",
        "attributes": {
            "Integer measuredValue": {
                "score": 1,
                "counterpart": ("double value", "SensorReading"),
            }
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand( commandType)",
        "counterpart": "ControlCommand",
        "attributes": {
            "commandType": {
                "score": 1,
                "counterpart": ("CommandType commandType", "ControlCommand"),
            }
        },
    },
    "AutomationRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AutomationRule( RuleStatus rule, Boolean precondition)",
        "counterpart": ("AlertRule"),
        "attributes": {
            "RuleStatus rule": {
                "score": 1,
                "counterpart": ("RuleStatus ruleStatus", "AlertRule"),
            },
            "Boolean precondition": {
                "score": 0.5,
                "counterpart": (None, "abstract BooleanExpression"),
            },
        },
    },
    "Action": {
        "score": 1,
        "type": "regular",
        "dsl": "Action( ActionStatus status)",
        "counterpart": "CommandSequence",
        "attributes": {
            "ActionStatus status": {
                "score": 0.5,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            }
        },
    },
    "Alert": {
        "score": 0,
        "type": "regular",
        "dsl": "Alert()",
        "counterpart": None,
        "attributes": {},
    },
    "TimeStamp": {
        "score": 0.5,
        "type": "regular",
        "dsl": "TimeStamp()",
        "counterpart": ("time timestamp", "abstract RuntimeElement"),
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
