"""Hаписать декоратор для повторного выполнения декорируемой функции через некоторое время.
Использует наивный экспоненциальный рост времени повтора (factor) до граничного времени ожидания
 (border_sleep_time). В качестве параметров декоратор будет получать:

call_count - число, описывающее кол-во раз запуска функций;
start_sleep_time - начальное время повтора;
factor - во сколько раз нужно увеличить время ожидания;
border_sleep_time - граничное время ожидания.
Формула:

t = start_sleep_time * 2^(n) if t < border_sleep_time
t = border_sleep_time if t >= border_sleep_time"""
import time


def func_decorator_repeat(call_count: int,
                          start_sleep_time: int,
                          factor: int,
                          border_sleep_time: int):
    def inner(function):
        def wrapper(*args, **kwargs):
            nonlocal start_sleep_time
            for i in range(1, call_count + 1):
                time.sleep(start_sleep_time)
                result = function(*args, **kwargs)
                print(f'Run № {i} - '
                      f'waiting {start_sleep_time} - '
                      f'result of the decorated function {result}')
                if start_sleep_time < border_sleep_time:
                    start_sleep_time *= factor
                    if start_sleep_time >= border_sleep_time:
                        start_sleep_time = border_sleep_time
            print('Finish')

        return wrapper

    return inner


