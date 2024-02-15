# pip install requests
# pip install BeautifulSoup
# pip install BeautifulSoup4

import requests
from bs4 import BeautifulSoup

print ("Primer ejemplo de web scraping")

def get_price_ml(url_producto):
    # Realizar la solicitud HTTP y obtener el contenido de la página
    response = requests.get(url_producto)
    html_content = response.content

    # Creamos un objeto de BeautifulSoup pasando el html y parceamos el html 
    soup = BeautifulSoup(html_content, 'html.parser')

    precio_elemento = soup.find('span', class_='andes-money-amount__fraction')

    # Extraermos el texto del elemento de precio
    precio = precio_elemento.text if precio_elemento else 'No disponible'
    # Algunas veces puede que tengan tabuladores o saltos de linea.
    # Para solucionarlo podemos usar el metodo strip() que los quita
    # precio = precio_elemento.text.strip() if precio_elemento else 'No disponible'
    return precio


url_producto = 'https://www.mercadolibre.com.mx/apple-iphone-apple-a15-bionic-14-512gb-mr3t3ea-color-amarillo-distribuidor-autorizado/p/MLM1023038893?pdp_filters=category:MLM1055#searchVariation=MLM1023038893&position=3&search_layout=stack&type=product&tracking_id=f71db7fd-69b2-4eee-844f-8ad97a9bccb8'
precio = get_price_ml(url_producto)
print(f'El precio del iPhone 15 en Mercado libre es: {precio}')
