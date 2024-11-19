from openai import OpenAI
import base64

client = OpenAI()

enconded_string = ""
with open("logo.png", "rb") as image_file:
    enconded_string = base64.b64encode(image_file.read()).decode("utf-8")

description = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": "Eres un experto en describir logos"}, {
        "role": "user", "content": [
            {"type": "text", "text": "Describe el logo de la empresa"},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{enconded_string}"}}]}]
)
print(description)

image = client.images.generate(
    model="dall-e-3",
    prompt=description.choices[0].message.content,
    n=1,
    size="1024x1024",
    response_format="b64_json",
    quality="hd",
    style="vivid"
)

with open("logo_variacion.png", "wb") as image_file:
    image_file.write(base64.b64decode(image.data[0].b64_json))
print(image.data[0].revised_prompt)
