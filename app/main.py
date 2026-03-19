from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="dio-atm-api",
    description="API para gerência de entidades e operações do sistema dio-atm-backend",
    version="1.0.0"
)

@app.get("/", summary="Default", tags=["Default"], description="Verifica se a API está rodando.")
def read_root():
    return {"message": "API running"}