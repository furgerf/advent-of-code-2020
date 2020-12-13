#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass

from day import Day


class Day08(Day):

  @dataclass
  class ComputerState:
    program_counter: int
    accumulator: int

  class Instruction:

    def __init__(self, state, name, argument):
      self._state = state
      self._name = name
      self._argument = argument
      self._instruction = getattr(self, f"_execute_{self._name}")

    @staticmethod
    def parse(state, line):
      name, argument = line.split(" ")
      return Day08.Instruction(state, name, int(argument))

    def __call__(self):
      self._instruction()

    def __str__(self):
      return f"{self._name} {self._argument:+d}"

    def _execute_nop(self):
      self._state.program_counter += 1

    def _execute_jmp(self):
      self._state.program_counter += self._argument

    def _execute_acc(self):
      self._state.accumulator += self._argument
      self._state.program_counter += 1

  def __init__(self):
    self._state = Day08.ComputerState(0, 0)
    super(Day08, self).__init__(8)

  def parse_data(self):
    return [Day08.Instruction.parse(self._state, line) for line in self.raw_data]

  @staticmethod
  def run_program(instructions, state):
    executed_instructions = set()
    while state.program_counter not in executed_instructions and \
            state.program_counter < len(instructions):
      executed_instructions.add(state.program_counter)
      instructions[state.program_counter]()

  def part_1(self):
    Day08.run_program(self.data, self._state)
    return self._state.accumulator

  @property
  def part_1_solution(self):
    return 2025

  def part_2(self):
    for instruction in self.data:
      if str(instruction).startswith("acc"):
        continue

      state = Day08.ComputerState(0, 0)

      def swap_instruction(instr):
        new_line = str(instr).replace("nop", "xxx").replace("jmp", "nop").replace("xxx", "jmp")
        return Day08.Instruction.parse(state, new_line)

      instructions = [swap_instruction(instr) if instr == instruction else Day08.Instruction.parse(state, str(instr)) \
                      for instr in self.data]
      Day08.run_program(instructions, state)
      if state.program_counter == len(instructions):
        return state.accumulator

  @property
  def part_2_solution(self):
    return 2001
