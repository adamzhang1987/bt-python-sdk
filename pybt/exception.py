class ClientException(Exception):
    """Unhandled API client exception"""
    message = 'unhandled error'

    def __init__(self, message=None):
        if message is not None:
            self.message = message

    def __unicode__(self):
        return u'<Err: {0.message}>'.format(self)

    __str__ = __unicode__


class ConnectionRefused(ClientException):
    """Connection refused by remote host"""


class EmptyResponse(ClientException):
    """Empty response from API"""


class BadRequest(ClientException):
    """Invalid request passed"""


class IPBlocked(ClientException):
    """IP blocked"""


class InvalidAPIKey(ClientException):
    """Invalid API key"""
