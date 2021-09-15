"""jack entry point"""
from typing import Union


def check_arg_type(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], int):
            raise TypeError("num_1 must be an integer")
        if not isinstance(args[1], int):
            raise TypeError("num_2 must be an integer")
        return func(*args, **kwargs)
    return wrapper


@check_arg_type
def add(num_1: int, num_2: int) -> Union[int, float]:
    """Add two numbers"""
    return num_1 + num_2


@check_arg_type
def sub(num_1: int, num_2: int) -> Union[int, float]:
    """Subtract two numbers"""
    return num_1 - num_2


@check_arg_type
def mul(num_1: int, num_2: int) -> Union[int, float]:
    """Multiply two numbers"""
    return num_1 * num_2


@check_arg_type
def div(num_1: int, num_2: int) -> Union[int, float]:
    """Divide two numbers"""
    return num_1 / num_2
