#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import combinations

from day import Day


class Day09(Day):

  def __init__(self):
    super().__init__(9)

  def parse_data(self):
    return [int(line) for line in self.raw_data]

  def part_1(self):
    for i in range(25, len(self.data)):
      target = self.data[i]
      if target not in {a + b for a, b in combinations(self.data[i - 25:i], 2)}:
        return target

  @property
  def part_1_solution(self):
    return 27911108

  def part_2(self):
    for i in range(len(self.data)):
      for j in range(i + 1, len(self.data)):
        numbers = self.data[i:j]
        if sum(numbers) == self.part_1_solution:
          return min(numbers) + max(numbers)
        if sum(numbers) > self.part_1_solution:
          break

    sequences = []
    for number in self.data:
      for sequence in sequences:
        sequence.append(number)
        if sum(sequence) == self.part_1_solution:
          return min(sequence) + max(sequence)
      sequences = [sequence for sequence in sequences if sum(sequence) < self.part_1_solution] + [[number]]

  @property
  def part_2_solution(self):
    return 4023754
