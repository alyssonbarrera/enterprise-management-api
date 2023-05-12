class AppError(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.statusCode = status_code

    def __str__(self):
        return f"AppError: {self.message} (code: {self.status_code})"
