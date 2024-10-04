import requests
from bs4 import BeautifulSoup
import asyncio 
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            print("La busqueda no es correcta")
            return None

async def scrape_from_wikipedia(search_input):
    url = f'https://en.wikipedia.org/wiki/{search_input}'
    async with aiohttp.ClientSession() as session:
        html_content = await fetch(session, url)
        if html_content:
            soup = BeautifulSoup(html_content, 'html.parser')
            definitions = soup.find_all('p')

            for definition in definitions:
                if not definition.has_attr('class'):
                    print(definition.get_text())
                    break

def main():
    search_input = input("Ingresa una busqueda: -> ")

    if search_input:
        asyncio.run(scrape_from_wikipedia(search_input))
    else:
        print("La busqueda no es correcta")
        asyncio.run(main())

if __name__ == '__main__':
    main()