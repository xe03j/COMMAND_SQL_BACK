from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


# ---------- Niveles ----------
class NivelBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    dificultad: Optional[str] = None
    tema_sql: Optional[str] = None

class NivelCreate(NivelBase):
    pass

class NivelResponse(NivelBase):
    id_nivel: int

    class Config:
        from_attributes = True


# ---------- Misiones ----------
class MisionBase(BaseModel):
    id_nivel: int
    enunciado: str
    consulta_correcta: Optional[str] = None
    tabla_base: Optional[str] = None

class MisionCreate(MisionBase):
    pass

class MisionResponse(MisionBase):
    id_mision: int

    class Config:
        from_attributes = True


# ---------- Usuarios ----------
class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr

class UsuarioUpdateXP(BaseModel):
    xp_total: int

class UsuarioCreate(UsuarioBase):
    contraseña: str  # campo que el cliente enviará; en DB guardamos el hash

class UsuarioResponse(UsuarioBase):
    id_usuario: int
    xp_total: int
    nivel_actual: Optional[int] = None
    fecha_registro: Optional[datetime] = None

    class Config:
        from_attributes = True


# ---------- Progreso ----------
class ProgresoBase(BaseModel):
    id_usuario: int
    id_mision: int
    estado: Optional[str] = "pendiente"
    intentos: Optional[int] = 0

class ProgresoCreate(ProgresoBase):
    pass

class ProgresoResponse(ProgresoBase):
    id_progreso: int
    fecha_completado: Optional[datetime] = None

    class Config:
        from_attributes = True


# ---------- Logros ----------
class LogroBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class LogroCreate(LogroBase):
    pass

class LogroResponse(LogroBase):
    id_logro: int

    class Config:
        from_attributes = True


# ---------- UsuarioLogro (asignación) ----------
class UsuarioLogroBase(BaseModel):
    id_usuario: int
    id_logro: int

class UsuarioLogroCreate(UsuarioLogroBase):
    pass

class UsuarioLogroResponse(UsuarioLogroBase):
    class Config:
        from_attributes = True
