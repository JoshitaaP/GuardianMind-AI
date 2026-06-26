from analyzers.website_analyzer import analyze
from decision_engine import decide

def process(url):
    website_result=analyze(url)
    final_result=decide(website_result)
    return final_result