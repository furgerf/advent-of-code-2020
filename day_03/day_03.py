#!/usr/bin/env python
# -*- coding: utf-8 -*-

from day import Day


class Day03(Day):

  def __init__(self):
    super().__init__(3)

  def parse_data(self):
    return [[x == "#" for x in line] for line in self.raw_data]

  def count_trees_on_slope(self, right, down):
    trees = 0
    for i, row in enumerate(self.data):
      if i % down == 0 and row[(i * right // down) % len(row)]:
        trees += 1
    return trees

  def part_1(self):
    return self.count_trees_on_slope(1, 2)

  @property
  def part_1_solution(self):
    return 254

  def part_2(self):
    return self.count_trees_on_slope(1, 1) * \
           self.count_trees_on_slope(3, 1) * \
           self.count_trees_on_slope(5, 1) * \
           self.count_trees_on_slope(7, 1) * \
           self.count_trees_on_slope(1, 2)

  @property
  def part_2_solution(self):
    return 1666768320
