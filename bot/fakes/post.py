from typing import Generator
from random import sample, randint
from string import ascii_lowercase


class FakePost:
    def __init__(self, min_items=3, max_items=12):
        self.min_items = min_items
        self.max_items = max_items
        self.title = self._sentence()
        self.context = self._text()

    def to_dict(self):
        return {'title': self.title, 'context': self.context}

    @staticmethod
    def _word():
        return ''.join(sample(ascii_lowercase, randint(1, len(ascii_lowercase))))

    def _generate_items(self, func):
        items_count = randint(self.min_items, self.max_items)
        return ' '.join(func() for _ in range(items_count))

    def _sentence(self):
        return f'{(self._generate_items(self._word)).capitalize()}.'

    def _text(self):
        return self._generate_items(self._sentence)
