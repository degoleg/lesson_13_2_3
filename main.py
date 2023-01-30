import os
import dotenv
from flask import Flask

app = Flask(__name__)

# загружаем в переменные окружения данные из файла .env
dotenv.load_dotenv(override=True)

if os.environ.get("APP_CONFIG") == "development":
    app.config.from_pyfile('config/development.py')
    title = app.config.get("TITLE")
    description = app.config.get("DESCRIPTION")
else:
    app.config.from_pyfile('config/production.py')
    title = app.config.get("TITLE")
    description = app.config.get("DESCRIPTION")

@app.route('/')
def page_index():
    return f"<p>{ title } - { description }<p>"


app.run()