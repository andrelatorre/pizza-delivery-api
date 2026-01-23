from fastapi import APIRouter, Depends
from models.models import Usuario, db
from dependencies import pegar_sessao
#from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autenticação do nosso sistema.
    """
    return {"message": "Você acessou a rota padrão de autenticação", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session=Depends(pegar_sessao)):

    usuario =  session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        #ja existe um user com esse email
        return {"message": "Já existe um usuário com esse email"}, 400
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"message": "Usuário cadastrado com sucesso"}
