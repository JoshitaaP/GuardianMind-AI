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
SOCIAL_MEDIA=[
    "instagram.com",
    "snapchat.com",
    "facebook.com",
    "x.com",
    "telegram.com",
    "reddit.com"
]
ADULT_CONTENT=[
    "pornhub.com",
    "xvideo.com",
    "xhamster.com",
    "xnxx.com"
]
GAMBLING=[
    "bet365.com",
    "stake.com",
    "1xbet.com"
]
@app.route("/analyze")
def analyze():
    url = request.args.get("url", "").lower()
    print("Website:",url)

    for site in ADULT_CONTENT:
        if site in url:
            return jsonify({
                "risk": 95,
                "categoy": "Adult Content",
                "action": "block"
            })
    for site in GAMBLING:
        if site in url:
            return jsonify({
                "risk": 95,
                "category": "Gambling",
                "action": "block"
            })
    for site in SOCIAL_MEDIA:
        if site in url:
            return jsonify({
                "risk": 70,
                "category": "Social Media",
                "action": "warn"
            })
    return jsonify({
        "risk": 5,
        "category": "Safe",
        "action": "block"
    })
if __name__ =="__main__":
    app.run(debug=True)
