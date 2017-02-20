import math

q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    ictr=0
    lx=x.bit_length()
    if lx%4==0:
      lx=lx//4
    else:
      lx=lx//4+1
    bx=x.to_bytes(lx,'little',signed=True)
    for i in range(x):
      li=i.bit_length()
      if li%4==0:
        li=li//4
      else:
        li=li//4+1
      bi=i.to_bytes(li,'little',signed=True)
      y=x.from_bytes(bx[:li],"little",signed=True)
      if y^i>y:
        ictr+=1
    print(ictr)