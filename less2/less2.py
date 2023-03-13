# pip freeze > requiremennts.txt
# python -m venv venv создание виртуального окружения для проекта
# надо свежий питон от 3.11.1
# надо установить pip install flask-wtf для создания формы и отслеживания что воодит пользователь
from flask import Flask, render_template
#from LoginForm import Lf

app = Flask(__name__)
app.config['SECRET_KEY']='hello hello hello world'#вводится секретный код


@app.route('/')
def main():
    return render_template('list2.html')


if __name__ == '__main__':
    app.run()