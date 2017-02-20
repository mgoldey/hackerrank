from math import factorial as fac

a,n=input().strip().split()
pr=int(a)/100 # reject probability

n=int(n)  # num of pistons in batch


def bd(i):
    p=fac(n)/(fac(i)*fac(n-i))
    res=p*pr**i*(1.-pr)**(n-i)
    return res

no_more_than_two=0.0
for i in range(3):
    no_more_than_two+=bd(i)

print("{:.3f}".format(no_more_than_two))

at_least_two=0.0
for i in range(2,n+1,1):
    at_least_two+=bd(i)
print("{:.3f}".format(at_least_two))
