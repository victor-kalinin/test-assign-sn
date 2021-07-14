import json
import requests
from random import sample, choice

from bot.config.config import settings
from bot.fakes.gen import instance_generator
from bot.fakes.user import FakeUser
from bot.fakes.post import FakePost

from bot.helpers.base import BaseHelper
from bot.helpers.signup import SignupHelper
from bot.helpers.login import LoginHelper
from bot.helpers.post import PostHelper
from bot.helpers.like import LikeHelper


def full_api_route(api_route):
    return settings.host + api_route


def signup(user: FakeUser):
    signup_helper = SignupHelper(first_name=user.first_name, last_name=user.last_name,
                                 email=user.email, password=user.password)
    url = full_api_route(settings.api_route_signup)
    try:
        res = requests.post(url=url, headers=signup_helper.headers, data=signup_helper.data())
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return res


def login(user: FakeUser):
    login_helper = LoginHelper(email=user.email, password=user.password)
    url = full_api_route(settings.api_route_login)
    try:
        res = requests.post(url=url, headers=login_helper.headers, data=login_helper.data, verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return json.loads(res.content)['access_token']


def user_post(user: FakeUser, post: FakePost):
    post_helper = PostHelper(token=user.token, title=post.title, context=post.context)
    url = full_api_route(settings.api_route_user_post)
    try:
        res = requests.post(url=url, headers=post_helper.headers, data=post_helper.data, verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return res


def get_posts_ids():
    helper = BaseHelper()
    url = full_api_route(settings.api_route_posts)
    try:
        res = requests.get(url=url, headers=helper.headers)
        content = json.loads(res.content)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return [post['id'] for post in content]


def user_like(user: FakeUser, post_id, is_like=True):
    like_helper = LikeHelper(token=user.token, is_like=is_like)
    url = full_api_route(settings.api_route_user_like + str(post_id))
    try:
        res = requests.post(url=url, headers=like_helper.headers, data=like_helper.data,
                            params=like_helper.params, verify=False)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return res


def main() -> None:
    print('Simple Social Network Bot started.')
    print('Preparing a list of fake users ...', end='\t')
    users_list = [user for user in instance_generator(FakeUser, settings.users_count)]
    print('OK')

    print('Signup and posting of publications ...', end='\t')
    for user in users_list:
        signup(user)
        user.token = login(user)  # login user and get token

        for post in instance_generator(FakePost, settings.user_posts_max):
            user_post(user, post)
    print('OK')

    # getting all posts ids
    post_ids = get_posts_ids()

    print('Liking posts ...', end='\t')
    for user in users_list:
        for like in sample(post_ids, settings.user_likes_max):
            user_like(user, like, choice([True, False]))
    print('OK')
    print('All tasks are completed.')
