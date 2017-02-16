def ransom_note(magazine, ransom):
    lm={}
    lr={}
    for i in magazine:
      if i in lm.keys():
        lm[i]=lm[i]+1
      else:
        lm[i]=1
    for i in ransom:
      if i not in lm.keys():
        return False
      if lm[i]==0:
        return False
      lm[i]=lm[i]-1
    return True
      
m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    

