import requests
from bs4 import BeautifulSoup

# URL de la página web con los títulos de películas
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Realizar solicitud HTTP y extraer contenido HTML
response = requests.get(URL)
# En esta parte se extrae el contenido 
web_page = response.text

# Crear objeto BeautifulSoup para facilitar el análisis del HTML
# Se crea la sopa
soup = BeautifulSoup(web_page, "html.parser")

# Encontrar todas las etiquetas h3 con la clase 'title' que contienen títulos de películas
tags = soup.findAll(name="h3", class_="title")

# Crear una lista de títulos de películas
movies_titles = [tag.getText() for tag in tags]

# Ordenar la lista de títulos en orden inverso
movies_titles_ordered = movies_titles[::-1]

# Nombre del archivo de texto
nombre_archivo = "movies_titles_ordered.txt"

#Se guardan los elementos en un archivo de texto
# Abrir el archivo en modo de escritura
with open(nombre_archivo, "w") as archivo:
    # Escribir cada título de película en una nueva línea dentro del archivo
    for titulo in movies_titles_ordered:
        archivo.write(titulo + "\n")

# Confirmar que el archivo ha sido creado
print(f"Se ha creado el archivo: {nombre_archivo}")