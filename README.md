# Спецификация plovo

## Список блюд
### Для получения списка блюд необходимо отправить ```GET``` запрос на ```/dish/```:
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

### Методы ```POST, PUT, UPDATE, DELETE``` на ```/dish/``` вернут ошибку ```405```

## Регистрация
### Для прохождения регистрации необходимо отправить ```POST``` запрос на ```/users/registration/``` со следующими данными:
```json 
{
    "username": "ulugbek",
    "email": "ulugbek@gmail.com",
    "password_1": "test123",
    "password_2": "test123",
    "first_name": "Ulugbek",
    "last_name": "Kadyrbekov",
}
```

### Вам вернётся ответ со статусом ```201```:
```json
{
    "username": "ulugbek",
    "first_name": "Ulugbek",
    "email": "ulugbek@gmail.com"
}
```

### Методы ```GET, PUT, UPDATE, DELETE``` на ```/users/registration/``` вернут ошибку ```405```

### Если поля будут пустыми или невалидными, то будет ответ ```400```, например:
```json
{
    "username": [
        "This field is required."
    ]
}
```

### При несовпадении паролей будет ответ ```406``` с сообщением:
```json
{
    "error": "Пароли не совпадают"
}
```