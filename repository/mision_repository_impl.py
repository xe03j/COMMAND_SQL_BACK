from sqlalchemy.orm import Session
from typing import List, Optional
from domain.mision_interface import MisionRepository
from models.models import Mision


class MisionRepositoryImpl(MisionRepository):
    def __init__(self, db: Session):
        self.db = db

    def obtener_misiones(self) -> List[Mision]:
        return self.db.query(Mision).all()

    def obtener_misiones_por_nivel(self, id_nivel: int) -> List[Mision]:
        return self.db.query(Mision).filter(Mision.id_nivel == id_nivel).all()

    def obtener_mision_por_id(self, id_mision: int) -> Optional[Mision]:
        return self.db.query(Mision).filter(Mision.id_mision == id_mision).first()

    def crear_mision(self, mision: Mision) -> Mision:
        self.db.add(mision)
        self.db.commit()
        self.db.refresh(mision)
        return mision

    def crear_misiones(self, misiones: List[Mision]) -> List[Mision]:
        self.db.add_all(misiones)  # insert masivo
        self.db.commit()
        for m in misiones:
            self.db.refresh(m)
        return misiones