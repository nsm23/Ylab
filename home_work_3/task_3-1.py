import functools
"""Напишите функцию-декоратор, которая сохранит (закэширует) 
значение декорируемой функции multiplier (Чистая функция). 
Если декорируемая функция будет вызвана повторно с теми же параметрами —
декоратор должен вернуть сохранённый результат, не выполняя функцию.

В качестве структуры для кэша, можете использовать словарь в Python.
*В качестве задания со звездочкой можете использовать вместо Python-словаря => Redis."""


def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]
    wrapper.cache = {}
    return wrapper


@cache
def multiplier(number: int):
    return number * 2
