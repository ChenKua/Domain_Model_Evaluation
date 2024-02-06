{
    "RelationType": {
        "score": 1,
        "type": "enum",
        "dsl": "RelationType(AND,OR,NOT)",
        "counterpart": "BinaryOp",
        "attributes": {
            "AND": {"score": 1, "counterpart": ("AND", "BinaryOp")},
            "OR": {"score": 1, "counterpart": ("OR", "BinaryOp")},
            "NOT": {"score": 0.5, "counterpart": (None, "NotExpression")},
        },
    },
    "Operation": {
        "score": 0,
        "type": "enum",
        "dsl": "Operation(CONTROLLER,SENSOR)",
        "counterpart": None,
        "attributes": {
            "CONTROLLER": {"score": 0, "counterpart": None},
            "SENSOR": {"score": 0, "counterpart": None},
        },
    },
    "SmartHome": {
        "score": 1,
        "type": "regular",
        "dsl": "SmartHome()",
        "counterpart": "SmartHome",
        "attributes": {},
    },
    "Address": {
        "score": 1,
        "type": "regular",
        "dsl": "Address( String city, String province, String streetNumber, String country, String postalCode, String streetName)",
        "counterpart": "Address",
        "attributes": {
            "String city": {"score": 1, "counterpart": ("string city", "Address")},
            "String province": {"score": 0, "counterpart": None},
            "String streetNumber": {
                "score": 1,
                "counterpart": ("string aptNumber", "Address"),
            },
            "String country": {"score": 0, "counterpart": None},
            "String postalCode": {
                "score": 1,
                "counterpart": ("string postalCode", "Address"),
            },
            "String streetName": {
                "score": 1,
                "counterpart": ("string street", "Address"),
            },
        },
    },
    "SmartRoom": {
        "score": 1,
        "type": "regular",
        "dsl": "SmartRoom( String roomName)",
        "counterpart": "Room",
        "attributes": {"String roomName": {"score": 0, "counterpart": None}},
    },
    "abstract Device": {
        "score": 1,
        "type": "abstract",
        "dsl": "abstract Device( autounique identifier, boolean isActivated)",
        "counterpart": "abstract Device",
        "attributes": {
            "autounique identifier": {
                "score": 1,
                "counterpart": ("int deviceID", "abstract Device"),
            },
            "boolean isActivated": {
                "score": 0.5,
                "counterpart": ("Activated", "DeviceStatus"),
            },
        },
    },
    "SensorDevice": {
        "score": 1,
        "type": "regular",
        "dsl": "SensorDevice()",
        "counterpart": "SensorDevice",
        "attributes": {},
    },
    "ActuatorDevice": {
        "score": 1,
        "type": "regular",
        "dsl": "ActuatorDevice()",
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
        "dsl": "SensorReading( Date timestamp)",
        "counterpart": "SensorReading",
        "attributes": {"Date timestamp": {"score": 0, "counterpart": None}},
    },
    "ControlCommand": {
        "score": 1,
        "type": "regular",
        "dsl": "ControlCommand( String commandName, Date timestamp, String status)",
        "counterpart": "ControlCommand",
        "attributes": {
            "String commandName": {
                "score": 0.5,
                "counterpart": ("CommandType commandType", "ControlCommand"),
            },
            "Date timestamp": {
                "score": 0.5,
                "counterpart": ("time timestamp", "abstract RuntimeElement"),
            },
            "String status": {
                "score": 0.5,
                "counterpart": ("CommandStatus commandStatus", "ControlCommand"),
            },
        },
    },
    "AutomationRule": {
        "score": 1,
        "type": "regular",
        "dsl": "AutomationRule( boolean isActivated)",
        "counterpart": "AlertRule",
        "attributes": {
            "boolean isActivated": {
                "score": 0.5,
                "counterpart": ("activated", "RuleStatus"),
            }
        },
    },
    "AutomationPrecondition": {
        "score": 0.5,
        "type": "regular",
        "dsl": "AutomationPrecondition( boolean statement, RelationType relationToNextPrecondition)",
        "counterpart": "abstract BooleanExpression",
        "attributes": {
            "boolean statement": {
                "score": 0,
                "counterpart": None,
            },
            "RelationType relationToNextPrecondition": {
                "score": 0.5,
                "counterpart": ("RuleStatus ruleStatus", "AlertRule"),
            },
        },
    },
    "MeasuredValue": {
        "score": 0,
        "type": "regular",
        "dsl": "MeasuredValue( String nameOfValue, String value)",
        "counterpart": None,
        "attributes": {
            "String nameOfValue": {
                "score": 0,
                "counterpart": None,
            },
            "String value": {
                "score": 0.5,
                "counterpart": ("double value", "SensorReading"),
            },
        },
    },
    "DeviceType": {
        "score": 0,
        "type": "regular",
        "dsl": "DeviceType ( String element, Operation operation)",
        "counterpart": None,
        "attributes": {
            "String element": {
                "score": 0,
                "counterpart": None,
            },
            "Operation operation": {"score": 0, "counterpart": None},
        },
    },
    "AutomationTrigger": {
        "score": 1,
        "type": "regular",
        "dsl": "AutomationTrigger( Date timestamp)",
        "counterpart": "CommandSequence",
        "attributes": {"Date timestamp": {"score": 0, "counterpart": None}},
    },
}
