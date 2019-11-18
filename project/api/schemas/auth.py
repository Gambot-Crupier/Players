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
        },
        "deviceId": {
            "type": "string"
        }
    },
    "required": ["email", "password", "name", "username"]
}

login_schema = {
    "type": "object",
    "properties": {
        "email": {
            "type": "string",
            "format": "email"
        },
        "password": {
            "type": "string"
        },
        "deviceId": {
            "type": "string"
        }
    },
    "required": ["email", "password"]
}

def validate_signup_json(data):
    try:
        validate(data, signup_schema)
    except ValidationError as e:
        return {'success': False, 'message': e}
    except SchemaError as e:
        return {'success': False, 'message': e}
    return {'success': True, 'user': data}

def validate_login_json(data):
    try:
        validate(data, login_schema)
    except ValidationError as e:
        return {'success': False, 'message': e}
    except SchemaError as e:
        return {'success': False, 'message': e}
    return {'success': True, 'user': data}