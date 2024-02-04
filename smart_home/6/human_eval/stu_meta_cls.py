{
    "ControlType": {
        "score": 1,
        "type": "enum",
        "dsl": "ControlType (LockDoor, TurnOnHeating)",
        "counterpart": "CommandType",
        "attributes": {
            "LockDoor": {"score": 1, "counterpart": ("lockDoor", "CommandType")},
            "TurnOnHeating": {
                "score": 1,
                "counterpart": ("turnOnHeating", "CommandType"),
            },
        },
    },
    "ControlStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "ControlStatus (Requested, Completed, Failed)",
        "counterpart": "CommandStatus",
        "attributes": {
            "Requested": {"score": 1, "counterpart": ("Requested", "CommandStatus")},
            "Completed": {"score": 1, "counterpart": ("Completed", "CommandStatus")},
            "Failed": {"score": 1, "counterpart": ("Failed", "CommandStatus")},
        },
    },
    "AutomationStatus": {
        "score": 1,
        "type": "enum",
        "dsl": "AutomationStatus (Created, Edited, Activated, Deactivated)",
        "counterpart": "RuleStatus",
        "attributes": {
            "Created": {"score": 1, "counterpart": ("created", "RuleStatus")},
            "Edited": {"score": 1, "counterpart": ("edited", "RuleStatus")},
            "Activated": {"score": 1, "counterpart": ("activated", "RuleStatus")},
            "Deactivated": {
                "score": 1,
                "counterpart": ("Deactivated", "DeviceStatus"),
            },
        },
    },
    "ConnectingOperator": {
        "score": 1,
        "type": "enum",
        "dsl": "ConnectingOperator (NOT, AND, OR, NoOperator)",
        "counterpart": "BinaryOp",
        "attributes": {
            "NOT": {"score": 0.5, "counterpart": (None, "NotExpression")},
            "AND": {"score": 1, "counterpart": ("AND", "BinaryOp")},
            "OR": {"score": 1, "counterpart": ("OR", "BinaryOp")},
            "NoOperator": {"score": 0, "counterpart": None},
        },
    },
    "DeviceType": {
        "score": 0,
        "type": "enum",
        "dsl": "DeviceType (Temperature, Movement, Light, Lock)",
        "counterpart": None,
        "attributes": {
            "Temperature": {"score": 0, "counterpart": None},
            "Movement": {"score": 0, "counterpart": None},
            "Light": {"score": 0, "counterpart": None},
            "Lock": {"score": 0, "counterpart": None},
        },
    },
    "SHAS": {
        "score": 1,
        "type": "regular",
        "dsl": "SHAS( String address, boolean operational)",
        "counterpart": "SHAS",
        "attributes": {
            "String address": {"score": 0.5, "counterpart": ("string city", "Address")},
            "boolean operational": {"score": 0, "counterpart": None},
        },
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
        "dsl": "abstract Device(unique int identifier, DeviceType deviceType, boolean activated)",
        "counterpart": "abstract Device",
        "attributes": {
            "unique int identifier": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
            "DeviceType deviceType": {
                "score": 0,
                "counterpart": None,
            },
            "boolean activated": {
                "score": 0.5,
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
    "SensorReading": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorReading( immutable int  measuredValue, Time timestamp)",
        "counterpart": "SensorReading",
        "attributes": {
            "immutable int  measuredValue": {
                "score": 1,
                "counterpart": ("double value", "SensorReading"),
            },
            "Time timestamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand( Time timestamp, ControlStatus controlStatus, ControlType controlType)",
        "counterpart": "ControlCommand",
        "attributes": {
            "Time timestamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
            "ControlStatus controlStatus": {
                "score": 1,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            },
            "ControlType controlType": {
                "score": 1,
                "counterpart": ("CommandType commandType", "ControlCommand"),
            },
        },
    },
    "AutomationRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AutomationRule( AutomationStatus automationStatus, Time triggeredTimestamp)",
        "counterpart": "AlertRule",
        "attributes": {
            "AutomationStatus automationStatus": {
                "score": 1,
                "counterpart": ("RuleStatus ruleStatus", "AlertRule"),
            },
            "Time triggeredTimestamp": {"score": 0, "counterpart": None},
        },
    },
    "Precondition": {
        "score": 0.5,
        "type": "regular",
        "dsl": "Precondition()",
        "counterpart": "abstract BooleanExpression",
        "attributes": {},
    },
    "RelationalTerm": {
        "score": 1,
        "type": "regular",
        "dsl": "RelationalTerm( String term)",
        "counterpart": "RelationalTerm",
        "attributes": {"String term": {"score": 0, "counterpart": None}},
    },
    "BooleanOperator": {
        "score": 1,
        "type": "regular",
        "dsl": "BooleanOperator( ConnectingOperator connectingOperator)",
        "counterpart": "BinaryExpression",
        "attributes": {
            "ConnectingOperator connectingOperator": {
                "score": 1,
                "counterpart": ("BinaryOp binaryOp", "BinaryExpression"),
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
}
