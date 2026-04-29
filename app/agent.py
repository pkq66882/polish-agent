from openai import OpenAI
import json
from app.config import OPENAI_API_KEY, MODEL
from app.prompts import SYSTEM_PROMPT, POLISH_TEMPLATE

client = OpenAI(api_key=OPENAI_API_KEY)

class PolishAgent:
    def __init__(self):
        self.model = MODEL

    def polish(self, text: str):
        prompt = POLISH_TEMPLATE.format(text=text)

        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )

        content = response.choices[0].message.content

        try:
            return json.loads(content)
        except:
            return {
                "formal": content,
                "neutral": content,
                "friendly": content
            }
