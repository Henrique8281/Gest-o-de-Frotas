from flask import flask, render_templates

app = flask(__name__)

@app.route('/login')
def tela_login():
    return render_templates('login.html')

@app.route('/homepage')
def tela_inicial():
    return render_templates('homepage.html')

if __name__ == '__main__':
    app.run()