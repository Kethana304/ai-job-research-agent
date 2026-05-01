import os
import time
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def agent_step(step_name, prompt):
    print(f"\n Agent Step: {step_name}")
    print("-" * 50)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    result = response.choices[0].message.content
    print(result)
    time.sleep(3)
    return result

print("=" * 60)
print("   AI JOB RESEARCH AGENT - by Kethana Harshitha")
print("=" * 60)

skills = agent_step(
    "Researching AI Engineer Skills",
    "What are the top 10 must-have skills for an AI Engineer in 2025? Be specific."
)

plan = agent_step(
    "Analyzing Fresher Roadmap",
    f"Based on these AI Engineer skills:\n{skills[:500]}\n\n"
    "Which 5 skills should a fresh graduate prioritize first and why?"
)

agent_step(
    "Generating 4-Week Learning Roadmap",
    f"Based on this priority list:\n{plan[:500]}\n\n"
    "Create a 4-week learning roadmap for a fresh AI graduate. "
    "Include free resources for each week."
)

print("\n" + "=" * 60)
print("  Agent Task Complete!")
print("=" * 60)