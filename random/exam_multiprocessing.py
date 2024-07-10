import multiprocessing as mp
import time
import math

result_one = []
result_two = []
result_three = []


def calc_one(numbers):
    for number in numbers:
        result_one.append(math.sqrt(number ** 3))


def calc_two(numbers):
    for number in numbers:
        result_two.append(math.sqrt(number ** 4))


def calc_three(numbers):
    for number in numbers:
        result_three.append(math.sqrt(number ** 5))


if __name__ == "__main__":
    number_list = list(range(3000000))

    p1 = mp.Process(target=calc_one, args=(number_list,))
    p2 = mp.Process(target=calc_two, args=(number_list,))
    p3 = mp.Process(target=calc_three, args=(number_list,))

    # If you're worried about the results let's check
    temp_one = result_one
    temp_two = result_two
    temp_three = result_three

    time_start = time.time()

    p1.start()
    p2.start()
    p3.start()

    time_end = time.time()
    print(time_end - time_start)
    # Multiprocessing is faster than multithread

    time_start = time.time()

    calc_one(number_list)
    calc_two(number_list)
    calc_three(number_list)

    time_end = time.time()

    print(time_end - time_start)

    # Check
    print(result_one == temp_one)
    print(result_two == temp_two)
    print(result_three == temp_three)
