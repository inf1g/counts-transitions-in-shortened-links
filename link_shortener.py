import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def configure_keys(token):
    load_dotenv()
    key = os.environ[token]
    return key


def is_shorten_link(url):
    return urlparse(url).netloc == "vk.cc"


def shorten_link(link, vk_api_key):
    url = "https://api.vk.ru/method/utils.getShortLink"
    payload = {"v": "5.199", "access_token": {vk_api_key}, "url": {link}}
    response = requests.get(f"{url}", params=payload)
    response.raise_for_status()
    return response.json()['response']['short_url']


def count_clicks(short_url, vk_api_key):
    url_path = urlparse(short_url).path.replace('/', '')
    url = "https://api.vk.ru/method/utils.getLinkStats"
    payload = {"v": "5.199", "access_token": {vk_api_key}, "key": {url_path}, "interval": "forever", "extended": "0"}
    response = requests.get(f"{url}", params=payload)
    response.raise_for_status()
    return response.json()["response"]["stats"][0]["views"]


def main():
    vk_api_token = configure_keys("VK_API_KEY")
    user_input = input("Введите URL-адрес: ")
    try:
        if is_shorten_link(user_input):
            print(f'Количество кликов по ссылке: {count_clicks(user_input, vk_api_token)}')
        if not is_shorten_link(user_input):
            print(f'Сокращенная ссылка: {shorten_link(user_input, vk_api_token)}')
    except requests.exceptions.HTTPError:
        print('Неверная ссылка')


if __name__ == '__main__':
    main()
