# -*- coding: utf-8 -*-

"""
requests.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of Requests' exceptions.

"""
from .packages.urllib3.exceptions import HTTPError as BaseHTTPError


class RequestException(IOError):
    """There was an ambiguous exception that occurred while handling your
    request."""

    def __init__(self, *args, **kwargs):
        """
        Initialize RequestException with `request` and `response` objects.

        __init__() with *args and **kwargs should be used in the base class
        (as it is here), because it does not limit the arguments could be
        used in the subclass.
        In contrast, if you do __init__(self, request=None, response=None),
        and if you don't override __init__() in subclass, you cannot
        accept other arguments in subclass constructor.
        If you override __init__() in sublcass, it would be like:
        def __init__(self, request=None, reponse=None, other=None):
            self.other = other
            super(RequestException, self).__init__(request, reponse)

        The benefit of using *args, **kwargs is to avoid redundant code and
        get centralized management of initialization. For example, if we
        want to handle one more argument of a particular subclass, we
        could just handle it in the base class __init__().

        What's more important, RequestException is itself a subclass,
        if you do __init__(self, request=None, response=None), you will
        limit the arguments that could pass to RequestException's superclass.

        When writing your own code, just consider the possibility of using
        *args and **kwargs in __init__().
        """
        response = kwargs.pop('response', None)
        self.response = response
        self.request = kwargs.pop('request', None)
        if (response is not None and not self.request and
                hasattr(response, 'request')):
            self.request = self.response.request
        super(RequestException, self).__init__(*args, **kwargs)


class HTTPError(RequestException):
    """An HTTP error occurred."""


class ConnectionError(RequestException):
    """A Connection error occurred."""


class ProxyError(ConnectionError):
    """A proxy error occurred."""


class SSLError(ConnectionError):
    """An SSL error occurred."""


class Timeout(RequestException):
    """The request timed out.

    Catching this error will catch both
    :exc:`~requests.exceptions.ConnectTimeout` and
    :exc:`~requests.exceptions.ReadTimeout` errors.
    """


class ConnectTimeout(ConnectionError, Timeout):
    """The request timed out while trying to connect to the remote server.

    Requests that produced this error are safe to retry.
    """


class ReadTimeout(Timeout):
    """The server did not send any data in the allotted amount of time."""


class URLRequired(RequestException):
    """A valid URL is required to make a request."""


class TooManyRedirects(RequestException):
    """Too many redirects."""


class MissingSchema(RequestException, ValueError):
    """The URL schema (e.g. http or https) is missing."""


class InvalidSchema(RequestException, ValueError):
    """See defaults.py for valid schemas."""


class InvalidURL(RequestException, ValueError):
    """ The URL provided was somehow invalid. """


class ChunkedEncodingError(RequestException):
    """The server declared chunked encoding but sent an invalid chunk."""


class ContentDecodingError(RequestException, BaseHTTPError):
    """Failed to decode response content"""


class StreamConsumedError(RequestException, TypeError):
    """The content for this response was already consumed"""


class RetryError(RequestException):
    """Custom retries logic failed"""


# Warnings


class RequestsWarning(Warning):
    """Base warning for Requests."""
    pass


class FileModeWarning(RequestsWarning, DeprecationWarning):
    """
    A file was opened in text mode, but Requests determined its binary length.
    """
    pass
