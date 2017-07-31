from sklearn.naive_bayes import MultinomialNB 
from sklearn.pipeline import Pipeline 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier as RF

qs=[]
labels=[]
f=open("trainingdata.txt")
n=int(f.readline().strip())
for i in range(n):
    data=f.readline().rstrip()
    labels.append(int(data[0]))
    data=data[2:]
    qs.append(data)
f.close()
#qs=transform.fit_transform(qs)

clf = Pipeline([ ('vectorizer', CountVectorizer()), ('classifier', MultinomialNB()) ])
clf.fit(qs,labels)

train=clf.predict(qs)
for i in range(n):
    print(train[i],labels[i])

test_data=[]
n_test=int(input().strip())
for i in range(n_test):
  test_data.append(input().rstrip())

test_labels=clf.predict(test_data)
for l in test_labels:
  print(l)
