# importando os módulos da biblioteca flask
from flask import Flask, render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():
    nome = "Seu Nome"  # Insira seu nome aqui
    idade = "Sua Idade"  # Insira sua idade aqui

    return render_template('index.html', nome=nome, idade=idade)

# rota para a página do pai
@app.route("/pai")
def pai():
    return render_template('pai.html')

# rota para a página da mãe
@app.route("/mae")
def mae():
    return render_template('mae.html')

# rota para a página do amigo
@app.route("/amigo")
def amigo():
    return render_template('amigo.html')

# execute o arquivo
if __name__ == '__main__':
    app.run(debug=True)
