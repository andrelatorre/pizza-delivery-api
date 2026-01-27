from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from database.schemas import PedidoSchema
from models.models import Pedido

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def orders():
    """
    Essa é a rota padrão de pedidos do sistema. Todas as rotas dos pedidos precisam de autenticação.
    """
    return {"message": "Você acessou a rota de pedidos"}

@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario = pedido_schema.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return {":message": f"Pedido criado com sucesso. Pedido número: {novo_pedido.id}"}