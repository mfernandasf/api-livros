from app.services.livro_service import LivroService
from app.dao.livro_dao import LivroDAO
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Criar o router para views
router = APIRouter()

service = LivroService()
# Configurar templates (usando a configuração do main.py)
templates = Jinja2Templates(directory="app/templates/")

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    # Obter a lista de livros do serviço
    livros = service.listar_livros()
    
    # Renderizar o template index.html com os dados
    return templates.TemplateResponse("index.html", {"request": request, "livros": livros})

@router.get("/listar_livros", response_class=HTMLResponse)
def index(request: Request):
    # Obter a lista de livros do serviço
    livros = service.listar_livros()
    
    # Renderizar o template index.html com os dados
    return templates.TemplateResponse("livros/listar_livro.html", {"request": request, "livros": livros})

@router.get("/adicionar_livro", response_class=HTMLResponse)
def adicionar_livro(request: Request):
    return templates.TemplateResponse("livros/adicionar_livro.html", {"request": request})

@router.get("/editar_livro", response_class=HTMLResponse)
def editar_livro(request: Request, livro_id: int):
    livro = LivroService.adicionar_livro(livro_id)
    return templates.TemplateResponse("livros/editar_livro.html", {"request": request, "livro": livro})