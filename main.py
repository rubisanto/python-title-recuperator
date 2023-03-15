import requests
from bs4 import BeautifulSoup


def title_recuperation(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        # if the adress is not valid
    except requests.exceptions.RequestException as e:
        return f"Erreur lors de l'accès à l'url: {e}"

    content = response.content

    soup = BeautifulSoup(content, 'html.parser')
    title = soup.find('title')

    if title:
        return title.text
    else:
        return 'title not found !'


url = input('entrer l\'url de la page : ')
title = title_recuperation(url)
print('le titre de la page est : ', title)
