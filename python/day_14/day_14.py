#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from day import Day
from functools import reduce, lru_cache


class Day14(Day):
  class Instruction:
    def __init__(self, line):
      if line.startswith("mask"):
        self.mask = line.split("=")[1].strip()
      elif line.startswith("mem"):
        self.mask = None
        self.address = int(re.split("[\[\]]", line)[1])
        self.value = int(line.split("=")[1].strip())
      else:
        assert False

    def run(self, memory, mask):
      if self.mask:
        return self.mask

      non_zero_mask, one_mask = Day14.Instruction._build_masks(mask)
      memory[self.address] = (self.value & non_zero_mask) | one_mask
      return mask

    def run_2_corinne(self, memory, mask):
      if self.mask:
        return self.mask

      _, one_mask = Day14.Instruction._build_masks(mask)
      addresses = [f"{self.address | one_mask :036b}"]

      for i, char in enumerate(mask):
        if char != 'X':
          continue
        new_addresses = []
        for address in addresses:
          new_address = address[:i] + ('1' if address[i] == '0' else '0') + address[i + 1:]
          new_addresses.append(new_address)
        addresses += new_addresses

      for address in addresses:
        memory[int("".join(address), 2)] = self.value
      return mask

    def run_2_fabian(self, memory, mask):
      if self.mask:
        return self.mask

      for m in Day14.Instruction._generate_masks(mask):
        non_y_mask, one_mask = Day14.Instruction._build_masks_2_fabian(m)
        memory[(self.address & non_y_mask) | one_mask] = self.value
      return mask

    @staticmethod
    @lru_cache(None)
    def _generate_masks(mask):
      masks = [mask]
      for i, char in enumerate(mask):
        if char != 'X':
          continue
        new_masks = []
        for m in masks:
          new_masks.append(m[:i] + "Y" + m[i + 1:])
          new_masks.append(m[:i] + "1" + m[i + 1:])
        masks = new_masks
      return masks

    @staticmethod
    @lru_cache(None)
    def _build_masks(mask):
      non_zero_mask = int("".join(['1' if char != '0' else '0' for char in mask]), 2)
      one_mask = int("".join(['1' if char == '1' else '0' for char in mask]), 2)
      return non_zero_mask, one_mask

    @staticmethod
    @lru_cache(None)
    def _build_masks_2_fabian(mask):
      non_y_mask = int("".join(['1' if char != 'Y' else '0' for char in mask]), 2)
      one_mask = int("".join(['1' if char == '1' else '0' for char in mask]), 2)
      return non_y_mask, one_mask

  def __init__(self):
    super().__init__(14)

  def parse_data(self):
    return [Day14.Instruction(line) for line in self.raw_data]

  def part_1(self):
    memory = {}
    mask = None
    for instruction in self.data:
      mask = instruction.run(memory, mask)

    return sum(memory.values())

  @property
  def part_1_solution(self):
    return 17028179706934

  def part_2(self):
    memory = {}
    mask = None
    for instruction in self.data:
      mask = instruction.run_2_fabian(memory, mask)

    return sum(memory.values())

  @property
  def part_2_solution(self):
    return 3683236147222
