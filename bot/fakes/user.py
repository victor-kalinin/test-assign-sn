from random import shuffle, sample, randint, choice
from string import ascii_letters, digits

from bot.datasets.basicdata import dataset


class FakeUser:
    def __init__(self):
        self.first_name = choice(dataset.FIRST_NAMES)
        self.last_name = choice(dataset.LAST_NAMES)
        self.password = None
        self.email = None
        self.token = None
        self.generate_email()
        self.generate_password()

    def generate_email(self):
        self.email = f'{self.first_name}{self.last_name}{randint(0, 100)}@{choice(dataset.EMAILS)}'

    def generate_password(self, pass_len=12):
        preshuffle_list = list(ascii_letters + digits)
        shuffle(preshuffle_list)
        shuffled_string = ''.join(preshuffle_list)
        self.password = ''.join(sample(shuffled_string, pass_len))
