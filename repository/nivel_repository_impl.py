from sqlalchemy.orm import Session
from typing import List, Optional
from domain.nivel_interface import NivelRepository
from models.models import Nivel


class NivelRepositoryImpl(NivelRepository):
    def __init__(self, db: Session):
        self.db = db

    def obtener_niveles(self) -> List[Nivel]:
        return self.db.query(Nivel).all()

    def obtener_nivel_por_id(self, id_nivel: int) -> Optional[Nivel]:
        return self.db.query(Nivel).filter(Nivel.id_nivel == id_nivel).first()

    def crear_nivel(self, nivel: Nivel) -> Nivel:
        self.db.add(nivel)
        self.db.commit()
        self.db.refresh(nivel)
        return nivel

    def crear_niveles(self, niveles: List[Nivel]) -> List[Nivel]:
        self.db.add_all(niveles)  # 👈 importante: add_all para insertar en batch
        self.db.commit()
        for nivel in niveles:
            self.db.refresh(nivel)
        return niveles
