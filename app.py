import sqlite3  # Импортируем модуль для работы с SQLite
from flask import Flask, render_template  # Импортируем модуль для создания и развертывания Flask-приложения

app = Flask(__name__)

# Функция для подключения к базе данных и получения данных
def get_data():
    conn = sqlite3.connect('database.db')  # Создаем соединение с базой данных
    c = conn.cursor()  # Создаем курсор для выполнения запросов к базе данных
    c.execute("PRAGMA table_info(stud_group)")
    columns = [column[1] for column in c.fetchall()]  # Получаем имена столбцов
    c.execute("SELECT * FROM stud_group")
    data = c.fetchall()  # Получаем все строки данных из таблицы
    conn.close()  # Закрываем соединение
    return columns, data

# Маршрут для отображения данных на веб-странице
@app.route('/')
def index():
    columns, data = get_data()
    return render_template('index.html', columns=columns, data=data)

if __name__ == '__main__':
    app.run(debug=True)  # Запускаем Flask-приложение в режиме отладки