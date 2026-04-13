from typing import Callable
import functools

g_results = {}


def cache(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args) -> Callable:
        result = g_results.get((func.__name__, args))
        if result is None:
            result = func(*args)
            g_results[(func.__name__, args)] = result
            print("Calculating new result")
        else:
            print("Getting from cache")
        return result
    return wrapper
