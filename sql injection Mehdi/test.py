from flask import Flask, request, jsonify
import joblib
import traceback

app = Flask(__name__)


# 1 Load trained machine learning model + vectorizer

try:
    model = joblib.load("trained_model.pkl")
    vectorizer = joblib.load("vectorized.pkl")
    print("[+] Model and vectorizer loaded successfully.")
except Exception as e:
    print("Error loading model or vectorizer:", e)
    exit()

# 2 Prediction function

def predict_sql_injection(query):
    try:
        vectorized = vectorizer.transform([query])
        prediction = model.predict(vectorized)[0]
        return "malicious" if prediction == 1 else "legitimate"
    except Exception:
        return "error"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        query = data.get("query", "")

        result = predict_sql_injection(query)

        return jsonify({
            "query": query,
            "prediction": result
        })

    except Exception as e:
        return jsonify({
            "error": "Server error",
            "trace": traceback.format_exc()
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
