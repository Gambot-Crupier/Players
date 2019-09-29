from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

signup_schema = {
    "type": "object",
    "properties": {
        "email": {
            "type": "string",
            "format": "email"
        },
        "password": {
            "type": "string",
        },
        "name": {
            "type": "string"
        },
        "username": {
            "type": "string"
        }
    },
    "required": ["email", "password", "name", "username"]
}

def validate_signup_json(data):
    try:
        validate(data, signup_schema)
    except ValidationError as e:
        return {'success': False, 'message': e}
    except SchemaError as e:
        return {'success': False, 'message': e}
    return {'success': True, 'user': data}