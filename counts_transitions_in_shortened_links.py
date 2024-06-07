import requests
import os
import time
from dotenv import load_dotenv
from urllib.parse import urlparse


def configure_keys(token):
    load_dotenv()
    key = os.getenv(token)
    return key


def is_shorten_link(url):
    parsed = urlparse(url)
    if parsed.scheme == 'https' or parsed.scheme == 'http':
        if urlparse(url).netloc == "vk.cc":
            count_clicks(url)
        else:
            shorten_link(url)
    else:
        print("Введите полный URL как на примере: https://ya.ru")


def shorten_link(link):
    url = "https://api.vk.ru/method/utils.getShortLink"
    payload = {"v": "5.199", "access_token": vk_api_key, "url": {link}}
    response = requests.get(f"{url}", params=payload)
    try:
        response.raise_for_status()
        print(f'Сокращенная ссылка: {response.json()['response']['short_url']}')
        return response.json()['response']['short_url']
    except requests.exceptions.HTTPError:
        print(f'HTTP Error')
    except KeyError:
        print(f'Ошибка: {response.json()['error']['error_msg']}')
    except Exception as error:
        print(f"{type(error)} {error}")


def count_clicks(short_url):
    parsed = urlparse(short_url).path.replace('/', '')
    time.sleep(1.1)
    url = "https://api.vk.ru/method/utils.getLinkStats"
    payload = {"v": "5.199", "access_token": vk_api_key, "key": parsed, "interval": "forever", "extended": "0"}
    response = requests.get(f"{url}", params=payload)
    try:
        response.raise_for_status()
        print(f'Количество кликов по ссылке: {response.json()["response"]["stats"][0]["views"]}')
    except requests.exceptions.HTTPError:
        print(f'HTTP Error')
    except Exception as error:
        print(f"{type(error)} {error}")


if __name__ == '__main__':
    user_input = input("Введите URL-адрес, который вы хотите сократить: ")
    vk_api_key = configure_keys("VK_API_KEY")
    is_shorten_link(user_input)
