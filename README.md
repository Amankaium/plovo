# Спецификация plovo
Для получения списка блюд необходимо отправить ```GET``` запрос на ```/dish/```:
```json
[
    {
    "id": 7,
    "name": "Fish with lemon",
    "price": 200
    },
    {
        "id": 5,
        "name": "Балбан самсасы",
        "price": 155
    },
]
```

Методы ```POST, PUT, UPDATE, DELETE``` на ```/dish/``` вернут ошибку ```405```