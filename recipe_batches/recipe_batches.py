#!/usr/bin/python

import math
#inputs:
#Recipe Dictionary: keys = ingredients, values = amounts
#Available Ingredients Dictionatry: keys = ingredients, values = amounts

#output:
#integer
#represents max num of batches of recipe that can be made with the available ingredients
 
#Tools: 
# use keys, values in dict.items to iterate and work with the 2 dictionaries
# use len dict to check if recipe is of greater length than ingredients, is so return 0

#Plan
#using keys, values, if key in 2 matches key in 1, then divide value of 2 by value of 1, using //, append integer result to array called possible totals
#return min of possible totals
#be wary of values becoming floats or strings, may have to use int() to make sure values stay integers
#what if the two dictionaries were of same length but ingredients differed?  could I check the length of possible totals against the length of recipes to see if zero needed to be returned? This test case is not in the tests, but is a possible scenario

def recipe_batches(recipe, ingredients):
  possible_batches = []
  if len(ingredients) < len(recipe):
    return 0
  else:
    for key, value in recipe.items():
      for ing, amt in ingredients.items():
        if key == ing:
          batch_amt = amt//value 
          possible_batches.append(batch_amt)
    return min(possible_batches)

recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 5 },
  { 'milk': 138, 'butter': 48, 'flour': 51 }
)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))