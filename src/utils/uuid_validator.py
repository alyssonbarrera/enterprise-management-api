from cerberus import Validator
from src.shared.errors.AppValidatorError import AppValidatorError

def uuid_validator(id):
    id_validator_schema = {
        'id': {
            'regex': '^[0-9a-fA-F]{8}-?[0-9a-fA-F]{4}-?[1-5][0-9a-fA-F]{3}-?[89abAB][0-9a-fA-F]{3}-?[0-9a-fA-F]{12}$',
        }
    }

    validator = Validator(id_validator_schema)

    if not validator.validate({'id': id}):
        raise AppValidatorError('Invalid id - the id must be a valid uuid')
    
    return validator.validated({'id': id})