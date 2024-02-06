{
    "CommandStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandStatus(REQUESTED,FAILED,COMPLETED)",
        "counterpart": "CommandStatus",
        "attributes": {
            "REQUESTED": {"score": 1, "counterpart": ("Requested", "CommandStatus")},
            "FAILED": {"score": 1, "counterpart": ("Failed", "CommandStatus")},
            "COMPLETED": {"score": 1, "counterpart": ("Completed", "CommandStatus")},
        },
    },
    "DeviceType": {
        "score": 0,
        "type": "enum",
        "dsl": "DeviceType(TEMPERATURE_SENSOR,MOVEMENT_SENSOR,LIGHT_CONTROLLER, LOCK_CONTROLLER)",
        "counterpart": None,
        "attributes": {
            "TEMPERATURE_SENSOR": {"score": 0, "counterpart": None},
            "MOVEMENT_SENSOR": {"score": 0, "counterpart": None},
            "LIGHT_CONTROLLER": {"score": 0, "counterpart": None},
            "LOCK_CONTROLLER": {"score": 0, "counterpart": None},
        },
    },
    "SHAS": {
        "score": 1,
        "type": "regular",
        "dsl": "SHAS ()",
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
    "Address": {
        "score": 1,
        "type": "regular",
        "dsl": "Address( int addressNumber, String streetName, String postalCode)",
        "counterpart": "Address",
        "attributes": {
            "int addressNumber": {
                "score": 1,
                "counterpart": ("string aptNumber", "Address"),
            },
            "String streetName": {
                "score": 1,
                "counterpart": ("string street", "Address"),
            },
            "String postalCode": {
                "score": 1,
                "counterpart": ("string postalCode", "Address"),
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
    "Device": {
        "score": 0.5,
        "type": "regular",
        "dsl": "Device( DeviceType type, Room room, autounique identifier, boolean isActive)",
        "counterpart": "abstract Device",
        "attributes": {
            "DeviceType type": {
                "score": 0,
                "counterpart": None,
            },
            "Room room": {"score": 0, "counterpart": None},
            "autounique identifier": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
            "boolean isActive": {
                "score": 0.5,
                "counterpart": ("DeviceStatus deviceStatus", "abstract Device"),
            },
        },
    },
    "SensorDevice": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorDevice( SensorReading lastReading)",
        "counterpart": "SensorDevice",
        "attributes": {"SensorReading lastReading": {"score": 0, "counterpart": None}},
    },
    "ActuatorDevice": {
        "score": 1,
        "type": "regular",
        "dsl": "ActuatorDevice( ControlCommand lastCommand)",
        "counterpart": "ActuatorDevice",
        "attributes": {
            "ControlCommand lastCommand": {
                "score": 0.5,
                "counterpart": ("CommandType commandType", "ControlCommand"),
            }
        },
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
        "dsl": "SensorReading( int readingValue, int time, Room room)",
        "counterpart": "SensorReading",
        "attributes": {
            "int readingValue": {
                "score": 1,
                "counterpart": ("double value", "SensorReading"),
            },
            "int time": {"score": 0, "counterpart": None},
            "Room room": {"score": 0, "counterpart": None},
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand( int time, CommandStatus status, Room room)",
        "counterpart": "ControlCommand",
        "attributes": {
            "int time": {"score": 0, "counterpart": None},
            "CommandStatus status": {
                "score": 1,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            },
            "Room room": {"score": 0, "counterpart": None},
        },
    },
    "AutomationRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AutomationRule( int priority, int time, boolean isActive)",
        "counterpart": "AlertRule",
        "attributes": {
            "int priority": {"score": 0, "counterpart": None},
            "int time": {
                "score": 0,
                "counterpart": None,
            },
            "boolean isActive": {
                "score": 0.5,
                "counterpart": ("RuleStatus ruleStatus", "AlertRule"),
            },
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
}
