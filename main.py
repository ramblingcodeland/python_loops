import time
import numpy as np
import cyloop        # Cython module
import loop          # C Extension
from dataclasses import dataclass
from functools import wraps
LOOP_COUNTER_MAX: int = 100_000_001


@dataclass
class Result:
    accumulator: int
    elapsed_time: float = 0
    func_name: str = ''

    def __repr__(self):
        return f"\nElapsed Time: {self.elapsed_time} Accumulator: {self.accumulator}  -  {self.func_name}\n\n"


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time: float = time.perf_counter()
        r: Result = func(*args, **kwargs)
        r.elapsed_time = time.perf_counter() - start_time
        r.func_name = func.__name__
        return r
    return wrapper


@timer
def pure_python_loop():
    acc: int = 0
    for i in range(1, LOOP_COUNTER_MAX):
        acc += i
    return Result(accumulator=acc)


@timer
def list_comprehension():
    acc: int = sum([x for x in range(1, LOOP_COUNTER_MAX)])
    return Result(accumulator=acc)


@timer
def generator_loop():
    acc: int = sum((x for x in range(1, LOOP_COUNTER_MAX)))
    return Result(accumulator=acc)


@timer
def numpy_loop():
    acc: int = np.arange(1, LOOP_COUNTER_MAX).sum()
    return Result(accumulator=acc)


@timer
def cython_loop():
    acc: int = cyloop.run(LOOP_COUNTER_MAX)
    return Result(accumulator=acc)


@timer
def c_extension_loop():
    acc: int = loop.run(LOOP_COUNTER_MAX)
    return Result(accumulator=acc)


if __name__ == '__main__':

    result: Result = pure_python_loop()
    print(f"{result!r}")

    result: Result = list_comprehension()
    print(f"{result!r}")

    result: Result = generator_loop()
    print(f"{result!r}")

    result: Result = numpy_loop()
    print(f"{result!r}")

    result: Result = cython_loop()
    print(f"{result!r}")

    result: Result = c_extension_loop()
    print(f"{result!r}")
