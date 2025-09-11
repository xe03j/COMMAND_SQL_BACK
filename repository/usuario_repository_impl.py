from sqlalchemy.orm import Session
from typing import List, Optional
from domain.usuario_interface import UsuarioRepository
from models.models import Usuario


class UsuarioRepositoryImpl(UsuarioRepository):
    def __init__(self, db: Session):
        self.db = db

    def obtener_usuarios(self) -> List[Usuario]:
        return self.db.query(Usuario).all()

    def obtener_usuario_por_id(self, id_usuario: int) -> Optional[Usuario]:
        return self.db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()

    def obtener_usuario_por_email(self, email: str) -> Optional[Usuario]:
        return self.db.query(Usuario).filter(Usuario.email == email).first()

    def crear_usuario(self, usuario: Usuario) -> Usuario:
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def actualizar_xp(self, id_usuario: int, xp_total: int) -> Optional[Usuario]:
        usuario = self.db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        if usuario:
            usuario.xp_total = xp_total
            self.db.commit()
            self.db.refresh(usuario)
        return usuario