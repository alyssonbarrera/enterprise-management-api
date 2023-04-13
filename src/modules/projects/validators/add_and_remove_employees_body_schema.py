add_and_remove_employees_body_schema = {
    'employees': {
        'type': 'list',
        'required': True,
        'schema': {
            'required': True,
            'regex': '^[0-9a-fA-F]{8}-?[0-9a-fA-F]{4}-?[1-5][0-9a-fA-F]{3}-?[89abAB][0-9a-fA-F]{3}-?[0-9a-fA-F]{12}$',
        }
    }
}