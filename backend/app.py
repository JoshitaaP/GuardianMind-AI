from flask import Flask,jsonify
from flask_cors import CORS
from flask import request

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

    safe_sites = [
        "google",
        "gmail",
        "wikipedia",
        "github"
    ]

    blocked_sites = [
        "porn",
        "xvideos",
        "xnxx",
        "pornhub"
    ]

    warning_sites = [
        "instagram",
        "snapchat",
        "tiktok"
    ]

    for site in blocked_sites:
        if site in url:
            return jsonify({
                "risk": 95,
                "category": "Adult Content",
                "action": "block"
            })

    for site in warning_sites:
        if site in url:
            return jsonify({
                "risk": 70,
                "category": "Social Media",
                "action": "warn"
            })

    return jsonify({
        "risk": 5,
        "category": "Safe",
        "action": "allow"
    })
if __name__ =="__main__":
    app.run(debug=True)
