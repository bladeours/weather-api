from app.flask import app
from app.controller import Controller

if __name__ == "__main__":
    Controller()
    app.run(host="localhost", port=8080)
