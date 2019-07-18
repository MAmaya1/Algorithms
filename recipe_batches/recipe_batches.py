#!/usr/bin/python

def recipe_batches(recipe, ingredients):
  batches = []

  for k in recipe:
    if k in ingredients:
      batches.append(ingredients[k] // recipe[k])
    else:
      return 0
      
  return min(batches)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))