from abc import ABC, abstractmethod
from typing import List, Optional
from models.models import Mision


class MisionRepository(ABC):
    @abstractmethod
    def obtener_misiones(self) -> List[Mision]:
        pass

    @abstractmethod
    def obtener_misiones_por_nivel(self, id_nivel: int) -> List[Mision]:
        pass

    @abstractmethod
    def obtener_mision_por_id(self, id_mision: int) -> Optional[Mision]:
        pass

    @abstractmethod
    def crear_mision(self, mision: Mision) -> Mision:
        pass

    @abstractmethod
    def crear_misiones(self, misiones: List[Mision]) -> List[Mision]:
        pass
