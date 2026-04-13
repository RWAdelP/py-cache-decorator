from typing import Callable
import functools

g_results = {}


def cache(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args,**kwargs) -> Callable:
        key = (func, args, tuple(sorted(kwargs.items()))) 
        if key in g_results:
            print("Getting from cache")
            result = g_results.get(key)
        else:
            print("Calculating new result")
            result = func(*args,**kwargs)
            g_results[key] = result            
        return result
    return wrapper
