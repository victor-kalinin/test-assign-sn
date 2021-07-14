import json

from .auth import AuthorizationHelper


class PostHelper(AuthorizationHelper):
    def __init__(self, title: str = None, context: str = None, **kwargs):
        super(PostHelper, self).__init__(**kwargs)
        self.title = title
        self.context = context

    @property
    def data(self):
        post_data = {
            'title': self.title,
            'context': self.context
        }
        return json.dumps(post_data)
