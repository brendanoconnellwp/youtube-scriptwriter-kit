# Step 2: Summarize every video → data/mine/summaries.json, then build catalog.md

For every video in `data/mine/index.json`, read its transcript (`file` field) and write one entry to `data/mine/summaries.json`:

```json
{
  "<video id>": {
    "summary": "One sentence: what the viewer learns or gets. Under 20 words.",
    "topics": ["3 to 5 lowercase tags, specific to the niche in creator.md, e.g. wordpress, n8n, hosting, client-work"],
    "format": "tutorial | explainer | opinion | build-along | comparison | vlog | short"
  }
}
```

Rules:
- If summaries.json exists, **only add missing IDs**. Don't rewrite existing entries.
- Keep the tag vocabulary consistent. Reuse existing tags before inventing new ones.
- Work in batches of ~10 videos and save after each batch, so a long run can resume.
- If a video has no captions, summarize it from its title and description, and add `"note": "no transcript"`.

Then run:

```
py tools/build_catalog.py
```

Report: the number of videos summarized, the top 10 tags by count, and the 3 topics with the highest average views per video.
