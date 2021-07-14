import json

from .base import BaseHelper


class SignupHelper(BaseHelper):
    def __init__(self, first_name: str = None, last_name: str = None, email: str = None, password: str = None):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def data(self):
        signup_data = {
            'fullname': f'{self.first_name} {self.last_name}',
            'email': self.email,
            'password': self.password
        }
        return json.dumps(signup_data)
