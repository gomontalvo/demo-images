from openai import OpenAI
import base64

client = OpenAI()

response = client.images.generate(
    model="dall-e-2",
    prompt="La imagen muestra un paisaje natural caracterizado por un cañón o un valle seco, con paredes de tierra y roca que se elevan a los lados. En el fondo, hay un lecho de río poco profundo, con charcos de agua reflejando el cielo. La vegetación es escasa, con algunas áreas verdes y arbustos creciendo en la tierra. En el horizonte, se puede ver una extensión de agua, sugiriendo la presencia de un lago o un cuerpo de agua más grande. El cielo está parcialmente nublado, creando un contraste interesante en la iluminación del entorno",
    n=1,
    size="1024x1024",
    response_format="b64_json"
)
print(response)

image_data = response.data[0].b64_json
with open("ejemplo2.png", "wb") as image_file:
    image_file.write(base64.b64decode(image_data))

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
