#!/usr/bin/env python
# -*- coding: utf-8 -*-

from day import Day


class Day15(Day):
  def __init__(self):
    super().__init__(15)

  def parse_data(self):
    return [int(number) for number in self.raw_data[0].split(',')]

  def find_number(self, target_index):
    occurrences = {number: index for index, number in enumerate(self.data[:-1])}
    last_number = self.data[-1]
    for index in range(len(occurrences), target_index - 1):
      last_index = occurrences.get(last_number)
      occurrences[last_number] = index
      if last_index is None:
        last_number = 0
      else:
        last_number = index - last_index

    return last_number

  def part_1(self):
    return self.find_number(2020)

  @property
  def part_1_solution(self):
    return 1665

  def part_2(self):
    return self.find_number(30000000)

  @property
  def part_2_solution(self):
    return 16439
