#!/usr/bin/env python
# -*- coding: utf-8 -*-

from day import Day


class Day01(Day):

  def __init__(self):
    super(Day01, self).__init__(1)

  def parse_data(self):
    return [int(line) for line in self.raw_data]

  def part_1(self):
    for i, number_1 in enumerate(self.data):
      for number_2 in self.data[i + 1:]:
        if number_1 + number_2 == 2020:
          return number_1 * number_2

  @property
  def part_1_solution(self):
    return 719796

  def part_2(self):
    for i, number_1 in enumerate(self.data):
      for j, number_2 in enumerate(self.data[i + 1:]):
        for number_3 in self.data[i + j + 2:]:
          if number_1 + number_2 + number_3 == 2020:
            return number_1 * number_2 * number_3

  @property
  def part_2_solution(self):
    return 144554112
