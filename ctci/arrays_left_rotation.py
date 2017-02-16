from copy import deepcopy

def array_left_rotation(a, n, k):
  b=deepcopy(a)
  k=k%n
  for i in range(n):
    b[i]=a[(i+k)%n]
  return b

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

