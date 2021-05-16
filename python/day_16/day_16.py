#!/usr/bin/env python
# -*- coding: utf-8 -*-

from day import Day


class Day16(Day):
  class Category:
    def __init__(self, line):
      self.name, ranges = line.split(':')
      ranges = ranges[1:].split(' or ')
      self.first_range = tuple(int(number) for number in ranges[0].split('-'))
      self.second_range = tuple(int(number) for number in ranges[1].split('-'))

    def is_valid(self, number):
      return self.first_range[0] <= number <= self.first_range[1] \
             or self.second_range[0] <= number <= self.second_range[1]

  def __init__(self):
    super().__init__(16)

  def parse_data(self):
    def parse_ticket(line):
      return [int(number) for number in line.split(',')]

    categories_end = self.raw_data.index('')
    categories = [Day16.Category(line) for line in self.raw_data[:categories_end]]
    my_ticket = parse_ticket(self.raw_data[categories_end + 2])
    other_tickets = [parse_ticket(line) for line in self.raw_data[categories_end + 5:]]

    return categories, my_ticket, other_tickets

  def part_1(self):
    categories, _, other_tickets = self.data
    ticket_scanning_error_rate = 0

    for ticket in other_tickets:
      for i in ticket:
        if not any([category.is_valid(i) for category in categories]):
          ticket_scanning_error_rate += i

    return ticket_scanning_error_rate

  @property
  def part_1_solution(self):
    return 27911

  def part_2(self):
    categories, my_ticket, other_tickets = self.data
    valid_tickets = []
    for ticket in other_tickets:
      if all(any([category.is_valid(i) for category in categories]) for i in ticket):
        valid_tickets.append(ticket)

    possible_categories = {}
    for category in categories:
      for i in range(len(my_ticket)):
        if all(category.is_valid(ticket[i]) for ticket in valid_tickets):
          if i not in possible_categories:
            possible_categories[i] = []
          possible_categories[i].append(category.name)

    result = 1
    while any(len(categories) > 0 for categories in possible_categories.values()):
      for index in possible_categories.keys():
        categories = possible_categories[index][:]
        if len(categories) != 1:
          continue
        if categories[0].startswith('departure'):
          result *= my_ticket[index]
        for other_categories in possible_categories.values():
          if categories[0] in other_categories:
            other_categories.remove(categories[0])

    return result

  @property
  def part_2_solution(self):
    return 737176602479
