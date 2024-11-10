""" Поведенческий шаблон проектирования 'Цепочка обязанностей'"' """


class Request:
    def __init__(self, data):
        self.data = data
        self.valid = True

class BaseRequestHandler:
    def __init__(self, _next: 'BaseRequestHandler' = None):
        self.next = _next

    def handle_request(self, request: Request):
        if self.next:
            self.next.handle_request(request)

class AuthenticationHandler(BaseRequestHandler):
    def handle_request(self, request: Request):
        if "token" not in request.data:
            request.valid = False
            print("Authentication failed")
        super().handle_request(request)

class DataValidationHandler(BaseRequestHandler):
    def handle_request(self, request: Request):
        if not request.valid:
            return
        if "data" not in request.data:
            request.valid = False
            print("Data validation failed")
        super().handle_request(request)

class LoggingHandler(BaseRequestHandler):
    def handle_request(self, request: Request):
        if not request.valid:
            return
        print("Logging request")
        super().handle_request(request)

if __name__ == "__main__":
    _request = Request({"token": "abc123", "data": "some_data"})

    authentication_handler = AuthenticationHandler()
    validation_handler = DataValidationHandler(authentication_handler)
    logging_handler = LoggingHandler(validation_handler)

    logging_handler.handle_request(_request)