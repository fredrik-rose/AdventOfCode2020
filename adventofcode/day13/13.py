# Day 13: Shuttle Search
import functools as ft
import math
import numpy as np


def parse_input(file_path):
    with open(file_path) as file:
        timestamp = int(file.readline().strip())
        times =  [int(e) if e != 'x' else e for e in file.readline().strip().split(',')]
        return (timestamp, times)


def part_one(timestamp, times):
    times = [t for t in times if t != 'x']
    wait_times = [t - (timestamp % t) for t in times]
    assert not any([t == wt for t, wt in zip(times, wait_times)])
    wait_time = np.min(wait_times)
    bus_id = times[np.argmin(wait_times)]
    print("Answer part one: {}".format(bus_id * wait_time))


def part_two(times):
    # Problem:
    #     bus_i - timestamp % bus_i = offset_i =>
    #     timestamp % bus_i = bus_i - offset_i =/Due to modulo properties/=>
    #     timestamp = (bus_i - offset_i) % bus_i
    #
    # Theres is a math trick known as the "Chinese remainder theorem" that can be used to solve an
    # a system of equations on this form.
    a = [t - i for i, t in enumerate(times) if t != 'x']
    n = [t for t in times if t != 'x']
    timestamp = chinese_remainder_theorem(a, n)
    print("Answer part one: {}".format(timestamp))


def chinese_remainder_theorem(a, n):
    # Solves a system of equations on the form
    #    x = a_i mod n_i.
    # given that n_i are pairwise co-prime.
    # https://brilliant.org/wiki/chinese-remainder-theorem/
    x = 0
    # 1. Compute N = n_1 * n_2 * ... * n_N.
    N = ft.reduce(lambda x, y: x * y, n)
    for a_i, n_i in zip(a, n):
        # 2. For each i, compute y_i = N / n_i.
        y_i = N // n_i
        # 3. For each i, compute z_i = y_i^-1 mod n_i.
        z_i = modular_inverse(y_i, n_i)
        # 4.a. Add a_i * y_i * z_i to x.
        x += a_i * y_i * z_i
    # 4.b. x mod N is the unique solution modulo N.
    return x % N


def modular_inverse(a, m):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def main():
    timestamp, times = parse_input('13.txt')
    part_one(timestamp, times.copy())
    part_two(times.copy())


if __name__ == "__main__":
    main()
