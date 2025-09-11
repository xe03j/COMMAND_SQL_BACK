from typing import List, Optional
from domain.progreso_interface import ProgresoRepository
from models.models import Progreso


class ProgresoService:
    def __init__(self, repository: ProgresoRepository):
        self.repository = repository

    def obtener_progreso_por_usuario(self, id_usuario: int) -> List[Progreso]:
        return self.repository.obtener_progreso_por_usuario(id_usuario)

    def obtener_progreso_mision(self, id_usuario: int, id_mision: int) -> Optional[Progreso]:
        return self.repository.obtener_progreso_mision(id_usuario, id_mision)

    def registrar_progreso(self, progreso: Progreso) -> Progreso:
        return self.repository.registrar_progreso(progreso)
