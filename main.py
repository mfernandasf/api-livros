from fastapi import FastAPI, APIRouter
from app.controllers.livro_controller import router as livro_router
from app.controllers.usuario_controller import router as usuario_router
from app.views.livro_view import router as livro_view_router
from app.views.usuario_view import router as usuario_view_router
from fastapi.templating import Jinja2Templates
from pathlib import Path



app = FastAPI()

# Configurar o diretório de templates
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

#rotas - controllers
app.include_router(livro_router, prefix="/livros", tags=["Livros"])
app.include_router(usuario_router, prefix="/usuarios", tags=["Usuários"])

app.include_router(livro_view_router, tags=["VIew - Livro"])
app.include_router(usuario_view_router, tags=["View - Usuários"])

