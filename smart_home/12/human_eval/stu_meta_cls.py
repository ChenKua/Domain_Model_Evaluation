{
    "ControllerStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "ControllerStatus ( Requested, Completed, Failed)",
        "counterpart": "CommandStatus",
        "attributes": {
            "Requested": {"score": 1, "counterpart": ("Requested", "CommandStatus")},
            "Completed": {"score": 1, "counterpart": ("Completed", "CommandStatus")},
            "Failed": {"score": 1, "counterpart": ("Failed", "CommandStatus")},
        },
    },
    "AutomationRuleStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "AutomationRuleStatus ( Created, Edited, Activated, Deactivated)",
        "counterpart": "RuleStatus",
        "attributes": {
            "Created": {"score": 1, "counterpart": ("created", "RuleStatus")},
            "Edited": {"score": 1, "counterpart": ("edited", "RuleStatus")},
            "Activated": {"score": 1, "counterpart": ("activated", "RuleStatus")},
            "Deactivated": {"score": 1, "counterpart": ("deactivated", "RuleStatus")},
        },
    },
    "SensorType": {
        "score": 0,
        "type": "enum",
        "dsl": "SensorType( TemperatureSensor, MovementSensor)",
        "counterpart": None,
        "attributes": {
            "TemperatureSensor": {"score": 0, "counterpart": None},
            "MovementSensor": {"score": 0, "counterpart": None},
        },
    },
    "ControllerType": {
        "score": 1,
        "type": "enum",
        "dsl": "ControllerType ( LightController, LockController)",
        "counterpart": "CommandType",
        "attributes": {
            "LightController": {
                "score": 1,
                "counterpart": ("turnOnHeating", "CommandType"),
            },
            "LockController": {"score": 1, "counterpart": ("lockDoor", "CommandType")},
        },
    },
    "SHAS": {
        "score": 1,
        "type": "regular",
        "dsl": "SHAS( boolean operational )",
        "counterpart": "SHAS",
        "attributes": {"boolean operational": {"score": 0, "counterpart": None}},
    },
    "SmartHome": {
        "score": 1,
        "type": "regular",
        "dsl": "SmartHome( address, owner)",
        "counterpart": "SmartHome",
        "attributes": {
            "address": {"score": 0.5, "counterpart": (None, "Address")},
            "owner": {"score": 0, "counterpart": None},
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
        "dsl": "abstract Device( unique Integer id, boolean activated )",
        "counterpart": "abstract Device",
        "attributes": {
            "unique Integer id": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
            "boolean activated": {
                "score": 0.5,
                "counterpart": ("Activated", "DeviceStatus"),
            },
        },
    },
    "SensorDevice": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorDevice( SensorType type)",
        "counterpart": "SensorDevice",
        "attributes": {
            "SensorType type": {
                "score": 0.5,
                "counterpart": ("DeviceStatus deviceStatus", "abstract Device"),
            }
        },
    },
    "ActuatorDevice": {
        "score": 1,
        "type": "regular",
        "dsl": "ActuatorDevice( ControllerType type)",
        "counterpart": "ActuatorDevice",
        "attributes": {
            "ControllerType type": {
                "score": 1,
                "counterpart": ("CommandType commandType", "ControlCommand"),
            }
        },
    },
    "SensorReading": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorReading( int measuredValue, Time timestamp)",
        "counterpart": "SensorReading",
        "attributes": {
            "int measuredValue": {
                "score": 1,
                "counterpart": ("double value", "SensorReading"),
            },
            "Time timestamp": {"score": 0, "counterpart": None},
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand( ControllerStatus status, Time timestamp, description)",
        "counterpart": "ControlCommand",
        "attributes": {
            "ControllerStatus status": {
                "score": 1,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            },
            "Time timestamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
            "description": {"score": 0, "counterpart": None},
        },
    },
    "AutomationRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AutomationRule( boolean precondition, action, lazy Time timestamp, AutomationRuleStatus status)",
        "counterpart": "AlertRule",
        "attributes": {
            "boolean precondition": {
                "score": 0.5,
                "counterpart": (None, "abstract BooleanExpression"),
            },
            "action": {"score": 0, "counterpart": None},
            "lazy Time timestamp": {"score": 0, "counterpart": None},
            "AutomationRuleStatus status": {
                "score": 0.5,
                "counterpart": ("RuleStatus ruleStatus", "AlertRule"),
            },
        },
    },
    "Alert": {
        "score": 0,
        "type": "regular",
        "dsl": "Alert( description)",
        "counterpart": None,
        "attributes": {"description": {"score": 0, "counterpart": None}},
    },
}
