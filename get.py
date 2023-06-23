import requests


def get_text(url):
    get = requests.get(url)
    text = get.text
    return text