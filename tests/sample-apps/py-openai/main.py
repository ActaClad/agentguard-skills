from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Reply with the word ready."}],
)

print(response.choices[0].message.content or "No response")
