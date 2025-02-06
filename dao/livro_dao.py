import json
import os
from typing import List, Optional
from app.models.livro_model import Livro

LIVROS_FILE = os.path.join(os.path.dirname(__file__), '../data/livros.json')

class LivroDAO:
    @staticmethod
    def _read_livros() -> List[Livro]:
        try:
            with open(LIVROS_FILE, 'r') as f:
                livros = json.load(f)
                return [Livro(**livro) for livro in livros]
        except FileNotFoundError:
            return []

    @staticmethod
    def _write_livros(livros: List[Livro]):
        with open(LIVROS_FILE, 'w') as f:
            json.dump([livro.dict() for livro in livros], f, indent=4)

    @classmethod
    def _get_novo_id(cls) -> int:
        livros = cls._read_livros()
        return max((livro.id for livro in livros), default=0) + 1

    @classmethod
    def add_livro(cls, livro: Livro):
        livros = cls._read_livros()
        if livro.id is None:
            livro.id = cls._get_novo_id()

        if any(existe_livro.id == livro.id for existe_livro in livros):
            raise ValueError('Já existe um livro com esse id.')
        livros.append(livro)
        cls._write_livros(livros)

    @classmethod
    def get_all_livros(cls) -> List[Livro]:
       
        return cls._read_livros()

    @classmethod
    def find_livro_by_id(cls, livro_id: int) -> Optional[Livro]:
      
        livros = cls._read_livros()
        return next((livro for livro in livros if livro.id == livro_id), None)

    @classmethod
    def delete_livro(cls, livro_id: int) -> bool:
      
        livros = cls._read_livros()
        livro = cls.find_livro_by_id(livro_id)
        if livro:
            livros.remove(livro)
            cls._write_livros(livros)
            return True
        return False

    @classmethod
    def update_livro(cls, livro_id: int, livro_atualizado: Livro) -> bool:

        livros = cls._read_livros()
        livro = next((l for l in livros if l.id == livro_id), None)

        if not livro:
            return False

        # Atualiza os atributos do livro
        livro.titulo = livro_atualizado.titulo
        livro.autor = livro_atualizado.autor
        livro.genero = livro_atualizado.genero
        livro.quantidade = livro_atualizado.quantidade

        cls._write_livros(livros)
        return True