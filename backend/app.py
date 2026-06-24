from flask import Flask,jsonify
from flask_cors import CORS
from flask import request
from classsifier import classify_url

app=Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "GuardianMind AI Backend Running"
    })

@app.route("/analyze")
def analyze():
    url = request.args.get("url", "").lower()
    print("Website:",url)
    result = classify_url(url)
    return jsonify(result)

if __name__ =="__main__":
    app.run(debug=True)
