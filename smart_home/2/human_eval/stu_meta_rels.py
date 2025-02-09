[
    {
        "dsl": "1 SHAS contain * User",
        "score": 1,
        "counterpart": "1 SHAS contain * User",
    },
    {
        "dsl": "* Room associate 1 SmartHome",
        "score": 0.5,
        "counterpart": "1 SmartHome contain * Room",
    },
    {"dsl": "1 SHAS contain 1 ActivityLog", "score": 0, "counterpart": None},
    {"dsl": "* Device assocaite 1 Room", "score": 0, "counterpart": None},
    {
        "dsl": "1 ActivityLog associate * SensorReading",
        "score": 0.5,
        "counterpart": "1 ActivityLog contain * SensorReading",
    },
    {
        "dsl": "1 ActivityLog associate * ActuatorCommand",
        "score": 0.5,
        "counterpart": "1 ActivityLog contain * ControlCommand",
    },
    {
        "dsl": "1 SensorDevice contain * SensorReading",
        "score": 0.5,
        "counterpart": "* SensorReading associate 1 SensorDevice",
    },
    {
        "dsl": "1 ActuatorDevice contain * ActuatorCommand",
        "score": 0.5,
        "counterpart": "* ControlCommand associate 1 ActuatorDevice",
    },
    {
        "dsl": "1..* AutomationRule contain 1..* Precondition",
        "score": 0.5,
        "counterpart": "1 AlertRule contain 0..1 BooleanExpression",
    },
    {
        "dsl": "1..* AutomationRule contain 1..* Action",
        "score": 0.5,
        "counterpart": "1 AlertRule contain * CommandSequence",
    },
    {
        "dsl": "* Action associate 1..* ActuatorCommand",
        "score": 0.5,
        "counterpart": "1 CommandSequence contain 0..1 ControlCommand",
    },
    {
        "dsl": "SensorDevice inherit Device",
        "score": 1,
        "counterpart": "SensorDevice inherit Device",
    },
    {
        "dsl": "ActuatorDevice inherit Device",
        "score": 1,
        "counterpart": "ActuatorDevice inherit Device",
    },
    {"dsl": "Device inherit RelationalTerm", "score": 0, "counterpart": None},
    {"dsl": "Room inherit RelationalTerm", "score": 0, "counterpart": None},
    {"dsl": "User inherit Owner", "score": 0, "counterpart": None},
    {"dsl": "1 SHAS contain 1 InfrastructureMap", "score": 0, "counterpart": None},
    {"dsl": "SensorReading inherit RelationalTerm", "score": 0, "counterpart": None},
    {"dsl": "ActuatorCommand inherit RelationalTerm", "score": 0, "counterpart": None},
    {"dsl": "* ChangeInState associate 1 Device", "score": 0, "counterpart": None},
    {
        "dsl": "* ChangeInState associate 1 InfrastructureMap",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "* AutomationRule associate * AutomationRule",
        "score": 0,
        "counterpart": None,
    },
    {"dsl": "1 Owner associate * AutomationRule", "score": 0, "counterpart": None},
    {"dsl": "* Owner associate * SmartHome", "score": 0, "counterpart": None},
    {
        "dsl": "* Precondition associate * RelationalTerm",
        "score": 0,
        "counterpart": None,
    },
    {
        "dsl": "1..* SeparationWord associate * Precondition",
        "score": 0,
        "counterpart": None,
    },
]
