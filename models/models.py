from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

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
#Itens Pedido

#executa a criação dos metadados (cria efetivamente o banco)