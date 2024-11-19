from openai import OpenAI

client = OpenAI()

response = client.images.generate(
    model="dall-e-2",
    prompt="A beautiful landscape with a river and mountains",
    n=1,
    size="1024x1024",
    response_format="url"
)
print(response)

descripcion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Eres un experto en describir imagenes"},
        {"role": "user", "content": [
            {"type": "text", "text": "Describe la imagen"},
            {"type": "image_url", "image_url": {"url": response.data[0].url}}]}
    ]
)


print(descripcion)
