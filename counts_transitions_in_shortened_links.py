import requests
import os
import time
from dotenv import load_dotenv
from urllib.parse import urlparse


def configure_keys(token):
    load_dotenv()
    key = os.getenv(token)
    return key


def input_check():
    while True:
        user_input_check = input("Введите URL-адрес: ")
        parsed = urlparse(user_input_check)
        if parsed.scheme != '':
            if parsed.netloc != '':
                break
            else:
                print("Введите полный URL как на примере: https://ya.ru")
        else:
            print("Введите полный URL как на примере: https://ya.ru")
    return user_input_check


def is_shorten_link(url):
    if urlparse(url).netloc == "vk.cc":
        return True
    else:
        return False


def shorten_link(link):
    url = "https://api.vk.ru/method/utils.getShortLink"
    payload = {"v": "5.199", "access_token": vk_api_key, "url": {link}}
    response = requests.get(f"{url}", params=payload)
    try:
        response.raise_for_status()
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
        return response.json()["response"]["stats"][0]["views"]
    except requests.exceptions.HTTPError:
        print(f'HTTPError')
    except Exception as error:
        print(f"{type(error)} {error}")


if __name__ == '__main__':
    vk_api_key = configure_keys("VK_API_KEY")
    user_input = input_check()
    if is_shorten_link(user_input) is True:
        print(f'Количество кликов по ссылке: {count_clicks(user_input)}')
    elif is_shorten_link(user_input) is False:
        print(f'Сокращенная ссылка: {shorten_link(user_input)}')
