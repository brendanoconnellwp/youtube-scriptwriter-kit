# Growth playbook

Built mainly from Brendan's own channel: 101 long-form videos (Oct 2022 to Aug 2026), their transcripts, and a lifetime YouTube Studio export. Two research creators (Creator A, Creator B; top 15 videos each) add structural ideas in sections 7 and 8. Brendan picked them as examples, not north stars: **when his own data and theirs disagree, his data wins.**

Numbers below are medians unless stated. "Top" = top 20% by views (20 videos, ≥ 4,583 views). "Bottom" = bottom third (34 videos).

## 1. What works on this channel

**1. Packaging decides everything. Delivery doesn't.**
| | Top 20% | Bottom third |
|---|---|---|
| Thumbnail CTR | **7.6%** | 3.0% |
| Impressions | 64k | 8k |
| Avg % viewed | 16% | 23% |
| Subs gained | 76 | 3 |

The winners don't hold viewers better; they get clicked 2.5x more, so YouTube shows them 8x more. His delivery (fillers, on-camera debugging) is the same in both groups. Spend effort on topic, title and the first 30 seconds.

**2. Winning topics: broad AI/automation tools, with money or independence at stake.** n8n (median 5.5k views across 10 videos), OpenRouter (44k), bring-your-own-key, Coolify self-hosting, WooCommerce and Airtable AI agents. Also: complete Bricks how-tos on visual topics (full site build 16k, GSAP 10.7k).

**3. "Free / open source alternative to [big name]" is his strongest frame.** OpenWhispr (vs WisprFlow) has the channel's best CTR at 10.5%. Paper vs Pencil (Figma alternatives) 22k. Open Design (vs Claude Design) 7.3k. Ditch Google Analytics 6.3k.

**4. What floors:** niche tools most viewers haven't heard of (Pinegrow, Toddle, Bitflows, Remote Data Blocks, AgentsView), sequels ("Part 2"), raw drafts ("first draft"), and personal show-and-tell ("Claude Fable helped me create this plugin", "I Left Claude Fable Alone and It Built 25 Websites"). Both first-person experiment titles are in the bottom 15. On this channel "I tried X" underperforms; "here's how you do X" wins.

**5. Length is not the problem. Completeness is a feature.** Videos over 25 minutes have the highest median views (3.9k) and subs (51) despite ~10% retention. They're searchable "full tutorial" references. Under 8 minutes: best retention (37%), lowest reach.

**6. A clear stance converts subscribers.** Opinion videos (n=4) gain a median 87 subs. "STOP Paying for AI Subscriptions" and "Why You NEED Automation & AI in 2025" earn far more subs per view than the tutorials.

**7. Openings.** From the transcripts: top videos name a concrete outcome or an "alternative to X" frame in the first sentence and show the working result within 30 to 90 seconds. Weak ones open on meta ("my camera's looking off to the side"), vague intent ("I just wanted to share some things I've been working on") or a surveyed list.

**8. Repackaging candidates.** High impressions, low CTR. New title and thumbnail could revive these:
- Bricks + Bricksforge: GSAP Animations & Timelines: 159k impressions, 1.4% CTR
- Remote Data Blocks Part 2 (Airtable): 16k impressions, 0.9% CTR
- 9 n8n Features You Might Have Missed: 10k impressions, 1.4% CTR

2026 videos have healthy CTR (5.0%) but fewer impressions so far. They're young; judge them again in six months.

## 2. Hook types

Every hook is 2 to 4 spoken sentences, states the promise inside 15 seconds, and follows `voice.md`.

1. **Result first.** Show the finished thing, then say you'll build it. *Use for:* tutorials and automations. *Example:* "This form just wrote a blog post, generated the featured image and published it to WordPress. No copy and paste. I'll show you how to build the whole flow in n8n."
2. **The alternative.** Name the big tool, then the free/open one. *Use for:* tool explainers. His strongest hook. *Example:* "Claude Design is cool, but it eats your usage limits. There's an open source version that runs on your own API key, and I've been using it all week."
3. **Stop paying / stop doing.** Name a cost or chore the viewer has, then the fix. *Use for:* opinion and money topics. *Example:* "If you're paying for three AI subscriptions, you're probably wasting money. One API key gets you every model, and most months it costs me a few dollars."
4. **Viewer question.** Open on a real question he's been asked. *Use for:* comparisons. *Example:* "People keep asking me if I build Bricks sites with Claude Code or by hand. So I built the same page both ways."
5. **News, then what it means for you.** Only when the news is big and the payoff is practical. *Use for:* major releases. *Example:* "Anthropic just shipped agent skills. For WordPress developers, that means Claude stops guessing how your site is set up."
6. **Client problem.** A real client request, then the fix. *Use for:* WordPress workflow tutorials. *Example:* "A client wanted their Google reviews on the homepage, updated automatically. Here's how I did it without a plugin."
7. **The honest take.** A clear stance up front. *Use for:* opinion videos (these grow subs). *Example:* "Most AI website builders are making the same page over and over. Here's where I think they're actually useful, and where they're not."
8. **The skeptical test.** A claim everyone is repeating, then "let's actually try it." *Use for:* launch-week reviews of new AI releases. *Example:* "Everyone's saying Claude can build a full WordPress site now. I gave it a real client brief and a Bricks install. Here's what it got right and what I had to fix."

