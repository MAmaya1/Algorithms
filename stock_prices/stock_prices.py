#!/usr/bin/python

import argparse

def find_max_profit(prices):
  current_largest_profit = prices[1] - prices[0]
  current_smallest_value = prices[0]

  for i in range(1, len(prices) - 1):
    if prices[i] - current_smallest_value > current_largest_profit:
      current_largest_profit = prices[i] - current_smallest_value

    if prices[i] < current_smallest_value:
      current_smallest_value = prices[i]

  # profit = current_largest - current_smallest

  return current_largest_profit

  # This is just some code to accept inputs from the command line
# parser = argparse.ArgumentParser(description='Find max profit from prices.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
# args = parser.parse_args()

# print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))