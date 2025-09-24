from main import app
from flask import request, render_template, redirect, url_for
from models.veiculos_model import *
# Criando  sessão para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#rotas
@app.route("/registroveiculos")
def criarveiculos():
    return render_template("veiculos/registro_veiculos.html")

@app.route("/veiculos", methods=["POST"])
def create_veiculo():
    
    if request.method == 'POST':
        #Captura os dados enviados pelo formulário
        placa = request.form['placa']
        marca = request.form['marca']
        modelo = request.form['modelo']
        ano = request.form['ano']
        chassi = request.form['chassi']
        data_aquisicao = request.form['data_aquisicao']
        status = request.form['status']
        tipo = request.form['tipo']
        quilometragem = request.form['quilometragem']
        #Cria um novo usuário
        new_entidade = Veiculos(placa=placa,marca=marca, modelo=modelo, ano=ano, chassi=chassi, data_aquisicao=data_aquisicao, status=status, tipo=tipo, quilometragem=quilometragem)
        #Cria um novo usuário no banco de dados
        db = SessionLocal()
        #Adiciona o novo usuário ao banco de dados
        db.add(new_entidade)
        db.commit()
    return redirect(url_for('lista'))
    
    
@app.route("/list")
def lista_veiculo():
    return "Aqui a lista de usuários cadastrados."