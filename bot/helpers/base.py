class BaseHelper:
    def __init__(self, accept='application/json', content_type='application/json'):
        self.accept = accept
        self.content_type = content_type

    @property
    def headers(self):
        return {'accept': self.accept,
                'content_type': self.content_type}

    @property
    def data(self):
        return {}

    @property
    def params(self):
        return {}
