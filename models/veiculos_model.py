#Model usuario
from models.conecxao import *

class Veiculos(Base):
    __tablename__ = "veiculos"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    placa = Column("placa", String(10))
    marca = Column("marca", String(200))
    modelo = Column("modelo", String(15))
    ano = Column("ano", String(100))
    chassi = Column("chassi", String(15))
    data_aquisicao = Column("data_aquisicao", String(10))
    status = Column("status", String(50))
    tipo = Column("tipo", String(20))
    quilometragem = Column("quilometragem", String(100))
     #A função __init__ serve para inicializar a classe (construtor da classe)
    def __init__(self,placa, marca, modelo, ano, chassi, data_aquisicao, status, tipo, quilometragem):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.chassi = chassi
        self.data_aquisicao = data_aquisicao
        self.status = status
        self.tipo = tipo
        self.quilometragem = quilometragem

#Criando as tabelas no banco de dados (caso não existam)
Base.metadata.create_all(bind=engine)
