import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_feedback(name, analysis):
    prompt = f"""
    Student: {name}

    Average Score: {analysis['Average']}
    Strong Subject: {analysis['Strong']}
    Weak Subject: {analysis['Weak']}
    Subject Gaps: {analysis['Gaps']}

    Give short, practical advice to improve performance.
    Avoid generic statements.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
