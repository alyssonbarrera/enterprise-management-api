project_validation_schema = {
    'name': {
        'type': 'string',
        'required': True,
        'empty': False,
    },

    'description': {
        'type': 'string',
        'required': True,
        'empty': False,
    },

    'estimated_deadline': {
        'type': 'string',
        'required': True,
        'empty': False,
    },

    'completed_hours': {
        'type': 'integer',
        'nullable': True,
        'empty': False,
    },

    'employees': {
        'type': 'list',
        'nullable': True,
        'empty': False,
    },

    'supervisor': {
        'type': 'string',
        'nullable': True,
        'empty': False,
    },

    'department': {
        'type': 'string',
        'required': True,
        'empty': False,
    },

    'done': {
        'type': 'boolean',
        'nullable': True,
        'empty': False,
    },

    'start_date': {
        'type': 'string',
        'nullable': True,
        'empty': False,
    },

    'end_date': {
        'type': 'string',
        'nullable': True,
        'empty': False,
    },
}