from website_categories import(
    SOCIAL_MEDIA,
    ADULT_CONTENT,
    GAMBLING
)
def classify_url(url):

    for site in ADULT_CONTENT:
        if site in url:
            return {
                "risk": 95,
                "category": "Adult Content",
                "action": "block"
            }

    for site in GAMBLING:
        if site in url:
            return {
                "risk": 95,
                "category": "Gambling",
                "action": "block"
            }

    for site in SOCIAL_MEDIA:
        if site in url:
            return {
                "risk": 70,
                "category": "Social Media",
                "action": "warn"
            }

    return {
        "risk": 5,
        "category": "Safe",
        "action": "allow"
    }