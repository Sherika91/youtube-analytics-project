# Access Modes. Homework

## Task Description

Modify the constructor of `Channel` so that after initialization, the instance has the following attributes filled with
real
channel data:

- Channel ID
- Channel name
- Channel description
- Channel link
- Number of subscribers
- Number of videos
- Total number of views

Add the following methods to the `Channel` class:

- Class method `get_service()`, returning an object for working with the YouTube API
- Method `to_json()`, saving the attribute values of the `Channel` instance to a file

## Expected Behavior

- The code in the `main.py` file should produce the expected output

# Режимы доступа. Домашнее задание

## Описание задачи

Модифицируйте конструктор `Channel`, чтобы после инициализации экземпляр имел следующие атрибуты, заполненные реальными
данными канала:

- id канала
- название канала
- описание канала
- ссылка на канал
- количество подписчиков
- количество видео
- общее количество просмотров

Добавьте в класс `Channel` следующие методы:

- класс-метод `get_service()`, возвращающий объект для работы с YouTube API
- метод `to_json()`, сохраняющий в файл значения атрибутов экземпляра `Channel`

## Ожидаемое поведение

- Код в файле `main.py` должен выдавать ожидаемые значения