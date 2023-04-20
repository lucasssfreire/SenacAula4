from flask import Flask

app = Flask(__name__)

@app.route("/produtos")
def produtos():
    return "<h1>pagina de produtos"


