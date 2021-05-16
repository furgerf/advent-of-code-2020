#!/usr/bin/env python
# -*- coding: utf-8 -*-

from day import Day
import re


class Day02(Day):
  class PasswordAndPolicy:
    def __init__(self, line):
      match = re.match(r'^(\d+)-(\d+) (\w): (\w+)$', line)
      self.min_count = int(match[1])
      self.max_count = int(match[2])
      self.character = match[3]
      self.password = match[4]

    @property
    def is_valid_sled(self):
      count = len([x for x in self.password if x == self.character])
      return self.min_count <= count <= self.max_count

    @property
    def is_valid_toboggan(self):
      first_char = self.password[self.min_count - 1]
      second_char = self.password[self.max_count - 1]
      return (first_char == self.character) ^ (second_char == self.character)

  def __init__(self):
    super().__init__(2)

  def parse_data(self):
    return [Day02.PasswordAndPolicy(line) for line in self.raw_data]

  def part_1(self):
    return len([x for x in self.data if x.is_valid_sled])

  @property
  def part_1_solution(self):
    return 638

  def part_2(self):
    return len([x for x in self.data if x.is_valid_toboggan])

  @property
  def part_2_solution(self):
    return 699
