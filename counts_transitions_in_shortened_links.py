import requests
import os
from dotenv import load_dotenv


def configure_keys(token):
    load_dotenv()
    key = os.getenv(token)
    return key


def shorten_link(link):
    url = "https://api.vk.ru/method/utils.getShortLink"
    payload = {"v": "5.199", "access_token": vk_api_key, "url": {link}}
    response = requests.get(f"{url}", params=payload)
    response.raise_for_status()
    response = response.json()
    answer = response['response']["short_url"]
    return answer


if __name__ == '__main__':
    link = input("Enter the url you want to shorten: ")
    vk_api_key = configure_keys("VK_API_KEY")
    print('Сокращенная ссылка: ', shorten_link(link))
