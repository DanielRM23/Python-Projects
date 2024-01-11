from bs4 import BeautifulSoup
import requests 

# Realizar la solicitud HTTP para obtener el contenido de la página web
response = requests.get("https://news.ycombinator.com/")
# Obtener el contenido HTML de la página
yc_web_page = response.text

# Crear un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(yc_web_page, "html.parser")

# Seleccionar todas las etiquetas <a> dentro de la clase "titleline"
tags = soup.select(".titleline a")

# Obtener textos y enlaces de las historias, excluyendo los que comienzan con 'from'
tag_texts = [tag.getText() for tag in tags if not tag.get("href", "").startswith('from')]
tag_links = [tag.get("href") for tag in tags if not tag.get("href", "").startswith('from')]

# Obtener puntuaciones de las historias
tag_scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# Observación:
# Revisando el sitio web, se encuentra que hay una página que no cuenta con un score,
# por lo que se presenta una discrepancia en las longitudes de las listas.

# Eliminar el elemento que no cuenta con score
del tag_texts[16]
del tag_links[16]

# ELEGIR EL ENLACE CON MAYOR SCORE
# Encontrar el índice del score más grande
largest_score = max(tag_scores)
largest_index = tag_scores.index(largest_score)

# Imprimir el título y el enlace de la historia con el puntaje más alto
print("Título con mayor puntaje:", tag_texts[largest_index])
print("Enlace con mayor puntaje:", tag_links[largest_index])
