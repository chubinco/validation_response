import pytest
from jsonschema import Draft201909Validator


@pytest.mark.parametrize("response", [
    {
        "data": {
            "names": ["messageId", "phraseText", "topK", "cus"],
            "tensor": {"shape": [1, 4],
                       "values": [
                           "12345",
                           "Подскажите как оформить дебетовую карту альфа банка?",
                           1,
                           "test_cus_8"]
                       }
        }
    },
    {
        "data": {
            "names": ["messageId", "phraseText", "topK", "cus"],
            "tensor": {"shape": [1, 10],
                       "values": [
                           "19",
                           "Подскажите как оформить кредитную карту и ипотеку  альфа банка? ",
                           -1,
                           "test_cus_11"]
                       }
        }
    }
])
def test_json_schema_validator(json_schema, response):
    Draft201909Validator(json_schema).validate(response)
