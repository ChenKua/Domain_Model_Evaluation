{
    "DeviceStatus": {
        "score": 0,
        "type": "enum",
        "dsl": "DeviceStatus(Activated, Deactivated)",
        "counterpart": None,
        "attributes": {
            "Activated": {
                "score": 0,
                "counterpart": None,
            },
            "Deactivated": {"score": 0, "counterpart": None},
        },
    },
    "CommandType": {
        "score": 0.5,
        "type": "enum",
        "dsl": "CommandType (lockDoor, turnOnHeating)",
        "counterpart": ("type", "abstract Device"),
        "attributes": {
            "lockDoor": {"score": 0, "counterpart": None},
            "turnOnHeating": {"score": 0, "counterpart": None},
        },
    },
    "CommandStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "CommandStatus (Requested, Completed, Failed)",
        "counterpart": "ActionStatus",
        "attributes": {
            "Requested": {"score": 1, "counterpart": ("requested", "ActionStatus")},
            "Completed": {"score": 1, "counterpart": ("completed", "ActionStatus")},
            "Failed": {"score": 1, "counterpart": ("failed", "ActionStatus")},
        },
    },
    "RuleStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "RuleStatus (created, edited, activated, deactivated )",
        "counterpart": "RuleStatus",
        "attributes": {
            "created": {"score": 1, "counterpart": ("created", "RuleStatus")},
            "edited": {"score": 1, "counterpart": ("edited", "RuleStatus")},
            "activated": {"score": 1, "counterpart": ("activated", "RuleStatus")},
            "deactivated": {"score": 1, "counterpart": ("deactivated", "RuleStatus")},
        },
    },
    "BinaryOp": {
        "score": 0,
        "type": "enum",
        "dsl": "BinaryOp (AND, OR )",
        "counterpart": None,
        "attributes": {
            "AND": {"score": 0, "counterpart": None},
            "OR": {"score": 0, "counterpart": None},
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
        "score": 0,
        "type": "regular",
        "dsl": "SmartHome()",
        "counterpart": None,
        "attributes": {},
    },
    "User": {
        "score": 1,
        "type": "regular",
        "dsl": "User(string name)",
        "counterpart": "User",
        "attributes": {"string name": {"score": 0, "counterpart": None}},
    },
    "Address": {
        "score": 1,
        "type": "regular",
        "dsl": "Address(string city, string postalCode, string street, string aptNumber)",
        "counterpart": "Address",
        "attributes": {
            "string city": {"score": 0, "counterpart": None},
            "string postalCode": {"score": 0, "counterpart": None},
            "string street": {"score": 0, "counterpart": None},
            "string aptNumber": {"score": 0, "counterpart": None},
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
        "dsl": "abstract Device(DeviceStatus deviceStatus, int deviceID)",
        "counterpart": "abstract Device",
        "attributes": {
            "DeviceStatus deviceStatus": {
                "score": 0.5,
                "counterpart": ("Boolean activated", "abstract Device"),
            },
            "int deviceID": {
                "score": 1,
                "counterpart": ("Integer uniqueId", "abstract Device"),
            },
        },
    },
    "SensorDevice": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorDevice()",
        "counterpart": "Sensor",
        "attributes": {},
    },
    "ActuatorDevice": {
        "score": 1,
        "type": "regular",
        "dsl": "ActuatorDevice()",
        "counterpart": "Actuator",
        "attributes": {},
    },
    "ActivityLog": {
        "score": 1,
        "type": "regular",
        "dsl": "ActivityLog()",
        "counterpart": "ActivityLog",
        "attributes": {},
    },
    "abstract RuntimeElement": {
        "score": 0,
        "type": "abstract",
        "dsl": "abstract RuntimeElement(time timestamp)",
        "counterpart": None,
        "attributes": {
            "time timestamp": {"score": 0.5, "counterpart": (None, "TimeStamp")}
        },
    },
    "SensorReading": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorReading(double value)",
        "counterpart": "SensorReading",
        "attributes": {
            "double value": {
                "score": 1,
                "counterpart": ("Integer measuredValue", "SensorReading"),
            }
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand (CommandType commandType, CommandStatus commandStatus)",
        "counterpart": "ControlCommand",
        "attributes": {
            "CommandType commandType": {
                "score": 1,
                "counterpart": ("commandType", "ControlCommand"),
            },
            "CommandStatus commandStatus": {
                "score": 0.5,
                "counterpart": ("ActionStatus status", "Action"),
            },
        },
    },
    "AlertRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AlertRule (RuleStatus ruleStatus)",
        "counterpart": "AutomationRule",
        "attributes": {
            "RuleStatus ruleStatus": {
                "score": 1,
                "counterpart": ("RuleStatus rule", "AutomationRule"),
            }
        },
    },
    "abstract BooleanExpression": {
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract BooleanExpression()",
        "counterpart": ("Boolean precondition", "AutomationRule"),
        "attributes": {},
    },
    "RelationalTerm": {
        "score": 0,
        "type": "regular",
        "dsl": "RelationalTerm()",
        "counterpart": None,
        "attributes": {},
    },
    "NotExpression": {
        "score": 0,
        "type": "regular",
        "dsl": "NotExpression()",
        "counterpart": None,
        "attributes": {},
    },
    "BinaryExpression": {
        "score": 0,
        "type": "regular",
        "dsl": "BinaryExpression(BinaryOp binaryOp)",
        "counterpart": None,
        "attributes": {"BinaryOp binaryOp": {"score": 0, "counterpart": None}},
    },
    "CommandSequence": {
        "score": 1,
        "type": "regular",
        "dsl": "CommandSequence()",
        "counterpart": "Action",
        "attributes": {},
    },
}
