from math import sqrt
import time


def exec_time(fn):
    def wrapper(*args, **kwargs):
        print(f"start  execution of function {fn.__name__} ")
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        end = time.perf_counter()
        exec_time = end-start
        print(f"end execution of the {fn.__name__}")
        print(f'exection time for the function was: {exec_time}')
        return result
    return wrapper


@exec_time
def get_primes(input_list):
    result_list = []
    for element in input_list:
        if is_prime(element):
            result_list.append(element)

    return result_list


@exec_time
def get_primes_generator(input_list):
    for element in input_list:
        if is_prime(element):
            yield element

@exec_time
def get_primes_list_expansion(input_list):
    return (element for element in input_list if is_prime(element))


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11, 14, 16, 18]
    print("----------------------------")
    get_primes(l)
    print("----------------------------")
    print("----------------------------")
    get_primes_generator(l)
    print("----------------------------")
    print("----------------------------")
    get_primes_list_expansion(l)
    print("----------------------------")