Avoid "I tried X" and "I left AI alone and..." as the main hook. On this channel, the experiment frame loses to the how-to frame.

## 3. Structures

**Tutorial (15 to 20 min, his best performers):**
- 0:00 Hook: result first (see above).
- 0:30 What it is, in one line, and who it's for. What you need (accounts, keys, plugins).
- 1:30 The plan, said out loud: "we're going from X to Y to Z."
- 2:00 Build, in 3 to 5 chunks. Each ends with a visible win ("There it is.").
- First payoff by 4:00. Sponsor slot after it, never before.
- Last 2 min: spoken recap of the flow, one gotcha, a question to the viewer, pointer to the related video.

**Alternative/tool explainer (8 to 14 min):**
- 0:00 The alternative hook plus proof on screen.
- 0:45 What it is, what it costs, what it replaces.
- 2:00 Tour of the 3 features that matter, each shown doing real work.
- 8:00 Honest limits: where the paid tool still wins.
- Close: who should switch, who shouldn't.

**Opinion (12 to 18 min):**
- 0:00 Stance in one sentence.
- 0:30 Why it matters now (cost, lock-in, speed).
- 2:00 Three reasons, each backed by something on screen (a bill, a demo, a result).
- Middle: the counterargument, taken seriously.
- Close: what he'd do, then ask viewers where they land.

