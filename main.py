import os
import json
import requests
import google.generativeai as genai
from duckduckgo_search import DDGS
from datetime import datetime

# Setup
GENAI_KEY = os.environ["GEMINI_API_KEY"]
GIST_TOKEN = os.environ["GIST_TOKEN"]
GIST_ID = os.environ["GIST_ID"]

genai.configure(api_key=GENAI_KEY)

def get_market_data():
    queries = [
        "Bitcoin price today usd", 
        "Ethereum price today usd",
        "latest crypto news geopolitics fed rate",
        "crypto fear and greed index today",
        "bitcoin support resistance levels analysis today"
    ]
    
    results = []
    with DDGS() as ddgs:
        for q in queries:
            r = list(ddgs.text(q, max_results=3))
            results.extend(r)
    return str(results)

def analyze_market(search_data):
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    Role: Senior Crypto Analyst.
    Task: Analyze these search results and output a strictly valid JSON object.
    
    Search Data: {search_data}
    
    Output Format (JSON only, no markdown blocks):
    {{
        "btc_price": "$95,XXX",
        "eth_price": "$3,XXX",
        "bias": "BULLISH" | "BEARISH" | "NEUTRAL",
        "bias_color": "#00FF00" (if bullish) | "#FF0000" (if bearish) | "#FFFF00" (if neutral),
        "summary": "One sentence summary of the market driver (e.g. 'Fed rate pause likely, driving risk-on flows').",
        "support": "BTC Support: $XX,XXX",
        "resistance": "BTC Res: $XX,XXX",
        "updated": "HH:MM UTC"
    }}
    """
    
    response = model.generate_content(prompt)
    clean_json = response.text.replace('```json', '').replace('```', '').strip()
    return json.loads(clean_json)

def update_gist(data):
    headers = {"Authorization": f"token {GIST_TOKEN}"}
    payload = {
        "files": {
            "crypto_data.json": {
                "content": json.dumps(data, indent=2)
            }
        }
    }
    requests.patch(f"https://api.github.com/gists/{GIST_ID}", json=payload, headers=headers)

if __name__ == "__main__":
    print("Starting analysis...")
    raw_data = get_market_data()
    print("Data fetched. Analyzing...")
    json_output = analyze_market(raw_data)
    json_output["updated"] = datetime.utcnow().strftime("%H:%M UTC")
    print("Analysis complete. Updating Gist...")
    update_gist(json_output)
    print("Done!")
