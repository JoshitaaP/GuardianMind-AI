from backend.website_categories import *
def analyze(url):
    url=url.lower()
    for site in ADULT_CONTENT:
        if site in url:
            return {
                "website": site,
                "category":"Adult Content",
                "risk":95,
                "confidence":1.0,
                "reasons":[
                    "Known adult content website"
                ]
            }

    for site in GAMBLING:
        if site in url:
            return {
                "website": site,
                "category": "Gambling",
                "risk": 95,
                "confidence": 1.0,
                "reasons": [
                    "Known gambling website"
                ]
            }

    for site in SOCIAL_MEDIA:
        if site in url:
            return {
                "website": site,
                "category": "Social Media",
                "risk": 70,
                "confidence": 0.95,
                "reasons": [
                    "High engagement paltform",
                    "Can reduce productivity"

                ]
            }

    return {
        "website": url,
        "risk": 5,
        "confidence": "0.90",
        "reasons":[
            "No risky category detected"
        ]
    }
