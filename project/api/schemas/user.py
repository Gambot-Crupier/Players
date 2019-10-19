from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

edit_user_schema = {
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
    "required": ["email", "password", "name", "username", "deviceId"]
}

def validate_edit_json(data):
    try:
        validate(data, edit_user_schema)
    except ValidationError as e:
        return {'success': False, 'message': e}
    except SchemaError as e:
        return {'success': False, 'message': e}
    return {'success': True, 'user': data}