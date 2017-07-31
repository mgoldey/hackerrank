total = int(input())
mm=0
pm=0
cm=0
m2=0
p2=0
c2=0
mp=0
mc=0
pc=0
for i in range(total):
    m,p,c=[int(i) for i in input().split()]
    # MEANS
    mm+=m
    pm+=p
    cm+=c
    
    # CROSS PRODs
    mp+=m*p
    mc+=m*c
    pc+=p*c
    
    # sum of squares
    m2+=m*m
    p2+=p*p
    c2+=c*c

mm/=total
pm/=total
cm/=total

rmp=(mp-total*mm*pm)/(((m2-total*mm**2)*(p2-total*pm**2))**.5)
rmc=(mc-total*mm*cm)/(((m2-total*mm**2)*(c2-total*cm**2))**.5)
rpc=(pc-total*pm*cm)/(((p2-total*pm**2)*(c2-total*cm**2))**.5)

print("{:.2f}".format(rmp))
print("{:.2f}".format(rpc))
print("{:.2f}".format(rmc))
