from flask import Flask,jsonify
from flask_cors import CORS
from flask import request
from AI.ai_manager import process

app=Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "GuardianMind AI Backend Running"
    })

@app.route("/analyze")
def analyze():
    url = request.args.get("url", "")
    result = process(url)
    return jsonify(result)

if __name__ =="__main__":
    app.run(debug=True)
