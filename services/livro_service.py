from app.models.livro_model import Livro
from app.dao.livro_dao import LivroDAO
from typing import List, Optional

class LivroService:
    def listar_livros(self) -> List[Livro]:
        
        return LivroDAO.get_all_livros()

    def buscar_livro_por_id(self, livro_id: int) -> Optional[Livro]:

        return LivroDAO.find_livro_by_id(livro_id)

    def adicionar_livro(self, livro: Livro) -> Livro:
        
        LivroDAO.add_livro(livro)
        return livro

    def atualizar_livro(self, livro_id: int, livro: Livro) -> bool:
        
        return LivroDAO.update_livro(livro_id, livro)

    def deletar_livro(self, livro_id: int) -> bool:
        
        return LivroDAO.delete_livro(livro_id)
    
