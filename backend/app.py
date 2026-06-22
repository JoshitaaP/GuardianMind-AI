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

    url = request.args.get("url", "")

    print("Website:", url)

    if "google" in url:

        return jsonify({
            "risk": 5,
            "category": "Safe",
            "action": "allow"
        })

    elif "youtube" in url:

        return jsonify({
            "risk": 20,
            "category": "Entertainment",
            "action": "allow"
        })

    elif "torrent" in url:

        return jsonify({
            "risk": 70,
            "category": "Piracy",
            "action": "warn"
        })

    else:

        return jsonify({
            "risk": 95,
            "category": "Unknown Risk",
            "action": "block"
        })
if __name__ =="__main__":
    app.run(debug=True)
