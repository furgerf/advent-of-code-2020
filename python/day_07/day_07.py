#!/usr/bin/env python
# -*- coding: utf-8 -*-

from day import Day


class Day07(Day):

  class BagRule:
    def __init__(self, line):
      line = line.replace("bags", "").replace("bag", "").replace(".", "")
      line_parts = line.split("contain")
      self.outer_bag = line_parts[0].strip()
      self.inner_bags = []
      if line_parts[1].endswith("no other "):
        return
      for bag in line_parts[1].split(","):
        number, colour = bag.strip().split(" ", 1)
        self.inner_bags.append((int(number), colour))

  def __init__(self):
    super(Day07, self).__init__(7)

  def parse_data(self):
    return [Day07.BagRule(line) for line in self.raw_data]

  def part_1(self):
    assert len({rule.outer_bag for rule in self.data}) == len(self.data)

    containment_rules = {}
    for rule in self.data:
      for _, bag in rule.inner_bags:
        if bag not in containment_rules:
          containment_rules[bag] = []
        containment_rules[bag].append(rule.outer_bag)

    possible_bags = set()
    bags_to_check = set(containment_rules["shiny gold"])

    while bags_to_check:
      bag = bags_to_check.pop()
      possible_bags.add(bag)
      bags_to_check.update(set(containment_rules.get(bag, [])).difference(possible_bags))

    return len(possible_bags)

  @property
  def part_1_solution(self):
    return 378

  def part_2(self):
    content_rules = {rule.outer_bag: rule.inner_bags for rule in self.data}
    bag_count = 0
    bags_to_check = [(1, "shiny gold")]

    while bags_to_check:
      bag = bags_to_check.pop()
      bag_count += bag[0]
      for inner_bag in content_rules[bag[1]]:
        bags_to_check.append((inner_bag[0] * bag[0], inner_bag[1]))

    return bag_count - 1  # only want to know the number of bags inside the shiny gold one

  @property
  def part_2_solution(self):
    return 27526

