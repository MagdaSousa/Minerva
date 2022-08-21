class ValueWithInvalidTypeException(Exception):
    def __init__(self, value, message=None):
        if not message:
            message = f'{value} is not a string'
        super().__init__(message)


class QueryPeriodErrorException(Exception):
    def __init__(self, value, message=None):
        if not message:
            message = f'{value} período fornecido inválido'
        super().__init__(message)
