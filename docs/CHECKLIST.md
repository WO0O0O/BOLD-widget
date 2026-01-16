# Checklist

Track your progress here.

---

## Phase 1: Backend

### Keys and credentials

- [ ] Get Gemini API key from [Google AI Studio](https://aistudio.google.com/)
- [ ] Generate GitHub PAT with gist scope
- [ ] Create public Gist with crypto_data.json
- [ ] Save the Gist ID

### Repo setup

- [ ] Create private repo on GitHub
- [ ] Add secret: GEMINI_API_KEY
- [ ] Add secret: GIST_TOKEN
- [ ] Add secret: GIST_ID

### Code

- [ ] Add requirements.txt
- [ ] Add main.py
- [ ] Add .github/workflows/daily_update.yml
- [ ] Push to GitHub

### Test

- [ ] Manually trigger the workflow
- [ ] Check that it passes
- [ ] Verify the Gist has real data

---

## Phase 2: Widget

### Scriptable

- [ ] Install Scriptable
- [ ] Create script called CryptoTick
- [ ] Paste widget code
- [ ] Update the Raw Gist URL

### Test

- [ ] Run script in Scriptable
- [ ] Check that the preview looks right

### Home screen

- [ ] Add Scriptable medium widget
- [ ] Set it to CryptoTick
- [ ] Done

---

## Optional stuff

- [ ] Add error handling to Python script
- [ ] Add retry logic
- [ ] Set up failure notifications
- [ ] Make a small widget version
- [ ] Add tap action

---

## Credentials

Keep these somewhere safe:

| What           | Value |
| -------------- | ----- |
| Gemini API Key |       |
| GitHub PAT     |       |
| Gist ID        |       |
| Raw Gist URL   |       |

---

## Links

- [Google AI Studio](https://aistudio.google.com/)
- [GitHub PAT settings](https://github.com/settings/tokens)
- [GitHub Gist](https://gist.github.com/)
- [Scriptable docs](https://docs.scriptable.app/)
