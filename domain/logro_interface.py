from abc import ABC, abstractmethod
from typing import List
from models.models import Logro, UsuarioLogro


class LogroRepository(ABC):
    @abstractmethod
    def obtener_logros(self) -> List[Logro]:
        pass

    @abstractmethod
    def crear_logro(self, logro: Logro) -> Logro:
        pass

    @abstractmethod
    def asignar_logro_a_usuario(self, usuario_logro: UsuarioLogro) -> UsuarioLogro:
        pass

    @abstractmethod
    def obtener_logros_por_usuario(self, id_usuario: int) -> List[Logro]:
        """Obtiene todos los logros asociados a un usuario"""
        pass