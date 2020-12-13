# Day 13: Shuttle Search
import os
import sys
import numpy as np

sys.path.append(os.path.join(sys.path[0], '..', 'algorithms'))
import algorithms as algo


def parse_input(file_path):
    with open(file_path) as file:
        timestamp = int(file.readline().strip())
        times = [int(e) if e != 'x' else e for e in file.readline().strip().split(',')]
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
    timestamp = algo.chinese_remainder_theorem(a, n)
    print("Answer part two: {}".format(timestamp))


def main():
    timestamp, times = parse_input('13.txt')
    part_one(timestamp, times.copy())
    part_two(times.copy())


if __name__ == "__main__":
    main()
