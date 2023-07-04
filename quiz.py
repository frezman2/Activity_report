from flask import Flask, session, render_template
import os
from random import shuffle

def index():
    session['departments'] = {
            'Отдел разработки': {
                'Главный разработчик': 'Фёдоров Руслан',
                'Младший разработчик': 'Иванова Ирина',
                'Тестировщик': 'Романов Пётр'
            },
            'Бухгалтерия': {
                'Старший бухгалтер': 'Петров Иван',
                'Бухгалтер': 'Антонова Ольга'
            }
    }
    return render_template('start1.html', q_list = session['departments'])
 


folder=os.getcwd()
# Создаём объект веб-приложения:
app = Flask(__name__, template_folder=folder, static_folder=folder)  
app.add_url_rule('/', 'index', index)   # создаёт правило для URL '/' # правило для '/index' 
# Устанавливаем ключ шифрования:
app.config['SECRET_KEY'] = 'NIGER'
if __name__ == "__main__":
    # Запускаем веб-сервер:
    app.run()