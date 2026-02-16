from openai import OpenAI
from config import Config
import json

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)

    def analyze_email(self, email_text: str, prompt_template: str) -> dict:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt_template},
                {"role": "user", "content": email_text}
            ],
            response_format={"type": "json_object"},
            temperature=0
        )
        
        content = response.choices[0].message.content
        return json.loads(content)