#!/usr/bin/env python
# -*- coding: utf-8 -*-

from day import Day
import re


class Day06(Day):
  class Group:
    def __init__(self):
      self.answers = []

    def add_line(self, line):
      self.answers.append(list(line))

    @property
    def number_of_any_yes(self):
      return len(set([item for sublist in self.answers for item in sublist]))

    @property
    def number_of_all_yes(self):
      all_yes = set(self.answers[0])
      for answer in self.answers:
        all_yes.intersection_update(answer)
      return len(all_yes)

  def __init__(self):
    super().__init__(6)

  def parse_data(self):
    groups = [Day06.Group()]
    for line in self.raw_data:
      if line == "":
        groups.append(Day06.Group())
      else:
        groups[-1].add_line(line)
    return groups

  def part_1(self):
    return sum([group.number_of_any_yes for group in self.data])

  @property
  def part_1_solution(self):
    return 6768

  def part_2(self):
    return sum([group.number_of_all_yes for group in self.data])

  @property
  def part_2_solution(self):
    return 3489
