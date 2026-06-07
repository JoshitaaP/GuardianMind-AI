from flask import Flask,jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "GuardianMind AI Backend Running"
    })
@app.route("/analyze")
def analyze():
    return jsonify({
        "risk": 95,
        "category": "Adult Content",
        "action": "block"
    })
if __name__ =="__main__":
    app.run(debug=True)
