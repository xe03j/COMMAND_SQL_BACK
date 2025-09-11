from abc import ABC, abstractmethod
from typing import List, Optional
from models.models import Nivel


class NivelRepository(ABC):
    @abstractmethod
    def obtener_niveles(self) -> List[Nivel]:
        pass

    @abstractmethod
    def obtener_nivel_por_id(self, id_nivel: int) -> Optional[Nivel]:
        pass

    @abstractmethod
    def crear_nivel(self, nivel: Nivel) -> Nivel:
        pass

    @abstractmethod
    def crear_niveles(self, niveles: List[Nivel]) -> List[Nivel]:
        pass
