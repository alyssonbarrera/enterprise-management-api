class AppValidatorError(Exception):
    def __init__(self, message):
        self.message = {
            'validation_error': message,
        }

        self.status_code = 400

    def __str__(self):
        return f"ValidationError: {self.message} (code: {self.status_code})"
