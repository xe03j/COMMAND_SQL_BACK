from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.database import Base


class Nivel(Base):
    __tablename__ = "niveles"

    id_nivel = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descripcion = Column(Text)
    dificultad = Column(String(50))
    tema_sql = Column(String(100))

    misiones = relationship("Mision", back_populates="nivel", cascade="all, delete-orphan")


class Mision(Base):
    __tablename__ = "misiones"

    id_mision = Column(Integer, primary_key=True, index=True)
    id_nivel = Column(Integer, ForeignKey("niveles.id_nivel"), nullable=False)
    enunciado = Column(Text, nullable=False)
    consulta_correcta = Column(Text)
    tabla_base = Column(String(100))

    nivel = relationship("Nivel", back_populates="misiones")
    progresos = relationship("Progreso", back_populates="mision", cascade="all, delete-orphan")


class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    # atributo Python sin ñ, pero la columna SQL se llamará "contraseña_hash"
    contrasena_hash = Column("contraseña_hash", String(255), nullable=False)
    xp_total = Column(Integer, default=0)
    nivel_actual = Column(Integer, nullable=True)
    fecha_registro = Column(TIMESTAMP, server_default=func.now())

    progresos = relationship("Progreso", back_populates="usuario", cascade="all, delete-orphan")
    usuarios_logros = relationship("UsuarioLogro", back_populates="usuario", cascade="all, delete-orphan")


class Progreso(Base):
    __tablename__ = "progreso"

    id_progreso = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_mision = Column(Integer, ForeignKey("misiones.id_mision"), nullable=False)
    estado = Column(String(50), default="pendiente")  # ej. pendiente, en_progreso, completado
    intentos = Column(Integer, default=0)
    fecha_completado = Column(TIMESTAMP, nullable=True)

    usuario = relationship("Usuario", back_populates="progresos")
    mision = relationship("Mision", back_populates="progresos")


class Logro(Base):
    __tablename__ = "logros"

    id_logro = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)

    usuarios_logros = relationship("UsuarioLogro", back_populates="logro", cascade="all, delete-orphan")


class UsuarioLogro(Base):
    __tablename__ = "usuarios_logros"

    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), primary_key=True)
    id_logro = Column(Integer, ForeignKey("logros.id_logro"), primary_key=True)

    usuario = relationship("Usuario", back_populates="usuarios_logros")
    logro = relationship("Logro", back_populates="usuarios_logros")
