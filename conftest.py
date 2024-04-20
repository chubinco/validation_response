import pytest


@pytest.fixture()
def json_schema():
    schema = {
        "type": "object",
        "properties": {
            "data": {
                "type": "object",
                "properties": {
                    "names": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "tensor": {
                        "type": "object",
                        "properties": {
                            "shape": {
                                "type": "array",
                                "items": {"type": "integer", "minimum": 1, "maximum": 10}
                            },
                            "values": {
                                "type": "array",
                                "items": [
                                    {"type": "string", "pattern": "^[0-9]{1,6}$"},
                                    {"type": "string", "maxLength": 100},
                                    {"type": "integer", "minimum": 1},
                                    {"type": "string", "maxLength": 100}
                                ],
                                "additionalItems": False
                            }
                        },
                        "required": ["shape", "values"],
                        "additionalProperties": False
                    }
                },
                "required": ["names", "tensor"],
                "additionalProperties": False
            }
        }
    }
    return schema

