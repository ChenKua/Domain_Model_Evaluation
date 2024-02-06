{
    "Status": {
        "score": 1,
        "type": "enum",
        "dsl": "Status(Requested, Completed, Failed)",
        "counterpart": "CommandStatus",
        "attributes": {
            "Requested": {"score": 1, "counterpart": ("Requested", "CommandStatus")},
            "Completed": {"score": 1, "counterpart": ("Completed", "CommandStatus")},
            "Failed": {"score": 1, "counterpart": ("Failed", "CommandStatus")},
        },
    },
    "SHAS": {
        "score": 1,
        "type": "regular",
        "dsl": "SHAS ( lazy String name)",
        "counterpart": "SHAS",
        "attributes": {"lazy String name": {"score": 0, "counterpart": None}},
    },
    "Infrastructure_Map": {
        "score": 1,
        "type": "regular",
        "dsl": "Infrastructure_Map(String name)",
        "counterpart": "SmartHome",
        "attributes": {"String name": {"score": 0, "counterpart": None}},
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
        "attributes": {
            "String name": {
                "score": 0,
                "counterpart": None,
            }
        },
    },
    "abstract Device": {
        "score": 1,
        "type": "abstract",
        "dsl": "abstract Device( unique String identifier, boolean isActivited)",
        "counterpart": "abstract Device",
        "attributes": {
            "unique String identifier": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
            "boolean isActivited": {
                "score": 0.5,
                "counterpart": ("Activated", "DeviceStatus"),
            },
        },
    },
    "Sensor_Device": {
        "score": 1,
        "type": "regular",
        "dsl": "Sensor_Device()",
        "counterpart": "SensorDevice",
        "attributes": {},
    },
    "Actuator_Device": {
        "score": 1,
        "type": "regular",
        "dsl": "Actuator_Device()",
        "counterpart": "ActuatorDevice",
        "attributes": {},
    },
    "Activity_Log": {
        "score": 1,
        "type": "regular",
        "dsl": "Activity_Log( lazy String name)",
        "counterpart": "ActivityLog",
        "attributes": {
            "lazy String name": {
                "score": 0,
                "counterpart": None,
            }
        },
    },
    "Sensor_Reading": {
        "score": 1,
        "type": "regular",
        "dsl": "Sensor_Reading( Integer value, Date timeStamp)",
        "counterpart": "SensorReading",
        "attributes": {
            "Integer value": {
                "score": 1,
                "counterpart": ("double value", "SensorReading"),
            },
            "Date timeStamp": {"score": 0, "counterpart": None},
        },
    },
    "Control_Command": {
        "score": 1,
        "type": "regular",
        "dsl": "Control_Command( Date timeStamp)",
        "counterpart": "ControlCommand",
        "attributes": {
            "Date timeStamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            }
        },
    },
    "Automation_Rule": {
        "score": 1,
        "type": "regular",
        "dsl": "Automation_Rule(boolean isActivated)",
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
        "dsl": "Precondition()",
        "counterpart": "abstract BooleanExpression",
        "attributes": {},
    },
    "Rational_Term": {
        "score": 1,
        "type": "regular",
        "dsl": "Rational_Term()",
        "counterpart": "RelationalTerm",
        "attributes": {},
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
    "Hierarchy": {
        "score": 0,
        "type": "regular",
        "dsl": "Hierarchy( lazy String name)",
        "counterpart": None,
        "attributes": {
            "lazy String name": {
                "score": 0,
                "counterpart": None,
            }
        },
    },
}
