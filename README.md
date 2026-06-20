# 🤖 AI Job Research Agent

An autonomous multi-step agent that takes a vague goal — "become job-ready as an AI Engineer" — and turns it into a concrete, personalized 4-week learning roadmap.

## Why I built it this way

Instead of asking an LLM to "just plan it" in one shot, I explicitly decomposed the task into three stages before writing any code:

1. **Research** — identify the current in-demand skills for AI Engineer roles
2. **Prioritize** — rank those skills by relevance for a fresher's starting point
3. **Generate** — build a 4-week roadmap with concrete, free resources per skill

Each stage gets a narrow, single job and its own prompt. [Replace with your real finding: e.g., "Output got noticeably more coherent once I split planning into these stages — single-shot planning kept producing vague or repetitive roadmaps."]

## Tech Stack
- Python
- Groq API (LLaMA 3.3 70B) for fast inference
- Multi-step task decomposition (no agent framework — built the orchestration logic myself)

## Example Output
[Paste one real roadmap output here — even a partial example makes this far more credible]

## Run it
\`\`\`bash
pip install groq python-dotenv
python job_agent.py
\`\`\`
