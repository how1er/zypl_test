## Установка и запуск
***

1. Склонировать репозиторий с Github:

````
https://github.com/how1er/zypl_test.git
````
2. Перейти в директорию проекта

3. Создать виртуальное окружение:

````
python -m venv venv
````

4. Активировать окружение:

````
source venv\scripts\activate
````

5. Установка зависимостей:

```
pip install -r requirements.txt
```


6. Запустить API с помощью uvicorn
```
uvicorn main:app --reload
```

***
# API

Документация для API доступна по адресу:

```http://127.0.0.1:8000/docs```