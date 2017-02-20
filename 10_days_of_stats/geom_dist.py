a,b=input().strip().split()
defect_ratio=float(a)/float(b)
n=int(input().strip())

res=defect_ratio*(1.-defect_ratio)**(n-1)
print("{:.3f}".format(res))
