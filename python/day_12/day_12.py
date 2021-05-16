#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

from day import Day


class Day12(Day):
  def __init__(self):
    super().__init__(12)

  def parse_data(self):
    return [(line[0], int(line[1:])) for line in self.raw_data]

  def part_1(self):
    facing = 90
    pos_x = 0
    pos_y = 0

    for instruction, amount in self.data:
      if instruction == "N":
        pos_y += amount
      elif instruction == "E":
        pos_x += amount
      elif instruction == "S":
        pos_y -= amount
      elif instruction == "W":
        pos_x -= amount
      elif instruction == "R":
        assert amount % 90 == 0
        facing += amount
      elif instruction == "L":
        assert amount % 90 == 0
        facing -= amount
      elif instruction == "F":
        pos_y += amount * int(np.cos(facing * np.pi / 180))
        pos_x += amount * int(np.sin(facing * np.pi / 180))
      else:
        assert False

    return abs(pos_x) + abs(pos_y)

  @property
  def part_1_solution(self):
    return 1177

  def part_2(self):
    pos_x = 0
    pos_y = 0
    wp_x = 10
    wp_y = 1

    def rotate_wp(angle):
      return (wp_x * int(np.cos(-angle * np.pi / 180)) - wp_y * int(np.sin(-angle * np.pi / 180)),
              wp_x * int(np.sin(-angle * np.pi / 180)) + wp_y * int(np.cos(-angle * np.pi / 180)))

    for instruction, amount in self.data:
      if instruction == "N":
        wp_y += amount
      elif instruction == "E":
        wp_x += amount
      elif instruction == "S":
        wp_y -= amount
      elif instruction == "W":
        wp_x -= amount
      elif instruction == "R":
        assert amount % 90 == 0
        wp_x, wp_y = rotate_wp(amount)
      elif instruction == "L":
        assert amount % 90 == 0
        wp_x, wp_y = rotate_wp(-amount)
      elif instruction == "F":
        pos_x += amount * wp_x
        pos_y += amount * wp_y
      else:
        assert False

    return abs(pos_x) + abs(pos_y)

  @property
  def part_2_solution(self):
    return 46530
