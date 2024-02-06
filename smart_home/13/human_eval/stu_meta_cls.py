{
    "Status": {
        "score": 1,
        "type": "enum",
        "dsl": "Status (Activated, Deactivated)",
        "counterpart": "DeviceStatus",
        "attributes": {
            "Activated": {"score": 1, "counterpart": ("Activated", "DeviceStatus")},
            "Deactivated": {"score": 1, "counterpart": ("Deactivated", "DeviceStatus")},
        },
    },
    "CommandStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandStatus(Requested, Completed, Failed)",
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
        "dsl": "RuleStatus(Created, Edited, Activated, Deactivated)",
        "counterpart": "RuleStatus",
        "attributes": {
            "Created": {"score": 1, "counterpart": ("created", "RuleStatus")},
            "Edited": {"score": 1, "counterpart": ("edited", "RuleStatus")},
            "Activated": {"score": 1, "counterpart": ("activated", "RuleStatus")},
            "Deactivated": {"score": 1, "counterpart": ("deactivated", "RuleStatus")},
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
        "dsl": "User( String name)",
        "counterpart": "User",
        "attributes": {
            "String name": {"score": 1, "counterpart": ("string name", "User")}
        },
    },
    "Room": {
        "score": 1,
        "type": "regular",
        "dsl": "Room( String name)",
        "counterpart": "Room",
        "attributes": {"String name": {"score": 0, "counterpart": None}},
    },
    "abstract Device": {
        "score": 1,
        "type": "abstract",
        "dsl": "abstract Device( unique Integer id, String location, Status status)",
        "counterpart": "abstract Device",
        "attributes": {
            "unique Integer id": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
            "String location": {
                "score": 0,
                "counterpart": None,
            },
            "Status status": {
                "score": 1,
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
    "abstract DeviceActivity": {
        "score": 1,
        "type": "abstract",
        "dsl": "abstract DeviceActivity( Time time)",
        "counterpart": "abstract RuntimeElement",
        "attributes": {
            "Time time": {
                "score": 1,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            }
        },
    },
    "SensorReading": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorReading( double value)",
        "counterpart": "SensorReading",
        "attributes": {
            "double value": {
                "score": 1,
                "counterpart": ("double value", "SensorReading"),
            }
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand( CommandStatus commandStatus",
        "counterpart": "ControlCommand",
        "attributes": {
            "CommandStatus commandStatu": {
                "score": 1,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            }
        },
    },
    "AutomationRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AutomationRule( Time triggeredTime, RuleStatus status)",
        "counterpart": "AlertRule ",
        "attributes": {
            "Time triggeredTime": {"score": 0, "counterpart": None},
            "RuleStatus status": {
                "score": 1,
                "counterpart": ("RuleStatus ruleStatus", "AlertRule"),
            },
        },
    },
    "Precondition": {
        "score": 0,
        "type": "regular",
        "dsl": "Precondition( boolean result)",
        "counterpart": "abstract BooleanExpression",
        "attributes": {"boolean result": {"score": 0, "counterpart": None}},
    },
    "CommandContent": {
        "score": 0,
        "type": "regular",
        "dsl": "CommandContent( String name)",
        "counterpart": None,
        "attributes": {
            "String name": {
                "score": 0,
                "counterpart": None,
            }
        },
    },
    "InfrastructureMap": {
        "score": 0,
        "type": "regular",
        "dsl": "InfrastructureMap( int activatedDevice, int deactivatedDevice)",
        "counterpart": None,
        "attributes": {
            "int activatedDevice": {"score": 0, "counterpart": None},
            "int deactivatedDevice": {"score": 0, "counterpart": None},
        },
    },
    "AutomationRecord": {
        "score": 0,
        "type": "regular",
        "dsl": "AutomationRecord()",
        "counterpart": None,
        "attributes": {},
    },
    "DeviceType": {
        "score": 0.5,
        "type": "regular",
        "dsl": "DeviceType( String name)",
        "counterpart": ("CommandType commandType", "ControlCommand"),
        "attributes": {"String name": {"score": 0, "counterpart": None}},
    },
    "RelevantAlert": {
        "score": 0,
        "type": "regular",
        "dsl": "RelevantAlert()",
        "counterpart": None,
        "attributes": {},
    },
    "Action": {
        "score": 1,
        "type": "regular",
        "dsl": "Action()",
        "counterpart": "CommandSequence",
        "attributes": {},
    },
}
