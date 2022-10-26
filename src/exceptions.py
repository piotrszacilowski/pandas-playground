class Error(Exception):
    """Base class for other exceptions"""
    pass


class ApiIsUnreachable(Error):
    """Raised when api is unreachable"""
    pass


class DataFetchingFailed(Error):
    """Raised when the data doesn't match"""
    pass


class IncorrectMonthValue(Error):
    """Incorrect value of the month. It should be between 1 and 12"""
    pass
