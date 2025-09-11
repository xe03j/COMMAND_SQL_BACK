from typing import List, Optional
from domain.usuario_interface import UsuarioRepository
from models.models import Usuario


class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def obtener_usuarios(self) -> List[Usuario]:
        return self.repository.obtener_usuarios()

    def obtener_usuario_por_id(self, id_usuario: int) -> Optional[Usuario]:
        return self.repository.obtener_usuario_por_id(id_usuario)

    def obtener_usuario_por_email(self, email: str) -> Optional[Usuario]:
        return self.repository.obtener_usuario_por_email(email)

    def crear_usuario(self, usuario: Usuario) -> Usuario:
        return self.repository.crear_usuario(usuario)

    def actualizar_xp(self, id_usuario: int, xp_total: int) -> Optional[Usuario]:
        return self.repository.actualizar_xp(id_usuario, xp_total)
