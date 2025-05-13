from typing import Optional

class ClientException(Exception):
    """Base exception for all API client errors."""
    message: str = 'unhandled error'

    def __init__(self, message: Optional[str] = None) -> None:
        """Initialize the exception.
        
        Args:
            message: Optional error message to override the default
        """
        if message is not None:
            self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        """String representation of the exception.
        
        Returns:
            Formatted error message
        """
        return f'<Err: {self.message}>'


class ConnectionRefused(ClientException):
    """Raised when connection to the panel is refused."""
    message = 'Connection refused by remote host'


class EmptyResponse(ClientException):
    """Raised when the API returns an empty response."""
    message = 'Empty response from API'


class BadRequest(ClientException):
    """Raised when the request is invalid."""
    message = 'Invalid request passed'


class IPBlocked(ClientException):
    """Raised when the IP address is blocked."""
    message = 'IP blocked'


class InvalidAPIKey(ClientException):
    """Raised when the API key is invalid."""
    message = 'Invalid API key'
