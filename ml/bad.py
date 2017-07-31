from sklearn.naive_bayes import MultinomialNB 
from sklearn.pipeline import Pipeline 
from sklearn.feature_extraction.text import CountVectorizer
x=[] 
y=[]
with open('trainingdata.txt') as f: 
    n_cases = f.readline() 
    for line in f: 
        temp = line.split() 
        n=len(temp) 
        y.append(int(temp[0])) 
        x.append( " ".join(temp[1:n]) )
pipeline = Pipeline([ ('vectorizer', CountVectorizer()), ('classifier', MultinomialNB()) ])
pipeline.fit(x, y)
n = int(input())
x_new=[]
for data in range(n): 
    temp = str(input()) 
    x_new.append(temp)
results=pipeline.predict(x_new)
for i in range(n): print(results[i])
