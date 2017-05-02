import math
max_w=9800
n=100
mean=500
std=80.
width=.95
z=1.96

def pprint(i):
  print("{:.2f}".format(i))

pprint(mean-z*std/n**.5)
pprint(mean+z*std/n**.5)

