import requests
from bs4 import BeautifulSoup

# Funzione per fare scraping di un sito
def scrape_website(url):
    # Fai una richiesta GET alla pagina web
    response = requests.get(url)
    
    # Verifica se la richiesta è andata a buon fine (status code 200)
    if response.status_code == 200:
        print(f"Successfully fetched the content from {url}")
        
        # Analizza il contenuto HTML della pagina
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Estrai il titolo della pagina
        title = soup.title.string
        print(f"Title of the page: {title}")
        
        # Estrai tutti i paragrafi
        paragraphs = soup.find_all('p')
        print(f"\nFound {len(paragraphs)} paragraphs:")
        for paragraph in paragraphs:
            print(paragraph.get_text())
        
        # Estrai tutte le immagini (url)
        images = soup.find_all('img')
        print(f"\nFound {len(images)} images:")
        for image in images:
            print(image.get('src'))
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")

# Funzione principale per eseguire lo scraper
def main():
    url = input("Enter the URL of the website you want to scrape: ")
    scrape_website(url)

# Esegui lo scraper se questo script è eseguito direttamente
if __name__ == "__main__":
    main()