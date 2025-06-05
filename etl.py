import os
import json
import pandas as pd
import requests
import openai

API_URL = "https://sdw-2023-prd.up.railway.app"

openai.api_key = os.environ.get("OPENAI_API_KEY", "")

def get_user(user_id: int):
    """Fetch a user from the remote API."""
    response = requests.get(f"{API_URL}/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    return None

def generate_ai_news(user: dict) -> str:
    """Generate a CRM marketing message for a user via OpenAI."""
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em marketing CRM",
            },
            {
                "role": "user",
                "content": (
                    f"Crie uma mensagem para {user['name']}, persuadindo-o a "
                    "comprar em nossa loja (máximo de 100 caracteres)"
                ),
            },
        ],
    )
    return completion.choices[0].message.content.strip('"')

def update_user(user: dict) -> bool:
    """Send the updated user back to the API."""
    response = requests.put(f"{API_URL}/users/{user['id']}", json=user)
    return response.status_code == 200

def main():
    df = pd.read_csv("Extract.csv.txt")
    user_ids = df["User ID"].tolist()

    users = [u for uid in user_ids if (u := get_user(uid)) is not None]
    print(json.dumps(users, indent=2, ensure_ascii=False))

    for user in users:
        news = generate_ai_news(user)
        user.setdefault("news", []).append({"icon": None, "description": news})
        success = update_user(user)
        print(f"User {user['name']} updated? {success}")

if __name__ == "__main__":
    main()
