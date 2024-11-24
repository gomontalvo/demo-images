from openai import OpenAI

client = OpenAI()

response = client.images.generate(
    model = "dall-e-2",
    prompt = "A beatiful landscape with a rvier and mountain",
    n=1,
    size="1024x1024",
    response_format="url"
)

print(response)