from typing import List, Optional
from domain.nivel_interface import NivelRepository
from models.models import Nivel


class NivelService:
    def __init__(self, repository: NivelRepository):
        self.repository = repository

    def obtener_niveles(self) -> List[Nivel]:
        return self.repository.obtener_niveles()

    def obtener_nivel_por_id(self, id_nivel: int) -> Optional[Nivel]:
        return self.repository.obtener_nivel_por_id(id_nivel)

    def crear_nivel(self, nivel: Nivel) -> Nivel:
        return self.repository.crear_nivel(nivel)

    def crear_niveles(self, niveles: List[Nivel]) -> List[Nivel]:
        return self.repository.crear_niveles(niveles)
