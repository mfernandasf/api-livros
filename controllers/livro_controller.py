from fastapi import APIRouter, HTTPException
from app.models.livro_model import Livro
from app.services.livro_service import LivroService


service = LivroService()
router = APIRouter()

@router.get("/", response_model=list[Livro])
def listar_livros():
    return service.listar_livros()

@router.get("/{livro_id}", response_model=Livro)
def buscar_livro(livro_id: int):
    livro = service.buscar_livro_por_id(livro_id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro

@router.post("/", response_model=Livro)
def adicionar_livro(livro: Livro):
    return service.adicionar_livro(livro)

@router.put("/{livro_id}", response_model=Livro)
def atualizar_livro(livro_id: int, livro: Livro):
    livro_atualizado = service.atualizar_livro(livro_id, livro)
    if not livro_atualizado:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro_atualizado

@router.delete("/{livro_id}", status_code=204)
def deletar_livro(livro_id: int):
    if not service.deletar_livro(livro_id):
        raise HTTPException(status_code=404, detail="Livro não encontrado")