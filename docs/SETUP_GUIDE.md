# Setup Guide

How to get this whole thing running.

---

## Before you start

You'll need:

- GitHub account
- Google account (for Gemini API)
- iPhone with Scriptable installed
- Python 3.9+ if you want to test locally

---

## Phase 1: Backend

### Step 1: Get your API keys

#### Gemini API key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in
3. Click "Get API Key"
4. Copy it somewhere safe

Don't commit this to your repo.

#### GitHub Personal Access Token

1. GitHub Settings > Developer Settings > Personal Access Tokens > Tokens (Classic)
2. Generate new token (classic)
3. Name it something like `crypto-widget-gist`
4. Check the `gist` scope
5. Generate and copy it immediately - you won't see it again

#### Create the Gist

1. Go to [gist.github.com](https://gist.github.com)
2. Create a public gist
3. Filename: `crypto_data.json`
4. Content: just put `{}` for now
5. Create public gist
6. Grab the Gist ID from the URL - it's the long string after your username

---

### Step 2: Set up the repo

1. Create a new private repo on GitHub (I called mine `crypto-widget-backend`)

2. Go to Settings > Secrets and variables > Actions

3. Add these repository secrets:

   | Name             | Value           |
   | ---------------- | --------------- |
   | `GEMINI_API_KEY` | Your Gemini key |
   | `GIST_TOKEN`     | Your GitHub PAT |
   | `GIST_ID`        | Your Gist ID    |

---

### Step 3: Add the code

Create these files in your repo:

#### requirements.txt

```
google-generativeai
duckduckgo-search
requests
```

#### main.py

See [Phase 1 Backend](./PHASE1_BACKEND.md#mainpy) for the full script.

#### .github/workflows/daily_update.yml

See [Phase 1 Backend](./PHASE1_BACKEND.md#github-action) for the workflow YAML.

---

### Step 4: Test it

1. Push everything to GitHub
2. Go to the Actions tab
3. Click "Hourly Crypto Update"
4. Click "Run workflow" > "Run workflow"
5. Wait for it to finish (should be a green checkmark)
6. Check your Gist - it should have real data now

---

## Phase 2: The widget

### Install Scriptable

Get it from the App Store. It's free.

### Create the script

1. Open Scriptable
2. Tap + to make a new script
3. Name it `CryptoTick`
4. Paste the widget code from [Phase 2 Widget](./PHASE2_WIDGET.md#widget-code)
5. Replace the URL with your Raw Gist URL

To get your Raw Gist URL:

1. Open your Gist page
2. Click the "Raw" button on your JSON file
3. Copy that URL

### Add to home screen

1. Long press on your home screen
2. Tap the + button
3. Search for Scriptable
4. Pick the medium widget
5. Add it
6. Tap the widget and select CryptoTick

---

## If things break

### Backend problems

| Problem           | Fix                                                    |
| ----------------- | ------------------------------------------------------ |
| Workflow fails    | Check the Actions logs. Usually it's a missing secret. |
| Gist not updating | Double-check your GIST_ID and GIST_TOKEN               |
| Rate limits       | Reduce how often it runs, or check your Gemini quota   |

### Widget problems

| Problem        | Fix                                                           |
| -------------- | ------------------------------------------------------------- |
| Shows an error | Your Raw Gist URL is probably wrong                           |
| Data is stale  | Tap the widget to refresh, or check if the backend is running |
| Looks broken   | Something in the JSON structure changed                       |
