from cerberus import Validator
from src.shared.errors.AppValidatorError import AppValidatorError

def validator(schema, data, update=False, variant=None):
    if len(data) == 0:
        raise AppValidatorError('No data to update')
    
    validator = Validator(schema)

    if not validator.validate(data, update=update):
        if variant == 'list_employees':
            raise AppValidatorError('Invalid employees list - must be a list of uuids')
        raise AppValidatorError(validator.errors)
    
    return validator.validated(data, update=update)