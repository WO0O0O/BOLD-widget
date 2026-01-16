# Crypto Widget

Free iPhone widget that shows live crypto prices and market analysis. Runs on GitHub Actions, uses Gemini AI for analysis, stores data in a Gist, displays via Scriptable.

Built by Daniel Wooster.

## How it works

1. GitHub Action runs every 30 mins
2. Python script fetches prices (CoinGecko) and news (DuckDuckGo)
3. Gemini analyses the data and outputs a market report
4. Report saved to a public Gist
5. Scriptable widget reads the Gist and displays it

## Stack

- **Scheduler:** GitHub Actions
- **AI:** Gemini 2.5 Flash
- **Prices:** CoinGecko API
- **Search:** ddgs (DuckDuckGo)
- **Storage:** GitHub Gist
- **Display:** Scriptable (iOS)

## Files

- `main.py` - fetches data and calls Gemini
- `CryptoTick.js` - Scriptable widget code
- `.github/workflows/daily_update.yml` - runs every 30 mins

## Docs

- [Overview](docs/OVERVIEW.md)
- [Limits](docs/LIMITS.md)
