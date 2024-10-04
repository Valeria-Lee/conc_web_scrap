import requests
from bs4 import BeautifulSoup
import time

def main():
    search_input = input("Ingresa algun campo a buscar: -> ")

    if search_input != "":
        url = f'https://en.wikipedia.org/wiki/{search_input}'
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            print("conexion exitosa!")
            soup = BeautifulSoup(respuesta.text, 'html.parser')

            definitions = soup.find_all('p')

            for definition in definitions:
                if not definition.has_attr('class'):
                    print(definition.get_text())
                    break
        else:
            print("error en la peticion")
    else:
        print("La busqueda no es correcta")
        time.sleep(2)
        main()

if __name__ == '__main__':
    main()