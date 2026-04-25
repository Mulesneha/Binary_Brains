import pandas as pd
import sklearn.tree
import pickle
   
data = pd.read_csv("dataset.csv")
print("Before mapping:")
print(data.isnull().sum()) 
   
data['soil'] = data['soil'].map({'sandy': 0, 'clay': 1, 'loamy': 2})
   
print("After mapping:")
print(data.isnull().sum())  
   
X = data[['soil', 'temperature', 'rainfall']]
y = data['crop']
   

data = data.dropna()
X = data[['soil', 'temperature', 'rainfall']]
y = data['crop']
   
model = sklearn.tree.DecisionTreeClassifier()
model.fit(X, y)
   
pickle.dump(model, open("model.pkl", "wb"))
print("Model trained and saved!")
