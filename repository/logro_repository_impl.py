from sqlalchemy.orm import Session
from typing import List
from domain.logro_interface import LogroRepository
from models.models import Logro, UsuarioLogro


class LogroRepositoryImpl(LogroRepository):
    def __init__(self, db: Session):
        self.db = db

    def obtener_logros(self) -> List[Logro]:
        return self.db.query(Logro).all()

    def crear_logro(self, logro: Logro) -> Logro:
        self.db.add(logro)
        self.db.commit()
        self.db.refresh(logro)
        return logro

    def asignar_logro_a_usuario(self, usuario_logro: UsuarioLogro) -> UsuarioLogro:
        # Verificar si ya existe
        existente = self.db.query(UsuarioLogro).filter(
            UsuarioLogro.id_usuario == usuario_logro.id_usuario,
            UsuarioLogro.id_logro == usuario_logro.id_logro
        ).first()

        if existente:
            return existente  # No insertar de nuevo, devolvemos el existente

        self.db.add(usuario_logro)
        self.db.commit()
        self.db.refresh(usuario_logro)
        return usuario_logro

    def obtener_logros_por_usuario(self, id_usuario: int) -> List[Logro]:
        return (
            self.db.query(Logro)
            .join(UsuarioLogro, Logro.id_logro == UsuarioLogro.id_logro)
            .filter(UsuarioLogro.id_usuario == id_usuario)
            .all()
        )