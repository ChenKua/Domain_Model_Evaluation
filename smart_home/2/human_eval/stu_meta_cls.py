{
    "DeviceStatus": {
        "score": 1,
        "counterpart": "DeviceStatus",
        "attributes": {
            "Activated": {"score": 1, "counterpart": ("Activated", "DeviceStatus")},
            "Deactivated": {"score": 1, "counterpart": ("Deactivated", "DeviceStatus")},
        },
    },
    "ControlCommand": {
        "score": 1,
        "counterpart": "CommandType",
        "attributes": {
            "LockDoor": {"score": 1, "counterpart": ("lockDoor", "CommandType")},
            "TurnOnHeating": {
                "score": 1,
                "counterpart": ("turnOnHeating", "CommandType"),
            },
        },
    },
    "Status": {
        "score": 1,
        "counterpart": "CommandStatus",
        "attributes": {
            "Requested": {"score": 1, "counterpart": ("Requested", "CommandStatus")},
            "Completed": {"score": 1, "counterpart": ("Completed", "CommandStatus")},
            "Failed": {"score": 1, "counterpart": ("Failed", "CommandStatus")},
        },
    },
    "RuleStatus": {
        "score": 1,
        "counterpart": "RuleStatus",
        "attributes": {
            "Created": {"score": 1, "counterpart": ("created", "RuleStatus")},
            "Edited": {"score": 1, "counterpart": ("edited", "RuleStatus")},
            "Activated": {"score": 1, "counterpart": ("activated", "RuleStatus")},
            "Deactivated": {"score": 1, "counterpart": ("deactivated", "RuleStatus")},
        },
    },
    "TypeOfActuator": {
        "score": 0,
        "counterpart": None,
        "attributes": {
            "LightController": {"score": 0, "counterpart": None},
            "LockController": {"score": 0, "counterpart": None},
        },
    },
    "TypeOfSensor": {
        "score": 0,
        "counterpart": None,
        "attributes": {
            "TemperatureSensor": {"score": 0, "counterpart": None},
            "MovementSensor": {"score": 0, "counterpart": None},
        },
    },
    "SHAS": {"score": 1, "counterpart": "SHAS", "attributes": {}},
    "SmartHome": {
        "score": 1,
        "counterpart": "SmartHome",
        "attributes": {
            "string address": {"score": 0.5, "counterpart": ("string city", "Address")}
        },
    },
    "User": {"score": 1, "counterpart": "User", "attributes": {}},
    "Room": {"score": 1, "counterpart": "Room", "attributes": {}},
    "Device": {
        "score": 0.5,
        "counterpart": "abstract Device",
        "attributes": {
            "string deviceIdentifier": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            }
        },
    },
    "SensorDevice": {
        "score": 1,
        "counterpart": "SensorDevice",
        "attributes": {"TypeOfSensor typeOfSensor": {"score": 0, "counterpart": None}},
    },
    "ActuatorDevice": {
        "score": 1,
        "counterpart": "ActuatorDevice",
        "attributes": {
            "TypeOfActuator typeOfActuator": {"score": 0, "counterpart": None}
        },
    },
    "ActivityLog": {"score": 1, "counterpart": "ActivityLog", "attributes": {}},
    "SensorReading": {
        "score": 1,
        "counterpart": "SensorReading",
        "attributes": {
            "float measuredValue": {
                "score": 1,
                "counterpart": ("double value", "SensorReading"),
            },
            "time timeStamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
        },
    },
    "ActuatorCommand": {
        "score": 1,
        "counterpart": "ControlCommand",
        "attributes": {
            "ControlCommand controlCommand": {
                "score": 1,
                "counterpart": ("CommandType commandType", "ControlCommand"),
            },
            "Time timeStamp": {"score": 0, "counterpart": None},
            "Status status": {
                "score": 1,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            },
        },
    },
    "AutomationRule": {
        "score": 1,
        "counterpart": "AlertRule",
        "attributes": {
            "RuleStatus ruleStatus": {
                "score": 1,
                "counterpart": ("RuleStatus ruleStatus", "AlertRule"),
            },
            "Time timeStamp": {"score": 0, "counterpart": None},
        },
    },
    "Precondition": {
        "score": 0.5,
        "counterpart": "abstract BooleanExpression",
        "attributes": {},
    },
    "RelationalTerm": {"score": 1, "counterpart": "RelationalTerm", "attributes": {}},
    "Action": {"score": 1, "counterpart": "CommandSequence", "attributes": {}},
    "InfrastructureMap": {"score": 0, "counterpart": None, "attributes": {}},
    "ChangeInState": {
        "score": 0,
        "counterpart": None,
        "attributes": {
            "DeviceStatus deviceStatus": {
                "score": 0.5,
                "counterpart": ("DeviceStatus deviceStatus", "abstract Device"),
            }
        },
    },
    "Owner": {"score": 0, "counterpart": None, "attributes": {}},
    "SeparationWord": {
        "score": 0,
        "counterpart": None,
        "attributes": {"String word": {"score": 0, "counterpart": None}},
    },
}
