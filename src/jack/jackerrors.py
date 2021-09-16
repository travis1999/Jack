class JackError(Exception):
    pass


class TokenError(JackError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Syntax Error: {self.message}"
