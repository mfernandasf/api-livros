from pydantic import BaseModel
from typing import Optional

class Livro(BaseModel):
    id: Optional[int] = None  # ID será opcional, pois será gerado automaticamente
    titulo: str
    autor: str
    genero: Optional[str] = None
    quantidade: int  # Quantidade de exemplares
