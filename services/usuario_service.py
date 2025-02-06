from app.models.usuario_model import Usuario
from app.dao.usuario_dao import UsuarioDAO
from typing import List, Optional

class UsuarioService:
    def listar_usuarios(self) -> List[Usuario]:
        
        return UsuarioDAO.listar_usuarios()

    def buscar_usuario_por_id(self, usuario_id: int) -> Optional[Usuario]:
        
        return UsuarioDAO.buscar_por_id(usuario_id)

    def adicionar_usuario(self, usuario: Usuario) -> Usuario:
        
        return UsuarioDAO.adicionar_usuario(usuario)

    def atualizar_usuario(self, usuario_id: int, usuario: Usuario) -> bool:
        
        return UsuarioDAO.atualizar_usuario(usuario_id, usuario)

    def deletar_usuario(self, usuario_id: int) -> bool:
        
        return UsuarioDAO.deletar_usuario(usuario_id)