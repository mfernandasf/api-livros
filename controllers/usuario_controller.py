from fastapi import APIRouter, HTTPException
from app.models.usuario_model import Usuario
from app.services.usuario_service import UsuarioService


router = APIRouter()

usuario_service = UsuarioService()

@router.get("/", response_model=list[Usuario])
def listar_usuarios():
    return usuario_service.listar_usuarios()

@router.get("/{usuario_id}", response_model=Usuario)
def buscar_usuario(usuario_id: int):
    usuario = usuario_service.buscar_usuario_por_id(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router.post("/", response_model=Usuario)
def adicionar_usuario(usuario: Usuario):
    return usuario_service.adicionar_usuario(usuario)

@router.put("/{usuario_id}", response_model=Usuario)
def atualizar_usuario(usuario_id: int, usuario: Usuario):
    usuario_atualizado = usuario_service.atualizar_usuario(usuario_id, usuario)
    if not usuario_atualizado:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario_atualizado

@router.delete("/{usuario_id}", status_code=204)
def deletar_usuario(usuario_id: int):
    if not usuario_service.deletar_usuario(usuario_id):
        raise HTTPException(status_code=404, detail="Usuário não encontrado")