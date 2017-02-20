
n,k=input().strip().split(' ')
n,k = [int(n),int(k)]
clouds=[int(i) for i in input().strip().split(" ")]

pos=0
E=100

def move(pos,E):
    pos+=k
    pos%=n
    E-=1
    if clouds[pos]==1:
        E-=2
    return pos,E
pos,E=move(pos,E)
while (pos!=0):
    pos,E=move(pos,E)

print(E)
