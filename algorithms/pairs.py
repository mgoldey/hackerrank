#!/usr/bin/py
# Head ends here - finds pairs of integers separated by difference k - run with pypy3 for time
def pairs(a,k):
  # a is the list of numbers and k is the difference value
  a=sorted(a)
  answer = 0
  for i in range(len(a)):
    for j in range(i+1,len(a),1):
      if (a[j]-a[i])==k:
        answer+=1
      elif (a[j]-a[i])>k:
        break
  return answer
# Tail starts here
if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))    
    _a_size=a[0]
    _k=a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b,_k))

