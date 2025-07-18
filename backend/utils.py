import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_recommendations(user_input):
    prompt = f"""
    Based on this input: "{user_input}", generate 3 personalized cultural recommendations.
    Each item should include:
    - title
    - type (e.g. film, music, restaurant, fashion)
    - a short reason why it matches the user's taste.
    
    Respond in this JSON format:
    [
        {{
            "title": "...",
            "type": "...",
            "reason": "..."
        }},
        ...
    ]
    """
    
    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a cultural taste concierge."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )

    # Extract just the JSON string from the response
    try:
        import json
        text = response.choices[0].message.content.strip()
        recommendations = json.loads(text)
        return recommendations
    except Exception as e:
        return [{"title": "Error", "type": "debug", "reason": str(e)}]
