from .auth import AuthorizationHelper


class LikeHelper(AuthorizationHelper):
    def __init__(self, is_like: bool = None, **kwargs):
        super(LikeHelper, self).__init__(**kwargs)
        self.is_like = is_like

    @property
    def params(self):
        like_params = {
            'is_like': self.is_like
        }
        return like_params
