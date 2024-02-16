# Importar el módulo requests para realizar solicitudes HTTP
import requests
# Importar el módulo BeautifulSoup para analizar el contenido HTML
from bs4 import BeautifulSoup

# Imprimir un mensaje de introducción
print ("Segundo ejercicio de web scraping")
print ("Sacar el correo de la pagina del tec de morelia")

# Definir una función que obtiene el precio de un producto en MercadoLibre
def get_price_ml(url_correo):
    """
    Obtiene el precio de un producto en MercadoLibre a partir de su URL.

    Parameters:
    url_producto (str): La URL del producto en MercadoLibre.

    Returns:
    str: El precio del producto o 'No disponible' si no se encuentra.

    """
    # Realizar la solicitud HTTP y obtener el contenido de la página
    response = requests.get(url_correo)
    html_content = response.content

    # Creamos un objeto de BeautifulSoup pasando el html y parceamos el html 
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encontrar el elemento que contiene el precio
    url_correo = soup.find('br', attrs={'_ngcontent-sbh-c3': ''})

    # Extraer el texto del elemento de precio
    correo = url_correo.text if url_correo else 'No disponible'
    # Algunas veces puede que tengan tabuladores o saltos de linea.
    # Para solucionarlo podemos usar el metodo strip() que los quita
    # precio = precio_elemento.text.strip() if precio_elemento else 'No disponible'
    return correo

# Asignar la URL de un producto en MercadoLibre a una variable
url_correo = 'https://www.morelia.tecnm.mx/#/'
# Llamar a la función get_price_ml con la URL del producto y guardar el resultado en una variable
correo = get_price_ml(url_correo)
# Imprimir el precio del producto usando una cadena formateada
print(f'El correo de la institucion es: {correo}')

