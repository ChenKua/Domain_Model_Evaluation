{
    "DeviceStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "DeviceStatus (Activated, Deactivated)",
        "counterpart": "DeviceStatus",
        "attributes": {
            "Activated": {"score": 1, "counterpart": ("Activated", "DeviceStatus")},
            "Deactivated": {"score": 1, "counterpart": ("Deactivated", "DeviceStatus")},
        },
    },
    "CommandStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandStatus (Requested, Completed, Failed)",
        "counterpart": "CommandStatus",
        "attributes": {
            "Requested": {"score": 1, "counterpart": ("Requested", "CommandStatus")},
            "Completed": {"score": 1, "counterpart": ("Completed", "CommandStatus")},
            "Failed": {"score": 1, "counterpart": ("Failed", "CommandStatus")},
        },
    },
    "RuleStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "RuleStatus (Activate, Deactivate)",
        "counterpart": "RuleStatus",
        "attributes": {
            "Activate": {"score": 1, "counterpart": ("activated", "RuleStatus")},
            "Deactivate": {"score": 1, "counterpart": ("Deactivate", "RuleStatus")},
        },
    },
    "DeviceType": {
        "score": 0,
        "type": "enum",
        "dsl": "DeviceType (TemperatorSensor, MovementSensor, LightController, LockController)",
        "counterpart": None,
        "attributes": {
            "TemperatorSensor": {"score": 0, "counterpart": None},
            "MovementSensor": {"score": 0, "counterpart": None},
            "LightController": {"score": 0, "counterpart": None},
            "LockController": {"score": 0, "counterpart": None},
        },
    },
    "SHASystem": {
        "score": 1,
        "type": "regular",
        "dsl": "SHASystem()",
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
    "User": {
        "score": 1,
        "type": "regular",
        "dsl": "User()",
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
    "abstract Device": {
        "score": 1,
        "type": "abstract",
        "dsl": "abstract Device( unique id, DeviceStatus deviceStatus, DeviceType deviceType)",
        "counterpart": "abstract Device",
        "attributes": {
            "unique id": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
            "DeviceStatus deviceStatus": {
                "score": 1,
                "counterpart": ("DeviceStatus deviceStatus", "abstract Device"),
            },
            "DeviceType deviceType": {
                "score": 0,
                "counterpart": None,
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
    "SensorReading": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorReading( measuredValue, Time timeStamp)",
        "counterpart": "SensorReading",
        "attributes": {
            "measuredValue": {
                "score": 1,
                "counterpart": ("double value", "SensorReading"),
            },
            "Time timeStamp": {"score": 0, "counterpart": None},
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand( name, Time timeStamp, CommandStatus commandstatus)",
        "counterpart": "ControlCommand",
        "attributes": {
            "name": {"score": 0, "counterpart": None},
            "Time timeStamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
            "CommandStatus commandstatus": {
                "score": 1,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            },
        },
    },
    "AutomationRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AutomationRule( RuleStatus status, Time timeStamp)",
        "counterpart": "AlertRule",
        "attributes": {
            "RuleStatus status": {
                "score": 1,
                "counterpart": ("RuleStatus ruleStatus", "AlertRule"),
            },
            "Time timeStamp": {
                "score": 0,
                "counterpart": None,
            },
        },
    },
    "Precondition": {
        "score": 0.5,
        "type": "regular",
        "dsl": "Precondition( boolean booleanValue)",
        "counterpart": "abstract BooleanExpression",
        "attributes": {"boolean booleanValue": {"score": 0, "counterpart": None}},
    },
    "BooleanOperator": {
        "score": 1,
        "type": "regular",
        "dsl": "BooleanOperator( name)",
        "counterpart": "BinaryExpression",
        "attributes": {"name": {"score": 0, "counterpart": None}},
    },
    "Action": {
        "score": 1,
        "type": "regular",
        "dsl": "Action()",
        "counterpart": "CommandSequence",
        "attributes": {},
    },
    "Alert": {
        "score": 0,
        "type": "regular",
        "dsl": "Alert()",
        "counterpart": None,
        "attributes": {},
    },
}
