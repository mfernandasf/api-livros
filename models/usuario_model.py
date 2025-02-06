from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id: Optional[int] = None  # ID será opcional, pois será gerado automaticamente
    nome: str
    telefone: str 
    curso: str