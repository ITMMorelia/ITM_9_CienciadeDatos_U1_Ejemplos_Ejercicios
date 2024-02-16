# Importar el módulo requests para realizar solicitudes HTTP
import requests
# Importar el módulo BeautifulSoup para analizar el contenido HTML
from bs4 import BeautifulSoup

# Imprimir un mensaje de introducción
print ("Primer ejercicio de web scraping")

# Definir una función que obtiene el precio de un producto en MercadoLibre
def get_price_ml(url_producto):
    """
    Obtiene el precio de un producto en MercadoLibre a partir de su URL.

    Parameters:
    url_producto (str): La URL del producto en MercadoLibre.

    Returns:
    str: El precio del producto o 'No disponible' si no se encuentra.

    """
    # Realizar la solicitud HTTP y obtener el contenido de la página
    response = requests.get(url_producto)
    html_content = response.content

    # Creamos un objeto de BeautifulSoup pasando el html y parceamos el html 
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encontrar el elemento que contiene el precio
    precio_elemento = soup.find('span', class_='a-price-whole')

    # Extraer el texto del elemento de precio
    precio = precio_elemento.text if precio_elemento else 'No disponible'
    # Algunas veces puede que tengan tabuladores o saltos de linea.
    # Para solucionarlo podemos usar el metodo strip() que los quita
    # precio = precio_elemento.text.strip() if precio_elemento else 'No disponible'
    return precio

# Asignar la URL de un producto en MercadoLibre a una variable
url_producto = 'https://www.amazon.com.mx/dp/B09RHX59P6/?coliid=IFCCI5VGR10UM&colid=2OK69FGKN3DQO&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it_im'
# Llamar a la función get_price_ml con la URL del producto y guardar el resultado en una variable
precio = get_price_ml(url_producto)
# Imprimir el precio del producto usando una cadena formateada
print(f'El precio de la pantalla portatil de Xbox Series S es: {precio}')

