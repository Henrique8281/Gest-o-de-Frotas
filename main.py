from flask import Flask, render_template

app = Flask(__name__)
from controllers.usuario_controller import *
if __name__ == "__main__":
    app.run()

@app.route('/login')
def tela_um():
    return render_template('/usuario/login.html')

@app.route("/create")
def inserir():
    return render_template("/usuario/create.html")

@app.route('/homepage')
def tela_dois():
    return render_template('/usuario/homepage.html')

@app.route('/lista_veiculos')
def tela_4():
    return render_template('/veiculos/lista_veiculos.html')

@app.route('/registroveiculos')
def tela_5():
    return render_template('/veiculos/registro_veiculos.html')

@app.route('/manutencao')
def tela_6():
    return render_template('/veiculos/registro_manutencao.html')

@app.route('/buscarveiculos')
def tela_7():
    return render_template('/manutencao/buscar_veículos.html')

@app.route('/listarmanutencao')
def tela_8():
    return render_template('/manutencao/listar_manutenções.html')

if __name__ =='__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

