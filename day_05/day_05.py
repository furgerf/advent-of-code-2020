#!/usr/bin/env python
# -*- coding: utf-8 -*-

from day import Day
import numpy as np


class Day05(Day):

  def __init__(self):
    super(Day05, self).__init__(5)

  def parse_data(self):
    boarding_passes = []
    for line in self.raw_data:
      boarding_pass = "".join(["1" if x in ("B", "R") else "0" for x in line])
      boarding_passes.append(int(boarding_pass, 2))
    return boarding_passes

  def part_1(self):
    return max(self.data)

  @property
  def part_1_solution(self):
    return 838

  def part_2(self):
    sorted_seats = list(sorted(self.data))
    index = np.where(np.diff(sorted_seats) == 2)[0][0]
    seat = sorted_seats[index] + 1
    assert seat not in sorted_seats
    return seat

  @property
  def part_2_solution(self):
    return 714
