class AppError(Exception):
    def __init__(self, message, statusCode=400):
        self.message = message
        self.statusCode = statusCode

    def __str__(self):
        return f"AppError: {self.message} (code: {self.statusCode})"
