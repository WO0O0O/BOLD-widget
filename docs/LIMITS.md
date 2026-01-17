# Usage Limits & Monitoring

Quick reference for free tier limits and expected usage.

---

## GitHub Actions

| Metric        | Free Tier Limit | Your Usage    |
| ------------- | --------------- | ------------- |
| Minutes/month | 2,000           | ~60-90 mins   |
| Runs/month    | -               | ~1,440        |
| Frequency     | -               | Every 30 mins |

**Calculation:**

- 30 mins = 48 runs/day = 1,440 runs/month
- Each run ~30-60 seconds
- Monthly usage: ~720-1,440 minutes (well under 2,000)

**Monitor:** [GitHub Actions Usage](https://github.com/settings/billing)

---

## Gemini API (Free Tier)

| Metric       | Free Tier Limit | Your Usage |
| ------------ | --------------- | ---------- |
| Requests/min | 10              | 1          |
| Requests/day | 500             | 48         |
| Tokens/min   | 250,000         | ~10,000    |

**Model:** gemini-2.0-flash

> **Note:** gemini-2.5-flash has only 20 RPD on free tier. We use 2.0-flash for its 500 RPD limit.

**Monitor:** [Gemini Rate Limits](https://ai.dev/rate-limit)

---

## CoinGecko API (Free, No Key)

| Metric       | Limit     | Your Usage |
| ------------ | --------- | ---------- |
| Requests/min | 10-30     | 1          |
| Requests/day | Unlimited | 48         |

No API key required for basic price endpoint.

---

## DuckDuckGo Search

| Metric     | Limit      | Your Usage      |
| ---------- | ---------- | --------------- |
| Rate limit | Soft limit | ~20 queries/run |

No API key. Uses ddgs Python library (web scraping).

---

## GitHub Gist

| Metric    | Limit     |
| --------- | --------- |
| File size | 10 MB     |
| Gists     | Unlimited |

Your JSON file is ~2-3 KB — no concerns.

---

## Expected Monthly Summary

| Service        | Expected Usage  | % of Free Tier     |
| -------------- | --------------- | ------------------ |
| GitHub Actions | ~90 mins        | 4.5%               |
| Gemini API     | ~1,440 requests | ~3% of daily limit |
| CoinGecko      | ~1,440 requests | N/A (no limit)     |

**Verdict:** You're using a tiny fraction of all free tiers.

---

## Secrets Stored

| Secret         | Location            | Purpose           |
| -------------- | ------------------- | ----------------- |
| GEMINI_API_KEY | GitHub Repo Secrets | Gemini API access |
| GIST_TOKEN     | GitHub Repo Secrets | Update Gist       |
| GIST_ID        | GitHub Repo Secrets | Gist identifier   |

---

## Monitoring Links

- [GitHub Actions Runs](https://github.com/WO0O0O/Market-News-Widget/actions)
- [Gemini Rate Limits](https://ai.dev/rate-limit)
- [Your Gist](https://gist.github.com/WO0O0O/43171059615e0008db423e0ace9e8e6a)

---

## If Something Breaks

| Issue             | Likely Cause                   | Fix                        |
| ----------------- | ------------------------------ | -------------------------- |
| Workflow fails    | API rate limit or bad response | Wait 15 mins, retry        |
| Gist not updating | Token expired                  | Regenerate PAT             |
| Prices wrong      | CoinGecko down                 | Will auto-recover next run |
| Widget error      | JSON structure changed         | Check Gist data            |
