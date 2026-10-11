# Step 3: Build the growth playbook → skill/youtube-scriptwriter/playbook.md

Inputs:
- `data/research/<creator>/`: top videos from creators the channel owner wants to learn from (listed in `research-channels.txt`).
- `data/mine/` + `data/mine/studio.csv` (if present): their own channel, the most relevant data of all.
- `skill/youtube-scriptwriter/creator.md`: who the creator is and their niche. Read it first.

**Ground rule:** extract *patterns*, never content. The playbook may name a technique ("cold open on the finished result") and cite where you saw it, but must not include another creator's scripts, bits, catchphrases or more than a few words of quotation. The goal is for the creator to sound more like themselves, done well, not like them.

## Analyze
For each research creator, read their transcripts and note:
1. **Hook (first ~30s):** the type (result-first, problem/stakes, contrarian claim, question, story, stunt), time until the promise is stated, and time until the first visual proof.
2. **Structure:** section count, segment lengths, where the first payoff lands, and how the end is handled.
3. **Retention devices:** open loops, pattern interrupts, re-hooks mid-video, stakes raised, callbacks.
4. **Titles:** the formulas behind their top videos (ranked by views). Note how titles and topics differ between their top 3 and their median.
5. **Packaging:** from titles and descriptions, the recurring promise shapes ("X in Y minutes", "I tried...", "Stop doing X").

Then do the same for **the creator's own channel**: what their ★ videos (catalog.md) do differently from their bottom third in hook, topic, title, length and format. If studio.csv exists, use CTR and average % viewed. This section matters most.

## Write `playbook.md` (remove the STATUS line), under ~2,000 words:
1. **What works on this channel.** Evidence-based findings from their own data.
2. **Hook types.** 6 to 8 named hook types, each with a one-line description, when to use it, and a *freshly written* example on a topic from their niche.
3. **Structures.** 3 to 4 reusable video skeletons (tutorial, explainer, opinion, build-along) with beat timings.
4. **Retention toolkit.** Named devices with a one-line how-to each.
5. **Title formulas.** 8 to 12, each as a pattern with a fresh example. Flag which ones fit their audience.
6. **Thumbnail principles.** Only what you can infer. Don't invent.
7. **Per-creator notes.** 3 to 5 bullets each: what's worth borrowing structurally, and what doesn't fit this creator.
8. **Topic gaps.** Topics the research creators do well that their catalog lacks, especially where they overlap the niche in creator.md.

Print the 5 most actionable findings when you're done.
