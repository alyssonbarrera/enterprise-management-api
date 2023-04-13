find_project_by_criteria_query_schema = {
    'id': {
        'required': False,
        'empty': False,
        'regex': '^[0-9a-fA-F]{8}-?[0-9a-fA-F]{4}-?[1-5][0-9a-fA-F]{3}-?[89abAB][0-9a-fA-F]{3}-?[0-9a-fA-F]{12}$',
    },

    'name': {
        'type': 'string',
        'required': False,
        'empty': False,
    },

    'department': {
        'type': 'string',
        'required': False,
        'empty': False,
    },
}