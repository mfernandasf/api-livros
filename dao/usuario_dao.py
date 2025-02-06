import json
import os
from typing import List, Optional
from app.models.usuario_model import Usuario

USUARIOS_FILE = os.path.join(os.path.dirname(__file__), '../data/usuarios.json')

class UsuarioDAO:
    @staticmethod
    def _read_usuarios() -> List[Usuario]:
    
        try:
            with open(USUARIOS_FILE, 'r') as f:
                usuarios = json.load(f)
                return [Usuario(**usuario) for usuario in usuarios]
        except FileNotFoundError:
            return []

    @staticmethod
    def _write_usuarios(usuarios: List[Usuario]):
        
        with open(USUARIOS_FILE, 'w') as f:
            json.dump([usuario.dict() for usuario in usuarios], f, indent=4)

    @classmethod
    def _get_novo_id(cls) -> int:
        
        usuarios = cls._read_usuarios()
        return max((usuario.id for usuario in usuarios), default=0) + 1

    @classmethod
    def listar_usuarios(cls) -> List[Usuario]:
        
        return cls._read_usuarios()

    @classmethod
    def buscar_por_id(cls, usuario_id: int) -> Optional[Usuario]:
        
        usuarios = cls._read_usuarios()
        return next((usuario for usuario in usuarios if usuario.id == usuario_id), None)

    @classmethod
    def adicionar_usuario(cls, usuario: Usuario) -> Usuario:
        
        usuarios = cls._read_usuarios()
        if usuario.id is None:
            usuario.id = cls._get_novo_id()

        if any(existe_usuario.id == usuario.id for existe_usuario in usuarios):
            raise ValueError('Já existe um usuário com esse id.')
        usuarios.append(usuario)
        cls._write_usuarios(usuarios)
        return usuario

    @classmethod
    def atualizar_usuario(cls, usuario_id: int, usuario_atualizado: Usuario) -> bool:
       
        usuarios = cls._read_usuarios()
        usuario = next((u for u in usuarios if u.id == usuario_id), None)

        if not usuario:
            return False

        # Atualiza os atributos do usuário
        usuario.nome = usuario_atualizado.nome
        usuario.telefone = usuario_atualizado.telefone
        usuario.curso = usuario_atualizado.curso

        cls._write_usuarios(usuarios)
        return True

    @classmethod
    def deletar_usuario(cls, usuario_id: int) -> bool:
        
        usuarios = cls._read_usuarios()
        usuario = cls.buscar_por_id(usuario_id)
        if usuario:
            usuarios.remove(usuario)
            cls._write_usuarios(usuarios)
            return True
        return False