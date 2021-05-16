#!/usr/bin/env python
# -*- coding: utf-8 -*-

from day import Day
from functools import reduce


class Day13(Day):
  def __init__(self):
    super().__init__(13)

  def parse_data(self):
    t_start = int(self.raw_data[0])
    buses = [int(x) if x != 'x' else None for x in self.raw_data[1].split(',')]
    return t_start, buses

  def part_1(self):
    t_start, buses = self.data
    wait_times = {}
    for bus in buses:
      if bus is None:
        continue
      wait_times[bus - (t_start % bus)] = bus

    min_wait_time = min(wait_times.keys())
    return min_wait_time * wait_times[min_wait_time]

  @property
  def part_1_solution(self):
    return 296

  # https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
  @staticmethod
  def chinese_remainder(n, a):
    print(n)
    print(a)
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
      p = prod // n_i
      sum += a_i * Day13.mul_inv(p, n_i) * p
    return sum % prod

  @staticmethod
  def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
      return 1
    while a > 1:
      q = a // b
      a, b = b, a % b
      x0, x1 = x1 - q * x0, x0
    if x1 < 0:
      x1 += b0
    return x1

  def part_2(self):
    buses = self.data[1]
    bus_freq_and_offset = [(bus, (100 * bus - i) % bus) for i, bus in enumerate(buses) if bus is not None]
    return Day13.chinese_remainder(*zip(*bus_freq_and_offset))

  @property
  def part_2_solution(self):
    return 535296695251210
