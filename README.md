## Консольная утилита сокращающая ссылки и считающая переходы по ним.

Если пользователь указал короткую ссылку, выводит статистку кликов по ней, а если нет, сокращает ссылку.
Скрипт показывает переходы за все дни.

## Установка

1. Клонируйте репозиторий с github
2. Установите зависимости 
```bash
pip install -r requirements.txt
```
3. Укажите сервисный токен приложения API VK в переменную:
```bash
vk_api_token
```
### Если его нет:
- Социальная сеть ВК — [зарегистрируйтесь](https://vk.com/)
- Получите [Сервисный токен приложения](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/tokens/service-token)
- [Создание приложения](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/create-application)

- Тип приложения - Web
- Базовый домен - example.com
- Доверенный Redirect URL - https://example.com
---
4. Запустите скрипт 'counts_transitions_in_shortened_links.py'
```bash
python counts_transitions_in_shortened_links.py
```

## Создано с помощью 

![Static Badge](https://img.shields.io/badge/Python-3.12-blue?style=flat-square)

## Пример работы скрипта

![img.png](https://i.imgur.com/xvPR9J4.png)
![img.png](https://i.imgur.com/dcaBK9u.png)


## Цель проекта

Код написан в учебных целях - для урока в курсе Python и API веб-сервисов на сайте [Devman](https://dvmn.org/) 