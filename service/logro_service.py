from typing import List
from domain.logro_interface import LogroRepository
from models.models import Logro, UsuarioLogro


class LogroService:
    def __init__(self, repository: LogroRepository):
        self.repository = repository

    def obtener_logros(self) -> List[Logro]:
        return self.repository.obtener_logros()

    def crear_logro(self, logro: Logro) -> Logro:
        return self.repository.crear_logro(logro)

    def asignar_logro_a_usuario(self, usuario_logro: UsuarioLogro) -> UsuarioLogro:
        return self.repository.asignar_logro_a_usuario(usuario_logro)

    def obtener_logros_por_usuario(self, id_usuario: int) -> List[Logro]:
        return self.repository.obtener_logros_por_usuario(id_usuario)
