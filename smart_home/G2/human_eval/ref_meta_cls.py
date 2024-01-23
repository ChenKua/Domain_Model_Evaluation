{
    "DeviceStatus": {
        "score": 1,
        "counterpart": "DeviceStatus",
        "attributes": {
            "Activated": {"score": 1, "counterpart": ("Activated", "DeviceStatus")},
            "Deactivated": {"score": 1, "counterpart": ("Deactivated", "DeviceStatus")},
        },
    },
    "CommandType": {
        "score": 1,
        "counterpart": "ControlCommand",
        "attributes": {
            "lockDoor": {"score": 1, "counterpart": ("LockDoor", "ControlCommand")},
            "turnOnHeating": {
                "score": 1,
                "counterpart": ("TurnOnHeating", "ControlCommand"),
            },
        },
    },
    "CommandStatus": {
        "score": 1,
        "counterpart": "Status",
        "attributes": {
            "Requested": {"score": 1, "counterpart": ("Requested", "Status")},
            "Completed": {"score": 1, "counterpart": ("Completed", "Status")},
            "Failed": {"score": 1, "counterpart": ("Failed", "Status")},
        },
    },
    "RuleStatus": {
        "score": 1,
        "counterpart": "RuleStatus",
        "attributes": {
            "created": {"score": 1, "counterpart": ("Created", "RuleStatus")},
            "edited": {"score": 1, "counterpart": ("Edited", "RuleStatus")},
            "activated": {"score": 1, "counterpart": ("Activated", "RuleStatus")},
            "deactivated": {"score": 1, "counterpart": ("Deactivated", "RuleStatus")},
        },
    },
    "BinaryOp": {
        "score": 0,
        "counterpart": None,
        "attributes": {
            "AND": {"score": 0, "counterpart": None},
            "OR": {"score": 0, "counterpart": None},
        },
    },
    "SHAS": {"score": 1, "counterpart": "SHAS", "attributes": {}},
    "SmartHome": {"score": 1, "counterpart": "SmartHome", "attributes": {}},
    "User": {
        "score": 1,
        "counterpart": "User",
        "attributes": {"string name": {"score": 0, "counterpart": None}},
    },
    "Address": {
        "score": 0.5,
        "counterpart": ("string address", "SmartHome"),
        "attributes": {
            "string city": {
                "score": 0.5,
                "counterpart": ("string address", "SmartHome"),
            },
            "string postalCode": {
                "score": 0.5,
                "counterpart": ("string address", "SmartHome"),
            },
            "string street": {
                "score": 0.5,
                "counterpart": ("string address", "SmartHome"),
            },
            "string aptNumber": {
                "score": 0.5,
                "counterpart": ("string address", "SmartHome"),
            },
        },
    },
    "Room": {"score": 1, "counterpart": "Room", "attributes": {}},
    "abstract Device": {
        "score": 0.5,
        "counterpart": "Device",
        "attributes": {
            "DeviceStatus deviceStatus": {
                "score": 0.5,
                "counterpart": ("DeviceStatus deviceStatus", "ChangeInState"),
            },
            "int deviceID": {
                "score": 1,
                "counterpart": ("string deviceIdentifier", "Device"),
            },
        },
    },
    "SensorDevice": {"score": 1, "counterpart": "SensorDevice", "attributes": {}},
    "ActuatorDevice": {"score": 1, "counterpart": "ActuatorDevice", "attributes": {}},
    "ActivityLog": {"score": 1, "counterpart": "ActivityLog", "attributes": {}},
    "abstract RuntimeElement": {
        "score": 0,
        "counterpart": None,
        "attributes": {
            "time timestamp": {
                "score": 0.5,
                "counterpart": ("time timeStamp", "SensorReading"),
            }
        },
    },
    "SensorReading": {
        "score": 1,
        "counterpart": "SensorReading",
        "attributes": {
            "double value": {
                "score": 1,
                "counterpart": ("float measuredValue", "SensorReading"),
            }
        },
    },
    "ControlCommand": {
        "score": 1,
        "counterpart": "ActuatorCommand",
        "attributes": {
            "CommandType commandType": {
                "score": 1,
                "counterpart": ("ControlCommand controlCommand", "ActuatorCommand"),
            },
            "CommandStatus commandStatus": {
                "score": 1,
                "counterpart": ("Status status", "ActuatorCommand"),
            },
        },
    },
    "AlertRule": {
        "score": 1,
        "counterpart": "AutomationRule",
        "attributes": {
            "RuleStatus ruleStatus": {
                "score": 1,
                "counterpart": ("RuleStatus ruleStatus", "AutomationRule"),
            }
        },
    },
    "abstract BooleanExpression": {
        "score": 0.5,
        "counterpart": "Precondition",
        "attributes": {},
    },
    "RelationalTerm": {"score": 1, "counterpart": "RelationalTerm", "attributes": {}},
    "NotExpression": {"score": 0, "counterpart": None, "attributes": {}},
    "BinaryExpression": {
        "score": 0,
        "counterpart": None,
        "attributes": {"BinaryOp binaryOp": {"score": 0, "counterpart": None}},
    },
    "CommandSequence": {"score": 1, "counterpart": "Action", "attributes": {}},
}
