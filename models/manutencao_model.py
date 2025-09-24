#Model usuario
from models.conecxao import *

class Manutencao(Base):
    __tablename__ = "manutencao"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    placa = Column("placa", String(10))
    data_manutencao = Column("data_manutencao", String(200))
    odometro = Column("odometro", String(20))
    tipo_manutencao = Column("tipo_manutencao", String(100))
    descricao_servico = Column("descricao_servico", String(200))
     #A função __init__ serve para inicializar a classe (construtor da classe)
    def __init__(self,nome, login, senha, email, telefone):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.email = email
        self.telefone = telefone

#Criando as tabelas no banco de dados (caso não existam)
Base.metadata.create_all(bind=engine)
