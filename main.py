def mod(a,b):
  multiplier=0
  while True:
    #print(b*multiplier)
    if b*(multiplier+1)>a:
      return a-(b*(multiplier))
    else:
      multiplier+=1

print(f"{mod(11,3)} : {11%3}")

def supermod(a,b):
  exponent=0
  while True:
    #print(b**exponent)
    if b**(exponent+1)>a:
      return a-(b**exponent)
    else:
      exponent+=1
print(supermod(154,5))
