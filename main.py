from flask import flask, render_templates

app = flask(__name__)

@app.route('/login')
def tela_usuario():
    return render_templates('login.html')

@app.route('/homepage')
def tela_usuario():
    return render_templates('homepage.html')

@app.route('/lista_veiculos')
def tela_veiculos():
    return render_templates('lista_veiculos.html')

@app.route('/registroveiculos')
def tela_veiculos():
    return render_templates('registro_veiculos.html')

@app.route('/manutencao')
def tela_veiculos():
    return render_templates('registro_manutencao.html')

@app.route('/homepage')
def tela_manutencao():
    return render_templates('homepage.html')

if __name__ == '__main__':
    app.run()