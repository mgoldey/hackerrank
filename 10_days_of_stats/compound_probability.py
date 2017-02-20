
rx=4./7.
ry=5./9.
rz=4./8.

bx=1.-rx
by=1.-ry
bz=1.-rz

prob=rx*ry*bz+rx*by*rz+bx*ry*rz
print(prob)
