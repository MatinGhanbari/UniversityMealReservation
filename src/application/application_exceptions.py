class ApplicationException(Exception):
    """Base class for all application exceptions."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message


class DatabaseConnectionException(ApplicationException):
    """Raised when a connection to the database cannot be established."""

    def __init__(self) -> None:
        super().__init__(f"Could not connect to the database.")
