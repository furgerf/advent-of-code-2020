#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from day import Day


class Day10(Day):

  def __init__(self):
    super().__init__(10)

  def parse_data(self):
    return [int(line) for line in self.raw_data]

  def part_1(self):
    differences = np.diff(sorted(self.data + [0, max(self.data) + 3]))
    return len(np.where(differences == 1)[0]) * (len(np.where(differences == 3)[0]))

  @property
  def part_1_solution(self):
    return 1920

  def part_2(self):
    open_sequences = {0: 1}
    device_joltage = max(self.data) + 3
    for number in sorted(self.data + [device_joltage]):
      for end_element, count in list(open_sequences.items()):
        if number - end_element > 3:
          del open_sequences[end_element]
      open_sequences[number] = sum(open_sequences.values())
    return open_sequences[device_joltage]

  @property
  def part_2_solution(self):
    return 1511207993344
