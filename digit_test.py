import pandas as pd
import numpy as np
import random
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn import cross_validation
from sklearn.learning_curve import learning_curve

Training=pd.DataFrame.from_csv("/home/user/train.csv")
Training.shape

Truth=pd.Series(Training.index)

state=random.randint(0,100000)
forest=RandomForestClassifier(n_estimators=100)
X_train, X_test, y_train, y_test = train_test_split(Training, Truth,test_size=0.2,random_state=state)
forest.fit(X_train,y_train)
predictions=forest.predict(X_test)
print sum(predictions == y_test)

num_trials=10
forest=RandomForestClassifier(n_estimators=100)
scores = cross_validation.cross_val_score(forest, Training, Truth, cv=num_trials)
print scores