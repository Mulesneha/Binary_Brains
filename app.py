from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    soil = request.form["soil"]
    temp = float(request.form["temperature"])
    rainfall = float(request.form["rainfall"])

    # Convert soil type to number - must match model.py mapping
    soil_map = {'sandy': 0, 'clay': 1, 'loamy': 2}
    soil_val = soil_map[soil]

    # Predict using model
    prediction = model.predict([[soil_val, temp, rainfall]])

    return render_template("index.html", result=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)
