def rotationalCipher(input, rotation_factor):
  #return the result of rotating input a number of times equal to the rotationFactor
  """"
  input: Zebra-493?
  rotationFactor: 3
  output: Cheud-726?
  """""
  
  #declare a string variable that accounts for all alphanumeric in order 
  #you set a counter for each value and when it says to rotate a certain number it moves over from that spot
  if not input or not rotation_factor:
       return input
  capAlpha = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
  alpha = [chr(c) for c in range(ord("a"), ord("z") + 1)]
  res = []
  for c in input:
      if not c.isalnum():
          res.append(c)
      elif c.isalpha():
          if c.isupper():
              idx = capAlpha.index(c) + rotation_factor
              if idx > 25:
                  idx %= 26
              res.append(capAlpha[idx])
          else:
              idx = alpha.index(c) + rotation_factor
              if idx > 25:
                  idx %= 26
              res.append(alpha[idx])
      elif c.isdigit():
          res.append(str(int(c) + rotation_factor)[-1])
  return "".join(c for c in res)
