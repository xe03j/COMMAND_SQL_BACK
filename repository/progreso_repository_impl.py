from sqlalchemy.orm import Session
from typing import List, Optional
from domain.progreso_interface import ProgresoRepository
from models.models import Progreso


class ProgresoRepositoryImpl(ProgresoRepository):
    def __init__(self, db: Session):
        self.db = db

    def obtener_progreso_por_usuario(self, id_usuario: int) -> List[Progreso]:
        return self.db.query(Progreso).filter(Progreso.id_usuario == id_usuario).all()

    def obtener_progreso_mision(self, id_usuario: int, id_mision: int) -> Optional[Progreso]:
        return (self.db.query(Progreso)
                .filter(Progreso.id_usuario == id_usuario, Progreso.id_mision == id_mision)
                .first())

    def registrar_progreso(self, progreso: Progreso) -> Progreso:
        self.db.add(progreso)
        self.db.commit()
        self.db.refresh(progreso)
        return progreso

