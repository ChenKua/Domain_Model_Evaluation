{
    "Command": {
        "score": 1,
        "type": "enum",
        "dsl": "Command(lockDoor,turnOnHeating,turnOnLight)",
        "counterpart": "CommandType",
        "attributes": {
            "lockDoor": {"score": 1, "counterpart": ("lockDoor", "CommandType")},
            "turnOnHeating": {
                "score": 1,
                "counterpart": ("turnOnHeating", "CommandType"),
            },
            "turnOnLight": {"score": 0, "counterpart": None},
        },
    },
    "ActuatorStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "ActuatorStatus(requested, completed, failed)",
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
        "dsl": "RuleStatus(created, edited, activated, deactivated)",
        "counterpart": "RuleStatus",
        "attributes": {
            "created": {"score": 1, "counterpart": ("created", "RuleStatus")},
            "edited": {"score": 1, "counterpart": ("edited", "RuleStatus")},
            "activated": {"score": 1, "counterpart": ("activated", "RuleStatus")},
            "deactivated": {"score": 1, "counterpart": ("deactivated", "RuleStatus")},
        },
    },
    "BooleanExpression": {
        "score": 1,
        "type": "enum",
        "dsl": "BooleanExpression(AND,OR, NOT)",
        "counterpart": "BinaryOp",
        "attributes": {
            "AND": {"score": 1, "counterpart": ("AND", "BinaryOp")},
            "OR": {"score": 1, "counterpart": ("OR", "BinaryOp")},
            "NOT": {"score": 0.5, "counterpart": (None, "NotExpression")},
        },
    },
    "SensorType": {
        "score": 0,
        "type": "enum",
        "dsl": "SensorType (temperatureSensor,movementSensor)",
        "counterpart": None,
        "attributes": {
            "temperatureSensor": {"score": 0, "counterpart": None},
            "movementSensor": {"score": 0, "counterpart": None},
        },
    },
    "ActuatorType": {
        "score": 0,
        "type": "enum",
        "dsl": "ActuatorType (lightController,lockController)",
        "counterpart": None,
        "attributes": {
            "lightController": {"score": 0, "counterpart": None},
            "lockController": {"score": 0, "counterpart": None},
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
        "dsl": "SmartHome( String address)",
        "counterpart": "SmartHome",
        "attributes": {
            "String address": {"score": 0.5, "counterpart": ("string city", "Address")}
        },
    },
    "Owner": {
        "score": 1,
        "type": "regular",
        "dsl": "Owner( String name)",
        "counterpart": "User",
        "attributes": {
            "String name": {"score": 1, "counterpart": ("string name", "User")}
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
        "dsl": "abstract Device( unique int id, boolean isActivated)",
        "counterpart": "abstract Device",
        "attributes": {
            "unique int id": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
            "boolean isActivated": {
                "score": 0.5,
                "counterpart": ("Activated", "DeviceStatus"),
            },
        },
    },
    "Sensor": {
        "score": 1,
        "type": "regular",
        "dsl": "Sensor( SensorType type)",
        "counterpart": "SensorDevice",
        "attributes": {"SensorType type": {"score": 0, "counterpart": None}},
    },
    "Actuator": {
        "score": 1,
        "type": "regular",
        "dsl": "Actuator( ActuatorType type)",
        "counterpart": "ActuatorDevice",
        "attributes": {"ActuatorType type": {"score": 0, "counterpart": None}},
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
        "dsl": "SensorReading( int measuredValue, Time timeStamp)",
        "counterpart": "SensorReading",
        "attributes": {
            "int measuredValue": {
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
        "dsl": "ControlCommand( Command command, Time timeStamp, ActuatorStatus status)",
        "counterpart": "ControlCommand",
        "attributes": {
            "Command command": {
                "score": 1,
                "counterpart": ("CommandType commandType", "ControlCommand"),
            },
            "Time timeStamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
            "ActuatorStatus status": {
                "score": 1,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            },
        },
    },
    "AutomationRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AutomationRule( RuleStatus status, Time timeStamp, boolean triggered)",
        "counterpart": "AlertRule",
        "attributes": {
            "RuleStatus status": {
                "score": 1,
                "counterpart": ("RuleStatus ruleStatus", "AlertRule"),
            },
            "Time timeStamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
            "boolean triggered": {"score": 0, "counterpart": None},
        },
    },
    "PreCondition": {
        "score": 0.5,
        "type": "regular",
        "dsl": "PreCondition()",
        "counterpart": "abstract BooleanExpression",
        "attributes": {},
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
    "RelevantAlert": {
        "score": 0,
        "type": "regular",
        "dsl": "RelevantAlert()",
        "counterpart": None,
        "attributes": {},
    },
}
