#!/usr/bin/python

import argparse

nums = [1050, 270, 1540, 3800, 2]

def find_max_profit(prices):
  # Find all possible profits
  # Use pointer i for range of 0 through len(arr)-1
  # Use pointer j for range of i+1(to prevent using any values before the i value) through len(arr)
  # iterate for each i subtracting each j and append(append is O(1) to a new array named 'profits'
  #use max to find the max of profits (max is O(n))
  profits = []
  for i in range(0, len(prices)-1):#O(n)
    for j in range(i+1, len(prices)):#O(n)
      profit = prices[j]-prices[i]#O(1)
      profits.append(profit)#O(1)

  return max(profits)#O(n)

print(find_max_profit(nums))

#time complexity = 
# O(n^2) + O(n)
# final = O(n^2)
  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))