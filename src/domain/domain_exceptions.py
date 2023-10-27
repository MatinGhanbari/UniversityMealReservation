class DomainException(Exception):
    """Base class for all domain exceptions."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message


class UserNotFoundException(DomainException):
    """Raised when a user cannot be found."""

    def __init__(self, user_id: int) -> None:
        super().__init__(f"User with ID {user_id} not found.")


class InvalidRequestException(DomainException):
    """Raised when a request is invalid."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
