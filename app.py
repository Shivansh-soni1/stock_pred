from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load pickle model
with open("stock_market.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.form

    # Create dataframe (same columns as training)
    input_data = pd.DataFrame([{
        "Open": float(data["Open"]),
        "High": float(data["High"]),
        "Low": float(data["Low"]),
        "Volume": float(data["Volume"]),
        "Year": int(data["Year"]),
        "Month": int(data["Month"]),
        "Day": int(data["Day"])
    }])

    prediction = model.predict(input_data)[0]

    return render_template("index.html", prediction=round(prediction,2))


if __name__ == "__main__":
    app.run(debug=True)
