import time

def number_of_repetitions(number):

    def actual_decorator (func):

        def wrapper():

            all_time_call = 0
            all_calls = []

            for _ in range(number):
                start_call = time.time()
                func_for_wrapper = func()
                end_call = time.time()
                time_for_call = end_call - start_call
                all_time_call += time_for_call
                all_calls.append(time_for_call)
                print(f'Время вызова: {time_for_call}')

            print(f'Имя декорируемой функции: {func.__name__}')
            print(f'Время на все вызовы: {all_time_call}')
            print(f'Время последнего вызова: {all_calls.pop()}')

            return func_for_wrapper

        return wrapper

    return actual_decorator

@number_of_repetitions(2)
def get_name():
    return "hi"
