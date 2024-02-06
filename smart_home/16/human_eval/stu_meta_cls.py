{
    "TypeOfCommand": {
        "score": 1,
        "type": "enum",
        "dsl": "TypeOfCommand (lockDoor, turnOnHeating)",
        "counterpart": "CommandType",
        "attributes": {
            "lockDoor": {"score": 1, "counterpart": ("lockDoor", "CommandType")},
            "turnOnHeating": {
                "score": 1,
                "counterpart": ("turnOnHeating", "CommandType"),
            },
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
    "SensorType": {
        "score": 0,
        "type": "enum",
        "dsl": "SensorType (Temperature, Movement)",
        "counterpart": None,
        "attributes": {
            "Temperature": {"score": 0, "counterpart": None},
            "Movement": {"score": 0, "counterpart": None},
        },
    },
    "ActuatorType": {
        "score": 0,
        "type": "enum",
        "dsl": "ActuatorType (Light, Lock)",
        "counterpart": None,
        "attributes": {
            "Light": {"score": 0, "counterpart": None},
            "Lock": {"score": 0, "counterpart": None},
        },
    },
    "ActuatorStatus": {
        "score": 0,
        "type": "enum",
        "dsl": "ActuatorStatus (Opened, Closed)",
        "counterpart": None,
        "attributes": {
            "Opened": {"score": 0, "counterpart": None},
            "Closed": {"score": 0, "counterpart": None},
        },
    },
    "SHAS": {
        "score": 1,
        "type": "regular",
        "dsl": "SHAS ( String address)",
        "counterpart": "SHAS",
        "attributes": {
            "String address": {
                "score": 0.5,
                "counterpart": (None, "Address"),
            }
        },
    },
    "Room": {
        "score": 1,
        "type": "regular",
        "dsl": "Room ( String name)",
        "counterpart": "Room",
        "attributes": {"String name": {"score": 0, "counterpart": None}},
    },
    "abstract Device": {
        "score": 1,
        "type": "abstract",
        "dsl": "abstract Device (  int identifier, boolean isActive)",
        "counterpart": "abstract Device",
        "attributes": {
            "int identifier": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
            "boolean isActive": {
                "score": 0.5,
                "counterpart": ("DeviceStatus deviceStatus", "abstract Device"),
            },
        },
    },
    "Sensor": {
        "score": 1,
        "type": "regular",
        "dsl": "Sensor ( SensorType type, SensorReading currentReading)",
        "counterpart": "SensorDevice",
        "attributes": {
            "SensorType type": {"score": 0, "counterpart": None},
            "SensorReading currentReading": {"score": 0, "counterpart": None},
        },
    },
    "Actuator": {
        "score": 1,
        "type": "regular",
        "dsl": "Actuator ( ActuatorType type, ActuatorStatus status)",
        "counterpart": "ActuatorDevice",
        "attributes": {
            "ActuatorType type": {"score": 0, "counterpart": None},
            "ActuatorStatus status": {
                "score": 0,
                "counterpart": None,
            },
        },
    },
    "abstract DeviceActivity": {
        "score": 0.5,
        "type": "abstract",
        "dsl": "abstract DeviceActivity ( String name, long timeStamp)",
        "counterpart": "abstract RuntimeElement",
        "attributes": {
            "String name": {
                "score": 0,
                "counterpart": None,
            },
            "long timeStamp": {
                "score": 1,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
        },
    },
    "SensorReading": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorReading ( int value)",
        "counterpart": "SensorReading",
        "attributes": {
            "int value": {"score": 1, "counterpart": ("double value", "SensorReading")}
        },
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand ( TypeOfCommand type, CommandStatus status)",
        "counterpart": "ControlCommand",
        "attributes": {
            "TypeOfCommand type": {
                "score": 1,
                "counterpart": ("CommandType commandType", "ControlCommand"),
            },
            "CommandStatus status": {
                "score": 1,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            },
        },
    },
    "AutomationRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AutomationRule ( String name, boolean isActive)",
        "counterpart": "AlertRule",
        "attributes": {
            "String name": {"score": 0, "counterpart": None},
            "boolean isActive": {"score": 0, "counterpart": None},
        },
    },
    "Precondition": {
        "score": 0.5,
        "type": "regular",
        "dsl": "Precondition ( String name, Object booleanExpression, boolean result)",
        "counterpart": "abstract BooleanExpression",
        "attributes": {
            "String name": {"score": 0, "counterpart": None},
            "Object booleanExpression": {
                "score": 0.5,
                "counterpart": (None, "BinaryExpression"),
            },
            "boolean result": {"score": 0, "counterpart": None},
        },
    },
    "Action": {
        "score": 1,
        "type": "regular",
        "dsl": "Action ( String name)",
        "counterpart": "CommandSequence",
        "attributes": {"String name": {"score": 0, "counterpart": None}},
    },
    "HistoryRuleTriggered": {
        "score": 0,
        "type": "regular",
        "dsl": "HistoryRuleTriggered ( long timeStamp)",
        "counterpart": None,
        "attributes": {"long timeStamp": {"score": 0, "counterpart": None}},
    },
}
