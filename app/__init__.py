from flask import Flask

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Секретный ключ для сессий и защиты формы CSRF

from app import routes  # Импортируем маршруты
