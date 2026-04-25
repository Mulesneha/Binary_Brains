from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

soil_map = {'sandy': 0, 'clay': 1, 'loamy': 2}


def recommend_fertilizer(n, p, k):
    recommendations = []

    if n < 60:
        recommendations.append("Add Nitrogen fertilizer (Urea)")
    elif n > 120:
        recommendations.append("Nitrogen is high, avoid adding more")

    if p < 40:
        recommendations.append("Add Phosphorus fertilizer (DAP)")
    elif p > 60:
        recommendations.append("Phosphorus is high, reduce usage")

    if k < 40:
        recommendations.append("Add Potassium fertilizer (MOP)")
    elif k > 60:
        recommendations.append("Potassium is high, avoid excess")

    if not recommendations:
        return ["Soil nutrients are balanced ✅"]

    return recommendations


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        soil = request.form["soil"]
        temperature = float(request.form["temperature"])
        rainfall = float(request.form["rainfall"])
        ph = float(request.form["ph"])
        nitrogen = float(request.form["nitrogen"])
        phosphorus = float(request.form["phosphorus"])
        potassium = float(request.form["potassium"])
        humidity = float(request.form["humidity"])

        soil_val = soil_map.get(soil, 0)

        features = [[
            soil_val,
            temperature,
            rainfall,
            ph,
            nitrogen,
            phosphorus,
            potassium,
            humidity
        ]]

  
        prediction = model.predict(features)[0]

        fertilizer = recommend_fertilizer(nitrogen, phosphorus, potassium)

        return render_template("index.html",
                               result=prediction,
                               fertilizer=fertilizer)

    except Exception as e:
        return render_template("index.html", result=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)
