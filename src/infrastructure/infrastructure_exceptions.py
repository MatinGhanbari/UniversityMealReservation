class InfrastructureException(Exception):
    """Base class for all infrastructure exceptions."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message


class EmailSendingException(InfrastructureException):
    """Raised when an email cannot be sent."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
