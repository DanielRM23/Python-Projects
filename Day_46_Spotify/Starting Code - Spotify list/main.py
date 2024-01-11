import requests
from bs4 import BeautifulSoup
#Estas librerias son para vinvular a Spotify
import spotipy
from spotipy.oauth2 import SpotifyOAuth



# Crea un input() que pregunta la fecha en la que se quiere obtener las canciones
# El formato aceptado es: YYY-MM-DD 
print("What year would you like to travel?")

# Me aseguro de que el año que se introduce es una cifra de 4 dígitos
year_flag = True
while year_flag:
    year = input("what is the year? (YYYY): ")
    if len(year) != 4:
        print("Write an acepted number")
        year_flag = True
    else:
        year_flag = False

# Me aseguro de que el mes que se introduzca sea un valor entre 1 y 12 además, 
# el dígito debe de ser de dos cifras 
month_flag = True
while month_flag:
    month = input("What is the month? (MM): ")
    if int(month)<0 or int(month)>12 or len(month) <=1:
        print("Write an acepted number")
        month_flag = True
    else:
        month_flag = False

# Me aseguro de que el día que se introduce es un valor entre 1 y 31 además
# de que el dígito debe de ser de dos cifras
day_flag = True
while day_flag:
    day = input("What is the day? (DD): ")
    if int(day)<0 or int(day)>31 or len(day) <=1 :
        print("Write an acepted number")
        day_flag = True
    else:
        day_flag = False

# Se tiene la fecha buscada 
date = f"{year}-{month}-{day}"

# Se accede al URL dada la fecha 
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

# Realizar una solicitud HTTP para obtener la página web de Billboard
response = requests.get(URL)
# En esta parte se extrae el contenido 
web_page = response.text

# Se crea la sopa 
# Se utiliza Beautiful Soup para analizar la página web y extraer los nombres de las canciones
soup = BeautifulSoup(web_page, "html.parser")

# Se extraen los tags de las canciones 
song_names_spans = soup.select("li ul li h3")

# Nombres de las canciones
song_names = [song.getText().strip() for song in song_names_spans]

# Se vincula a Spotify
# Autenticación en Spotify utilizando Spotipy
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",  # El alcance de la autenticación, permite modificar listas de reproducción privadas
        redirect_uri="http://example.com",  # URL de redirección después de la autorización en Spotify
        client_id="41f28d2cadaf4191bb9f469d8eaacd94",  # ID único del cliente de la aplicación en Spotify
        client_secret="c062af7cf37c4f0f9d9e61a369e9f467",  # Secreto del cliente de la aplicación en Spotify
        show_dialog=True,  # Mostrar un cuadro de diálogo de autorización (True para mostrar)
        cache_path="token.txt"  # Ruta donde se almacenará el token de autenticación
    )
)

# Obtener el ID de usuario de Spotify actual
user_id = sp.current_user()["id"]
print(user_id)

# Buscar en Spotify las canciones por título y año, luego obtener sus URI
    # Un URI (Uniform Resource Identifier) es una cadena de caracteres que identifica un nombre o recurso en la web de manera única
    # Los URIs se utilizan para identificar de manera única las canciones dentro de la plataforma de Spotify.  
song_uris = []
year = date.split("-")[0]  # Extraer el año de la fecha proporcionada
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")  # Búsqueda de la canción en Spotify
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]  # Obtener el URI de la primera coincidencia de la búsqueda
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Crear una nueva lista de reproducción privada en Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Agregar las canciones encontradas a la nueva lista de reproducción en Spotify
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)







