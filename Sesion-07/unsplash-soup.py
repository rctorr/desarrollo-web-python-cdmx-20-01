from bs4 import BeautifulSoup
import requests

# obtener el contenido de toda la página de google
respuesta = requests.get("https://unsplash.com/")

if respuesta.status_code == 200:
    sopa = BeautifulSoup(respuesta.content, features="html.parser")
    # Obtener el título
    print(sopa.title.string)
    # Obtener lista de imágenes
    for img in sopa.find_all("img"):
        # Filtrando sólo las fotos
        if "photo" in img["src"]:
            print(img["src"])
else:
    print("Error al obtener la página!", respuesta.status_code)
