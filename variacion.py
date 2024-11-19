from openai import OpenAI

client = OpenAI()

response = client.images.create_variation(
    image=open("hd-vivid.png", "rb"),
    n=1,
    size="1024x1024",
    response_format="url"
)

print(response)
