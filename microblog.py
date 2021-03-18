from flask import Flask
app = Flask ("microblog")

# operador do python que faz algo com a funcao logo abaixo
@app.route("/")
def index():
    return "Olá Mundo!"

app.run()
