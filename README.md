## Консольная утилита сокращающая ссылки и считающая переходы по ним.

Если пользователь указал короткую ссылку, выводит статистку кликов по ней, а если нет, сокращает ссылку.
Скрипт показывает переходы за все дни.

## Установка

1. Клонируйте репозиторий с github
2. Установите зависимости 
```bash
pip install -r requirements.txt
```
3. Пропишите в файл `.env` имя и значение этой переменной как на примере ниже, замените `0123456789abcdefgh` на свой сервисный ключ – “токен” API VK.
```bash
VK_API_KEY=0123456789abcdefgh
```
### Как его получить:
- Социальная сеть ВК — [зарегистрируйтесь](https://vk.com/)
- Получите [Сервисный токен приложения](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/tokens/service-token)
- [Создание приложения](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/create-application)

- Тип приложения - Web
- Базовый домен - example.com
- Доверенный Redirect URL - https://example.com
---
4. Запустите скрипт 'link_shortener.py'
```bash
python link_shortener.py.py
```

## Создано с помощью 

![Static Badge](https://img.shields.io/badge/Python-3.12-blue?style=flat-square)

## Пример работы скрипта

![img.png](https://i.imgur.com/xvPR9J4.png)
![img.png](https://i.imgur.com/dcaBK9u.png)


## Цель проекта

Код написан в учебных целях - для урока в курсе Python и API веб-сервисов на сайте [Devman](https://dvmn.org/) 