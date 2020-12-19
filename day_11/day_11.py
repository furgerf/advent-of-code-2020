#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

from day import Day


class Day11(Day):
  FLOOR = "."
  FREE = "L"
  OCCUPIED = "#"

  def __init__(self):
    super().__init__(11)

  def parse_data(self):
    return np.array([list(line) for line in self.raw_data])

  @staticmethod
  def count_occupied_neighbors_part_1(seating, index):
    min_x = max(index[0] - 1, 0)
    max_x = min(index[0] + 2, seating.shape[0])
    min_y = max(index[1] - 1, 0)
    max_y = min(index[1] + 2, seating.shape[1])
    return len(np.where(seating[min_x:max_x, min_y:max_y] == Day11.OCCUPIED)[0]) - \
           (1 if seating[index] == Day11.OCCUPIED else 0)

  @staticmethod
  def count_occupied_neighbors_part_2(seating, index):
    def is_occupied(cells):
      for cell in cells:
        if cell == Day11.FLOOR:
          continue
        return cell == Day11.OCCUPIED
      return False

    occupied_seats = [
      is_occupied(seating[index[0] + 1:, index[1]]),
      is_occupied(np.flip(seating[:index[0], index[1]])),
      is_occupied(seating[index[0], index[1] + 1:]),
      is_occupied(np.flip(seating[index[0], :index[1]]))
    ]

    down_right = np.diag_indices(min(seating.shape[0] - index[0] - 1, seating.shape[1] - index[1] - 1))
    occupied_seats.append(is_occupied(seating[down_right[0] + index[0] + 1, down_right[1] + index[1] + 1]))

    down_left = np.diag_indices(min(index[0], seating.shape[1] - index[1] - 1))
    occupied_seats.append(is_occupied(seating[index[0] - down_left[0] - 1, down_left[1] + index[1] + 1]))

    up_right = np.diag_indices(min(seating.shape[0] - index[0] - 1, index[1]))
    occupied_seats.append(is_occupied(seating[up_right[0] + index[0] + 1, index[1] - up_right[1] - 1]))

    up_left = np.diag_indices(min(index[0], index[1]))
    occupied_seats.append(is_occupied(seating[index[0] - up_left[0] - 1, index[1] - up_left[1] - 1]))

    return len([x for x in occupied_seats if x])

  @staticmethod
  def simulate_step(seating, max_neighbors, count_neighbors):
    next_seating = np.empty_like(seating)
    changed = False
    for index, cell in np.ndenumerate(seating):
      if cell == Day11.FREE and count_neighbors(seating, index) == 0:
        next_seating[index] = Day11.OCCUPIED
        changed = True
      elif cell == Day11.OCCUPIED and count_neighbors(seating, index) >= max_neighbors:
        next_seating[index] = Day11.FREE
        changed = True
      else:
        next_seating[index] = cell
    return next_seating, changed

  def simulate(self, max_neighbors, count_neighbors):
    changed = True
    seating = self.data
    while changed:
      seating, changed = Day11.simulate_step(seating, max_neighbors, count_neighbors)
    return len(np.where(seating == Day11.OCCUPIED)[0])

  def part_1(self):
    return self.simulate(4, Day11.count_occupied_neighbors_part_1)

  @property
  def part_1_solution(self):
    return 2354

  def part_2(self):
    return self.simulate(5, Day11.count_occupied_neighbors_part_2)

  @property
  def part_2_solution(self):
    return 4023754
