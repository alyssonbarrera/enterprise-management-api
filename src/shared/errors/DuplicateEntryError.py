from .AppError import AppError

class DuplicateEntryError(AppError):
    def __init__(self, message):
        super().__init__(message, 409)
