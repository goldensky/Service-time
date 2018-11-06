import functools
import time
import unittest
import heapq
import random
import numpy as np


def count_time(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        t = time.time()
        result = func(*args, **kwargs)
        time_of_work = time.time() - t
        print('time_of_work = ', time_of_work)
        return result
    return inner


@count_time
def totalTime(input_array, number_of_items):
    result_array = [0] * number_of_items
    for item in input_array:
        smallest_element = result_array[0]
        heapq.heapreplace(result_array, smallest_element + item)
    return heapq.nlargest(1, result_array)[0]


@count_time
def totalTime(input_array, number_of_items):
    result_array = [0] * number_of_items
    for item in input_array:
        heapq.heapreplace(result_array, result_array[0] + item)
    return heapq.nlargest(1, result_array)[0]


def get_random_array_generator(low, high, size):
    return (random.randint(low, high) for i in range(size))


def get_np_random_array_generator(low, high, size):
    return (np.random.randint(low, high) for i in range(size))


                 

if __name__ == '__main__':
    low = 1
    high = 256
    queue_size = 10000000
    number_of_cash_desk = 1000
    current_queue = list(get_np_random_array_generator(low, high, queue_size))
    
    result = totalTime(current_queue, number_of_cash_desk)
    print('result = ', result)







