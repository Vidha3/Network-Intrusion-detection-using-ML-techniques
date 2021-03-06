import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier 
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pandas as pd
import numpy as np
from time import time

start_time = time()
#Import dataset
#directory = os.getcwd()
#directory = os.path.join(directory, "optimized_attacks_normal")
#os.chdir(directory)
dataset = pd.read_csv('attacks_normal.csv')
data = dataset.iloc[1:, 1:] 
X = data.iloc[:, :-1].values 
y = data.iloc[:, 41].values 

y[y==11] = 1
y[y!=1] = 0

#split data intp train and test, fit, transform
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#classify using mlp
classifier=MLPClassifier(hidden_layer_sizes = (5,), solver='lbfgs', random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

end_time = time()

#Print results
print("Accuracy Score:", accuracy_score(y_test, y_pred)) 
print("\n\nTime taken: %.2f" %(end_time-start_time),"seconds")
print()
print("Confusion Matrix\n", confusion_matrix(y_test, y_pred))
print("Report:\n", classification_report(y_test, y_pred, target_names=['attack', 'normal']))
