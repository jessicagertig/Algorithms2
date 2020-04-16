#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
# def eating_cookies(n, cache=None):
#   if cache is None:
#     cache = {}
#   if n <= 1:
#     return 1
#   elif n == 2:
#     return 2
#   elif n in cache:
#     return cache[n]
#   else:
#     answer = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
#     cache[n] = answer
#     return answer

# print(eating_cookies(50))

def eating_cookies(n):
  if n <= 1:
    return 1
  elif n == 2:
    return 2
  else:
    answer = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    return answer

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')