#!/usr/bin/env python
# -*- coding: utf-8 -*-

from day import Day
import re


class Day04(Day):
  class Passport:
    def __init__(self):
      self.fields = {
        "byr": None,  # (Birth Year)
        "iyr": None,  # (Issue Year)
        "eyr": None,  # (Expiration Year)
        "hgt": None,  # (Height)
        "hcl": None,  # (Hair Color)
        "ecl": None,  # (Eye Color)
        "pid": None,  # (Passport ID)
        "cid": None  # (Country ID)
      }

    @property
    def are_fields_present(self):
      for key, value in self.fields.items():
        if key != "cid" and value is None:
          return False
      return True

    @property
    def is_byr_valid(self):
      try:
        return 1920 <= int(self.fields["byr"]) <= 2002
      except Exception:
        return False

    @property
    def is_iyr_valid(self):
      try:
        return 2010 <= int(self.fields["iyr"]) <= 2020
      except Exception:
        return False

    @property
    def is_eyr_valid(self):
      try:
        return 2020 <= int(self.fields["eyr"]) <= 2030
      except Exception:
        return False

    @property
    def is_hgt_valid(self):
      try:
        if self.fields["hgt"].endswith("cm"):
          return 150 <= int(self.fields["hgt"][:-2]) <= 193
        if self.fields["hgt"].endswith("in"):
          return 59 <= int(self.fields["hgt"][:-2]) <= 76
      except Exception:
        return False

    @property
    def is_hcl_valid(self):
      return bool(re.match(r'^#[0-9a-f]{6}$', self.fields["hcl"]))

    @property
    def is_ecl_valid(self):
        return self.fields["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl",
                                      "oth")

    @property
    def is_pid_valid(self):
      return bool(re.match(r'^[0-9]{9}$', self.fields["pid"]))

    @property
    def is_cid_valid(self):
        return True

    @property
    def are_fields_valid(self):
      return self.is_byr_valid and \
             self.is_iyr_valid and \
             self.is_eyr_valid and \
             self.is_hgt_valid and \
             self.is_hcl_valid and \
             self.is_ecl_valid and \
             self.is_pid_valid and \
             self.is_cid_valid

    @property
    def is_valid(self):
      return self.are_fields_present and self.are_fields_valid

    def add_line(self, line):
      entries = re.findall(r'([^:\s]+:[^:\s]+)', line)
      for entry in entries:
        key, value = entry.split(":")
        assert key in self.fields and self.fields[key] is None
        self.fields[key] = value

  def __init__(self):
    super().__init__(4)

  def parse_data(self):
    passports = [Day04.Passport()]
    for line in self.raw_data:
      if line == "":
        passports.append(Day04.Passport())
      else:
        passports[-1].add_line(line)
    return passports

  def part_1(self):
    return len([x for x in self.data if x.are_fields_present])

  @property
  def part_1_solution(self):
    return 222

  def part_2(self):
    return len([x for x in self.data if x.is_valid])

  @property
  def part_2_solution(self):
    return 699
