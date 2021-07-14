from typing import Generator


def instance_generator(class_name, value=1) -> Generator:
    for _ in range(value):
        instance = class_name()
        yield instance
