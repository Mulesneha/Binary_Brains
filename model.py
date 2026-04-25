import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load data
data = pd.read_csv("dataset.csv")

# Convert categorical to numbers
data['soil'] = data['soil'].map({'sandy': 0, 'clay': 1, 'loamy': 2})

X = data[['soil', 'temperature', 'rainfall']]
y = data['crop']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved!")
