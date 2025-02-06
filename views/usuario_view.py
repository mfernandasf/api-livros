from app.services.usuario_service import UsuarioService
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Criar o router para views
router = APIRouter()

service = UsuarioService()
# Configurar templates (usando a configuração do main.py)
templates = Jinja2Templates(directory="app/templates/")

@router.get("/listar_usuarios", response_class=HTMLResponse)
def index(request: Request):
    usuarios = service.listar_usuarios()
    # Renderizar o template index.html com os dados
    return templates.TemplateResponse("usuarios/listar_usuario.html", {"request": request,"usuarios":usuarios})

@router.get("/adicionar_usuario", response_class=HTMLResponse)
def index(request: Request):
    # Renderizar o template index.html com os dados
    return templates.TemplateResponse("usuarios/adicionar_usuario.html", {"request": request})


@router.get("/editar_usuario", response_class=HTMLResponse)
def editar_usuario(request: Request, usuario_id: int):
    usuario = UsuarioService.buscar_usuario_por_id(usuario_id)

    return templates.TemplateResponse("usuarios/editar_usuario.html", {"request": request, "usuario": usuario})