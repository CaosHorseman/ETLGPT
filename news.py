try:
    import openai
except ImportError:  # pragma: no cover
    openai = None


def generate_ai_news(user):
    """Generate marketing news message for the given user."""
    if openai is None:
        raise ImportError("openai package is required")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em marketing CRM",
            },
            {
                "role": "user",
                "content": f"Crie uma Mensagem para {user['name']}, persuadindo ele a comprar em nossa loja (máximo de 100 caracteres)",
            },
        ],
    )
    return completion.choices[0].message.content.strip('"')

