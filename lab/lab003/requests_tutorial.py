from rich.console import Console
import rich.traceback
import requests
from bs4 import BeautifulSoup

console = Console()
console.clear()
rich.traceback.install()

req = requests.get('https://www.imdb.com/name/nm0001569/')
# console.print(req.status_code)
# console.print(req.headers)
# console.print(req.request.headers)
# console.print(req.text)

soup = BeautifulSoup(req.text, 'html.parser')
divs_film_cayegory = soup.find('div', class_ = 'filmo-category-section')
divs_films = divs_film_cayegory.find_all('div', class_ = 'filmo-row')

for div in divs_films:
    console.print(f"{div.find('span').text.strip() = } {div.find('a').text.strip() = } {div.find('a')['href']}")
    
