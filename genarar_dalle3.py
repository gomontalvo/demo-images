from openai import OpenAI
import base64

client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt="La imagen muestra un paisaje natural caracterizado por un cañón o un valle seco, con paredes de tierra y roca que se elevan a los lados. En el fondo, hay un lecho de río poco profundo, con charcos de agua reflejando el cielo. La vegetación es escasa, con algunas áreas verdes y arbustos creciendo en la tierra. En el horizonte, se puede ver una extensión de agua, sugiriendo la presencia de un lago o un cuerpo de agua más grande. El cielo está parcialmente nublado, creando un contraste interesante en la iluminación del entorno",
    n=1,
    size="1024x1024",
    response_format="url",
    quality="hd",
    style="natural"
)
print(response)
# ImagesResponse(created=1732055499, data=[Image(b64_json=None, revised_prompt='The image illustrates a natural landscape characterized by a canyon or dry valley, with earth and rock walls rising on the sides. In the background lies a shallow riverbed, with puddles of water reflecting the sky. Vegetation is sparse, with some patches of greenery and shrubs growing in the soil. In the horizon, a span of water is visible, hinting at the presence of a lake or larger body of water. The sky is partly cloudy, casting interesting contrasts of light across the scenery.',
#                url='https://oaidalleapiprodscus.blob.core.windows.net/private/org-EK0V852W3PDB287VAMCADWkh/user-ZaajrtLjSNXD8gL5QJRvLnEs/img-4Werc37JoiC5NI1TH3Xh6wmh.png?st=2024-11-19T21%3A31%3A39Z&se=2024-11-19T23%3A31%3A39Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-11-19T19%3A09%3A31Z&ske=2024-11-20T19%3A09%3A31Z&sks=b&skv=2024-08-04&sig=ZxQrffkmBA0QcdEvY6BBzr96noKFh%2Bzh%2B0lWE/kU14w%3D')])

response = client.images.generate(
    model="dall-e-3",
    prompt="La imagen muestra un paisaje natural caracterizado por un cañón o un valle seco, con paredes de tierra y roca que se elevan a los lados. En el fondo, hay un lecho de río poco profundo, con charcos de agua reflejando el cielo. La vegetación es escasa, con algunas áreas verdes y arbustos creciendo en la tierra. En el horizonte, se puede ver una extensión de agua, sugiriendo la presencia de un lago o un cuerpo de agua más grande. El cielo está parcialmente nublado, creando un contraste interesante en la iluminación del entorno",
    n=1,
    size="1024x1024",
    response_format="url",
    quality="hd",
    style="vivid"
)

print(response)

# ImagesResponse(created=1732055542, data=[Image(b64_json=None, revised_prompt="The picture encapsulates a natural landscape characterized by a canyon or a dry valley, with earthen and rock walls rising on either side. At the base, there's a shallow river bed, with puddles of water that mirror the sky. The vegetation is sparse, with occasional green patches and shrubs sprouting from the ground. The horizon reveals a stretch of water, indicating the presence of a lake or a larger water body. The sky is partly covered with clouds, creating an intriguing contrast in the environment's lighting.",
#                url='https://oaidalleapiprodscus.blob.core.windows.net/private/org-EK0V852W3PDB287VAMCADWkh/user-ZaajrtLjSNXD8gL5QJRvLnEs/img-m08nk1HD3xhtA3OC9TLMf6Gv.png?st=2024-11-19T21%3A32%3A22Z&se=2024-11-19T23%3A32%3A22Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-11-19T19%3A13%3A57Z&ske=2024-11-20T19%3A13%3A57Z&sks=b&skv=2024-08-04&sig=NDokcNXlL%2BaczXb4On/g2WZhwiQZtHThE83uyPN1JhE%3D')])
