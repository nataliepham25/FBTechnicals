import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def are_they_equal(array_a, array_b):
  #length of array a
  #length of array b
  #sort the two arrays
  lenA=len(array_a)
  lenB=len(array_b)
  
  if lenA != lenB:
    return False
  
  for i in array_b: 
    if i not in array_a:
      return False
  return True


