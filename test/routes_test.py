import sys
import os
from fastapi import FastAPI
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from order_routes import order_router  
from auth_routes import auth_router 

app = FastAPI()
app.include_router(order_router)
app.include_router(auth_router)

client = TestClient(app)


def test_order_routes():
    response = client.get("/order/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Você acessou a rota de pedidos"
    }

def test_auth_routes():
    response = client.get("/auth/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Você acessou a rota padrão de autenticação",
        "autenticado": False
    }


