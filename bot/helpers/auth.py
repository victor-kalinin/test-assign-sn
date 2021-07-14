from .base import BaseHelper


class AuthorizationHelper(BaseHelper):
    def __init__(self, token: str = None):
        super(AuthorizationHelper, self).__init__()
        self.token = token

    @property
    def headers(self):
        base_headers = super(AuthorizationHelper, self).headers
        base_headers.update({
            'Authorization': f'Bearer {self.token}'
        })
        return base_headers
