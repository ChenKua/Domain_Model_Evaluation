{
    "Command": {
        "score": 1,
        "type": "enum",
        "dsl": "Command ( lockDoor, turnOnHeating )",
        "counterpart": "CommandType",
        "attributes": {
            "lockDoor": {"score": 1, "counterpart": ("lockDoor", "CommandType")},
            "turnOnHeating": {
                "score": 1,
                "counterpart": ("turnOnHeating", "CommandType"),
            },
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
        "dsl": "SmartHome()",
        "counterpart": "SmartHome",
        "attributes": {},
    },
    "User": {
        "score": 1,
        "type": "regular",
        "dsl": "User(string name)",
        "counterpart": "User",
        "attributes": {
            "string name": {"score": 1, "counterpart": ("string name", "User")}
        },
    },
    "Address": {
        "score": 1,
        "type": "regular",
        "dsl": "Address(string city, string postalCode, string streetAddress, string province)",
        "counterpart": "Address",
        "attributes": {
            "string city": {"score": 1, "counterpart": ("string city", "Address")},
            "string postalCode": {
                "score": 1,
                "counterpart": ("string postalCode", "Address"),
            },
            "string streetAddress": {
                "score": 1,
                "counterpart": ("string aptNumber", "Address"),
            },
            "string province": {
                "score": 1,
                "counterpart": ("string street", "Address"),
            },
        },
    },
    "Room": {
        "score": 1,
        "type": "regular",
        "dsl": "Room(string name)",
        "counterpart": "Room",
        "attributes": {"string name": {"score": 0, "counterpart": None}},
    },
    "abstract Device": {
        "score": 1,
        "type": "abstract",
        "dsl": "abstract Device(String identifier, boolean isActivated, String status, String type)",
        "counterpart": "abstract Device",
        "attributes": {
            "String identifier": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
            "boolean isActivated": {
                "score": 0.5,
                "counterpart": ("Activated", "DeviceStatus"),
            },
            "String status": {
                "score": 1,
                "counterpart": ("DeviceStatus deviceStatus", "abstract Device"),
            },
            "String type": {"score": 0, "counterpart": None},
        },
    },
    "Sensor": {
        "score": 1,
        "type": "regular",
        "dsl": "Sensor(String measuredValue)",
        "counterpart": "SensorDevice",
        "attributes": {"String measuredValue": {"score": 0, "counterpart": None}},
    },
    "Actuator": {
        "score": 1,
        "type": "regular",
        "dsl": "Actuator ()",
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
        "dsl": "SensorReading(string timeStamp, string measuredValue)",
        "counterpart": "SensorReading",
        "attributes": {
            "string timeStamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
            "string measuredValue": {
                "score": 1,
                "counterpart": ("double value", "SensorReading"),
            },
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand(Command command, String timeStamp, String status)",
        "counterpart": "ControlCommand",
        "attributes": {
            "Command command": {
                "score": 1,
                "counterpart": ("CommandType commandType", "ControlCommand"),
            },
            "String timeStamp": {"score": 0, "counterpart": None},
            "String status": {
                "score": 1,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            },
        },
    },
    "AutomationRule": {
        "score": 0.5,
        "type": "regular",
        "dsl": "AutomationRule(boolean isActivated)",
        "counterpart": "AlertRule",
        "attributes": {
            "boolean isActivated": {
                "score": 0.5,
                "counterpart": ("activated", "RuleStatus"),
            }
        },
    },
    "Precondition": {
        "score": 0.5,
        "type": "regular",
        "dsl": "Precondition(boolean isTriggered)",
        "counterpart": "abstract BooleanExpression",
        "attributes": {
            "boolean isTriggered": {
                "score": 0,
                "counterpart": None,
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
    "Owner": {
        "score": 0,
        "type": "regular",
        "dsl": "Owner()",
        "counterpart": None,
        "attributes": {},
    },
    "AutomationRuleLog": {
        "score": 0,
        "type": "regular",
        "dsl": "AutomationRuleLog(String timeStamp)",
        "counterpart": None,
        "attributes": {
            "String timeStamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            }
        },
    },
}
