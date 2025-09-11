from typing import List, Optional
from domain.mision_interface import MisionRepository
from models.models import Mision


class MisionService:
    def __init__(self, repository: MisionRepository):
        self.repository = repository

    def obtener_misiones(self) -> List[Mision]:
        return self.repository.obtener_misiones()

    def obtener_misiones_por_nivel(self, id_nivel: int) -> List[Mision]:
        return self.repository.obtener_misiones_por_nivel(id_nivel)

    def obtener_mision_por_id(self, id_mision: int) -> Optional[Mision]:
        return self.repository.obtener_mision_por_id(id_mision)

    def crear_mision(self, mision: Mision) -> Mision:
        return self.repository.crear_mision(mision)

    def crear_misiones(self, misiones: List[Mision]) -> List[Mision]:
        return self.repository.crear_misiones(misiones)
