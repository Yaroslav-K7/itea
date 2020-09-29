import time
from functools import wraps
from threading import Thread


def name_of_threads(name_thr, is_daemon=False):

    def actual_decorator(func):

        @wraps(func)
        def wrapper():
            thread = Thread(target=func, name=name_thr, daemon=is_daemon)
            thread.start()

        return wrapper

    return actual_decorator


@name_of_threads('MyThread', False)
def ten():
    a = time.time()
    time.sleep(1)
    for i in range(10):
        print(i)
    print(time.time() - a)
