class Error(Exception):
    """Base class for other exceptions"""
    pass


class ApiIsUnreachable(Error):
    """Raised when api is unreachable"""
    pass


class DataFetchingFailed(Error):
    """Raised when the data doesn't match"""
    pass
