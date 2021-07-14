from .signup import SignupHelper


class LoginHelper(SignupHelper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = self.email

    @property
    def data(self):
        login_data = {
            'grant_type': 'password',
            'username': self.username,
            'password': self.password
        }
        return login_data

