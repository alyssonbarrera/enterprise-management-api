employee_validation_schema = {
    'name': {
        'type': 'string',
        'required': True,
        'empty': False,
    },

    'cpf': {
        'type': 'string',
        'required': True,
        'empty': False,
    },

    'rg': {
        'type': 'string',
        'required': True,
        'empty': False,
    },

    'gender': {
        'type': 'string',
        'required': True,
        'empty': False,
    },

    'birth_date': {
        'type': 'string',
        'required': True,
        'empty': False,
    },

    'has_driving_license': {
        'type': 'boolean',
        'required': True,
        'empty': False,
    },

    'salary': {
        'type': 'float',
        'required': True,
        'empty': False,
    },

    'weekly_workload': {
        'type': 'integer',
        'required': True,
        'empty': False,
    },

    'department': {
        'type': 'string',
        'required': True,
        'empty': False,
    },

    'active': {
        'type': 'boolean',
        'required': False,
        'empty': False,
    }
}
