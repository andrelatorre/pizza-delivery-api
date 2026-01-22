from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType

#cria a coneção do banco
db = create_engine("sqlite:///database/banco.db")

#cria a base do banco
Base = declarative_base()

#cria as classes/tabela
#Usuario
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome =  Column("nome", String, nullable=False) 
    email =  Column("email", String, nullable=False)
    senha = Column("email", String)
    ativo = Column("ativo", Boolean, default=True)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

#Pedido
class Pedido(Base):
    __tablename__ = "pedidos"

    STATUS_PEDIDO = (
        ("PENDENTE", "PENDENTE"),
        ("CANCELADO", "CANCELADO"),
        ("FINALIZADO", "FINALIZADO")
    )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", ChoiceType(choices=STATUS_PEDIDO))  #pendente, cancelado e finalizado
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    #cd_itens_pedido = 

    def __init__(self, usuario, status='PENDENTE', preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco
    
#Itens Pedido

#executa a criação dos metadados (cria efetivamente o banco)