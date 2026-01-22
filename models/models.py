#para criar o banco via alembic
# alembic revision --autogenerate -m "Initial Migration"
# e para executar a versao
# alembic upgrade head

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
    senha = Column("senha", String)
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

    #STATUS_PEDIDO = (
    #    ("PENDENTE", "PENDENTE"),
    #    ("CANCELADO", "CANCELADO"),
    #    ("FINALIZADO", "FINALIZADO")
    #)

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String)  #pendente, cancelado e finalizado
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    #itens_pedido = Column("itens_pedido", ForeignKey("itens_pedido.id"))

    def __init__(self, usuario, status='PENDENTE', preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco
    
#Itens Pedido
class ItensPedido(Base):
    __tablename__ ="itens_pedido"
    

    #TAMANHO = (
    #    ("GRANDE", "GRANDE"),
    #    ("PEQUENA", "PEQUENA"),
    #    ("MEDIA", "MEDIA")
    #)

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.tamanho = tamanho
        self.sabor = sabor
        self.preco_unitario = preco_unitario
        self.pedido = pedido

#executa a criação dos metadados (cria efetivamente o banco)