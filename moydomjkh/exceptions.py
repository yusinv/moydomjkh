class SessionException(BaseException):
    pass


class InvalidSession(SessionException):
    pass


class SessionTimeout(SessionException):
    pass

