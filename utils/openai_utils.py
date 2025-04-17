import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_gpt_response(user_prompt, model="gpt-3.5-turbo", temperature=0.7, max_tokens=512):
    system_prompt = "You are PeerGen, an AI text generation assistant."

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"