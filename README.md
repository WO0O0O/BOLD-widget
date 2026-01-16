# Crypto Widget

A fully free crypto market widget that pulls live data, runs it through Gemini for analysis, and displays it on my iPhone home screen.

Built by Daniel Wooster.

## What it does

- Runs hourly on GitHub Actions (free tier)
- Scrapes crypto data using DuckDuckGo search
- Sends results to Gemini 1.5 Flash for sentiment analysis
- Stores the output as JSON in a public Gist
- Displays on iPhone via Scriptable widget

## How it works

```
GitHub Actions (cron) --> Python script --> DuckDuckGo search
                                |
                                v
                          Gemini API
                                |
                                v
                          GitHub Gist
                                |
                                v
                       Scriptable widget
```

## Docs

- [Overview](docs/OVERVIEW.md) - architecture and stack
- [Setup Guide](docs/SETUP_GUIDE.md) - how to set this up yourself
- [Phase 1: Backend](docs/PHASE1_BACKEND.md) - the Python script and GitHub Action
- [Phase 2: Widget](docs/PHASE2_WIDGET.md) - the Scriptable code
- [Checklist](docs/CHECKLIST.md) - track your progress

## Output

The backend produces JSON like this:

```json
{
  "btc_price": "$95,420",
  "eth_price": "$3,250",
  "bias": "BULLISH",
  "bias_color": "#00FF00",
  "summary": "Fed rate pause likely, driving risk-on flows.",
  "support": "BTC Support: $92,000",
  "resistance": "BTC Res: $98,000",
  "updated": "14:30 UTC"
}
```

## The stack

Everything here is free:

| Component | Service           | Notes                         |
| --------- | ----------------- | ----------------------------- |
| Scheduler | GitHub Actions    | 2,000 mins/month free         |
| Search    | duckduckgo-search | Python lib, no API key needed |
| AI        | Google Gemini     | Free tier for 1.5 Flash       |
| Storage   | GitHub Gist       | Just a public gist            |
| Display   | Scriptable        | Free iOS app                  |

## License

MIT
