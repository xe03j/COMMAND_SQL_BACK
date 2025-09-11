from abc import ABC, abstractmethod
from typing import List, Optional
from models.models import Progreso


class ProgresoRepository(ABC):
    @abstractmethod
    def obtener_progreso_por_usuario(self, id_usuario: int) -> List[Progreso]:
        pass

    @abstractmethod
    def obtener_progreso_mision(self, id_usuario: int, id_mision: int) -> Optional[Progreso]:
        pass

    @abstractmethod
    def registrar_progreso(self, progreso: Progreso) -> Progreso:
        pass
