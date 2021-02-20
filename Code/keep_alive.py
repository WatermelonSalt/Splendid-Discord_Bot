import os

from flask import Flask

from threading import Thread

from dotenv import load_dotenv

load_dotenv()

NAME = os.getenv('BOT_NAME')
app = Flask('')


@app.route('/')
def main():
    return f"{NAME} is alive!"


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    server = Thread(target=run)
    server.start()
