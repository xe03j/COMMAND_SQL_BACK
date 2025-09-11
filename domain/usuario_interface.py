from abc import ABC, abstractmethod
from typing import List, Optional
from models.models import Usuario


class UsuarioRepository(ABC):
    @abstractmethod
    def obtener_usuarios(self) -> List[Usuario]:
        pass

    @abstractmethod
    def obtener_usuario_por_id(self, id_usuario: int) -> Optional[Usuario]:
        pass

    @abstractmethod
    def obtener_usuario_por_email(self, email: str) -> Optional[Usuario]:
        pass

    @abstractmethod
    def crear_usuario(self, usuario: Usuario) -> Usuario:
        pass

    @abstractmethod
    def actualizar_xp(self, id_usuario: int, xp_total: int) -> Optional[Usuario]:
        pass