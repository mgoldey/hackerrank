# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input().strip()


def proc_str(t):
  if t=="":
    return "Empty String"
  for i in range(len(t)-1):
    if t[i]==t[i+1]:
      t=proc_str(t[:i]+t[i+2:])
      break
  return t
print(proc_str(s))
    


