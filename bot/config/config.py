import configparser
import os


class Settings:
    USER_SECTION = 'User'
    API_SECTION = 'API_Routes'

    def __init__(self, config_filename='./bot/config/settings.ini'):
        self.config_filename = config_filename
        self.config = None
        self.users_count = None
        self.user_posts_max = None
        self.user_likes_max = None
        self.host = None
        self.api_route_signup = None
        self.api_route_login = None
        self.api_route_posts = None
        self.api_route_user_post = None
        self.api_route_user_like = None
        self.load()
        self.save()

    def create_if_not_exist(self):
        self.config = configparser.ConfigParser()
        if not os.path.exists(self.config_filename):
            self.config.add_section(self.USER_SECTION)
            self.config.add_section(self.API_SECTION)
            with open(self.config_filename, 'w') as cf:
                self.config.write(cf)

    def load(self):
        self.create_if_not_exist()
        self.config.read(self.config_filename)

        try:
            self.users_count = int(self.config[self.USER_SECTION].get('users_count', '1'))
            self.user_posts_max = int(self.config[self.USER_SECTION].get('user_posts_max', '1'))
            self.user_likes_max = int(self.config[self.USER_SECTION].get('user_likes_max', '1'))
            self.host = self.config[self.API_SECTION].get('host', 'http://127.0.0.1:3000')
            self.api_route_signup = self.config[self.API_SECTION].get('api_route_signup', '')
            self.api_route_login = self.config[self.API_SECTION].get('api_route_login', '')
            self.api_route_posts = self.config[self.API_SECTION].get('api_route_posts', '')
            self.api_route_user_post = self.config[self.API_SECTION].get('api_route_user_post', '')
            self.api_route_user_like = self.config[self.API_SECTION].get('api_route_user_like', '')

        except configparser.Error:
            raise configparser.ParsingError

    def save(self):
        self.config[self.USER_SECTION]['users_count'] = str(self.users_count)
        self.config[self.USER_SECTION]['user_posts_max'] = str(self.user_posts_max)
        self.config[self.USER_SECTION]['user_likes_max'] = str(self.user_likes_max)
        self.config[self.API_SECTION]['host'] = self.host
        self.config[self.API_SECTION]['api_route_signup'] = self.api_route_signup
        self.config[self.API_SECTION]['api_route_login'] = self.api_route_login
        self.config[self.API_SECTION]['api_route_posts'] = self.api_route_posts
        self.config[self.API_SECTION]['api_route_user_post'] = self.api_route_user_post
        self.config[self.API_SECTION]['api_route_user_like'] = self.api_route_user_like

        with open(self.config_filename, 'w') as cf:
            self.config.write(cf)


settings = Settings()
