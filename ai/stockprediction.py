from math import floor
m,k,d=[float(i) for i in input().split()]
stocks=[]
hists=[[] for i in range(int(k))]
def mean(ar):
  m=0
  for i in ar:
    m+=i
  return m/len(ar)

def slope(x,y):
  mx=mean(x)
  my=mean(y)
  num=0
  denom=0
  for i in range(len(x)):
    num+=(x[i]-mx)*(y[i]-my)
    denom+=(x[i]-mx)**2
  return num/denom
  
owned=[]
slopes=[]
prices=[]
days=[1,2,3,4,5]
for stock in range(int(k)):
  i=input().strip().split()
  n=i[0]
  stocks.append(n)
  o=int(i[1])
  owned.append(o)
  vals=[float(j) for j in i[2:]]
  prices.append(vals[-1])
  s=slope(days,vals)
  slopes.append(s)
 

transactions=[]
if d>0:  
  l=zip(stocks,owned,prices,slopes)
  l=sorted(l,key=lambda i:i[-1])
  for stock in l:
    if stock[1]>0 and stock[-1]<0:
        transactions.append([stock[0],"SELL",round(.9*stock[1])])
        #m+=floor(stock[1])*stock[2] # WAIT TIL NEXT DAY
  l=sorted(l,key=lambda i:-i[-1])
  for stock in l:
    if stock[-1]>0 and m>0:
        amount=floor(.9*m/stock[2])
        if amount>0:
            transactions.append([stock[0],"BUY",amount])
            m-=stock[2]*amount
else:
  l=zip(stocks,owned,prices,slopes)
  l=sorted(l,key=lambda i:i[-1])
  for stock in l:
    transactions.append([stock[0],"SELL",stock[1]])
    
print(len(transactions))
for t in transactions:
    print(t[0],t[1],t[2])
