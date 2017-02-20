a,b=input().strip().split()
defect_ratio=float(a)/float(b)
n=int(input().strip())

res=1.0-(1.0-defect_ratio)**n
print("{:.3f}".format(res))
