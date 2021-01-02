import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())

i = 0
while True:
  if (a/b == c/d):
    print(i)
    break
  elif (a/b > c/d):
    print(0)
    break
  else:
    a += 1
    b += 1
    tmp = math.gcd(a, b)
    a = a // tmp
    b = b // tmp
    i += 1
