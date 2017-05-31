for i in range(1,1+int(input())):
  ret_str=""
  if i%3==0:
    ret_str+="Fizz"
  if i%5==0:
    ret_str+="Buzz"
  if ret_str=="":
    print(i)
  else:
    print(ret_str)