**Options with a verdict (10 to 16 min):** for "how do I do X" topics with several routes.
- 0:00 Finished result on screen, plus the constraint ("just Bricks and one MCP, no add-ons").
- 0:45 Route 1, the obvious way. Show where it falls short.
- Route 2 and 3, each with a quick verdict (fastest / most flexible / what I'd ship to a client).
- Close: the one he'd pick and why.

**Build-along / full tutorial (30+ min, a search reference):**
- 0:00 Finished site or app on screen, the stack named.
- 1:00 Chapters said out loud, so viewers know they can jump.
- Build in chapter-sized chunks with a re-hook at each ("Next, the part most people skip: the query loop.").
- Speed up or cut the waits and say so.
- Close: recap the stack, link the template or repo if there is one.

## 4. Retention toolkit

Keep these in his voice. No "stay till the end."
- **Proof in the first 30 seconds.** The finished result on screen before any setup.
- **Say the plan.** One sentence mapping the route, so viewers know where they are.
- **Chunked wins.** End each section with something visibly working.
- **Honest open loop.** "There's one setting at the end that makes this actually usable for clients." Then pay it off.
- **The gotcha.** "Here's where it breaks for most people." His on-camera debugging, framed on purpose.
- **Naive first, then better.** Try the obvious prompt or method, show it fall short, then show what works. Teaches and holds attention.
- **Constraint stack.** Say what the viewer won't need ("no plugin, no code") in the first 30 seconds.
- **Price check.** Say what it cost ("that run was 20 cents"). His audience cares, and it resets attention.
- **Agent wait cuts.** Cut or speed up agent runs, and say how long they really took.
- **Callback.** Point to one specific past video from the catalog, not a generic "check out my other videos."

## 5. Title formulas

✅ = proven on this channel. ⚠️ = untested or mixed. ❌ = underperformed here.

1. ✅ **[Tool]: [concrete outcome] ([qualifier])**: "OpenRouter: Easily access multiple AI models (including FREE ones)". *Fresh:* "WP-CLI for Claude Code: Let Agents Manage WordPress Safely"
2. ✅ **Free/Open Source [X] Alternative [that does Y]**: *Fresh:* "Free Open Source Zapier Alternative You Can Self Host"
3. ✅ **STOP [costly habit]! [fix]**: *Fresh:* "STOP Hand-Coding WordPress Themes: Let Claude Code Do It"
4. ✅ **This [open source] Tool Replaces [big name]**: *Fresh:* "This Open Source Tool Replaces Google Search Console"
5. ✅ **Create [specific thing] for [platform] with [tool]**: *Fresh:* "Create an AI Support Agent for WordPress with n8n"
6. ✅ **[A] vs [B]: [what's being decided]**: *Fresh:* "Claude Code vs Cursor for WordPress Development"
7. ✅ **[Outcome] (FULL TUTORIAL)**: *Fresh:* "Build a Directory Site with Bricks and ACF (FULL TUTORIAL)"
8. ✅ **It's Time to Ditch [big name] ([reason])**: *Fresh:* "It's Time to Ditch Page Builder Templates (Agents Do It Better)"
9. ⚠️ **Why You NEED [X] in [year]**: high subs, modest views. Use for opinion pieces.
10. ⚠️ **[Tool] + WordPress: [outcome]** for Claude Code topics. Agent Skills (8.7k) worked; personal plugin demos didn't.
11. ❌ **Numbered lists** ("9 n8n Features You Might Have Missed", 1.4% CTR).
12. ❌ **First-person experiments** ("I Left Claude Fable Alone and It Built 25 Websites"), **"Part 2"**, **"first draft"**, and **"coming in [version]"** news titles.

Keep titles under 60 characters where possible. Put the big, known name (n8n, Claude Code, WordPress, Figma, Google) in the first half.

## 6. Thumbnail principles

There's no thumbnail data in the kit, so this is limited to what CTR shows:
- The known brand in the title should be visible in the thumbnail too. Nearly every 8%+ CTR video names a tool or platform people already search for.
- Promise a money or independence payoff ("FREE", "replaces X"). Those frames hold the top CTRs.
- To go further, save thumbnails for the top 10 and bottom 10 videos in `data/mine/thumbs/` and re-run this step.

## 7. Per-creator notes

Examples, not models. Borrow structure only; never their lines, bits or catchphrases.

**Creator A** (a WordPress page-builder tutorial channel, now covering Claude Code + WordPress)
- Their Claude Code in WordPress video is growing about 3x faster per month than anything else on that channel. Strong signal for Brendan's lane.
- Borrow: result on screen at 0s, then the constraint stack. Options-with-verdicts structure ("three ways, here's the one I'd use").
- Borrow: code, prompts and files hosted on his own site, linked in the first line of the description. Skills, CLAUDE.md files and n8n templates make good lead magnets.
- Borrow: crediting commenters for video ideas; teasing the next video in a series.
- Skip: 60 to 90 second intros with subscribe and affiliate asks, first payoff 5 to 10 minutes in, click-by-click beginner narration.

**Creator B** (a web design channel covering design tools, AI builders and AI video)
- Promise in the first sentence, finished site playing from 0s, first build step at about 1:50. Fixed pipeline: brief, assets, build, small follow-up prompts, mobile check, deploy, reveal.
- His #1 video is a skeptical launch-week test with no hype word in the title. The winners name a brand-new release, not an adjective.
- Borrow: naive first, then better. Honest closing beats (AI gets you most of the way, what it costs, what's missing).
- Skip: "Insane," "GENIUS" titles, sponsor-led topic picks, flashy fictional concept sites, hashtag-stuffed descriptions.
- Where he stops, Brendan starts: CMS, client editing, WordPress and automation are the "part 2" he never makes.

## 8. Topic gaps

From the research plus his own data:
- **Claude Code + WordPress how-tos,** Bricks-specific: setup (CLAUDE.md, skills, WP-CLI, MCP), what breaks, safe-edit guardrails. Proven on both his channel (Agent Skills, 8.7k) and Creator A's fastest-growing video. Frame as how-to, not "Claude helped me build this."
- **Design to real WordPress site:** Claude Design or Figma, handed to Claude Code, landing in Bricks with a real CMS behind it. The step the design channels skip.
- **Launch-week skeptical tests** of new Claude and AI builder releases, framed for WordPress devs.
- **n8n + WordPress, updated for agents and MCP.** His best topic cluster, nothing new since Sept 2025.
- **Agent QA:** an agent audits a site before launch and files the fixes (n8n or Claude Code).
- **Evergreen components built by an agent in Bricks:** mobile menus, sticky headers, query loops and filters, WooCommerce grids. Search magnets.
- **Opinion pieces** (only 4 so far; they gain the most subs per view) and **open source alternatives to paid AI tools** (every attempt has performed).
