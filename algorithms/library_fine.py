# Enter your code here. Read input from STDIN. Print output to STDOUT
d1,m1,y1=[int(i) for i in input().split()]

d2,m2,y2=[int(i) for i in input().split()]
fine=0
if y1>y2:
  fine+=10000
elif m1>m2 and y1==y2:
  fine+=(m1-m2)*500
elif d1>d2 and y1==y2 and m1==m2:
  fine+=(d1-d2)*15
print(fine)
  
