
fd={0:0,1:1}
def fibonacci(n):
    if n in fd.keys():
      return fd[n]
    else:      
      fd[n]=fibonacci(n-1)+fibonacci(n-2)
    return fd[n]
n = int(input())
print(fibonacci(n))

