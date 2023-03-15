
import requests
from bs4 import BeautifulSoup


def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'accès à l'URL: {e}")
        return None


def extract_title(content):
    soup = BeautifulSoup(content, 'html.parser')
    title = soup.find('title')

    if title:
        return title.get_text()
    else:
        return 'Titre non trouvé !'


def main():
    url = input("Entrez l'URL de la page : ")
    content = fetch_content(url)

    if content:
        title = extract_title(content)
        print('Le titre de la page est :', title)


if __name__ == "__main__":
    main()
