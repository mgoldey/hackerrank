

r=1.09

pb=r/(r+1.)
pg=1.0-pb

from math import factorial as fac


def bd(n):
    p=fac(6)/(fac(n)*fac(6-n))
    res=p*pb**n*pg**(6-n)
    return res
    
res=0
for i in [3,4,5,6]:
    res+=bd(i)
print("{:.3f}".format(res))



#for i in range(int(1e8)):
#    bctr=0
#    ctr+=1
#    for j in range(6):
#        if random.random()<=thr:
#            bctr+=1
#    if bctr==3:
#        ctrb+=1

#print("{:.3f}".format(100.*ctrb/ctr))
