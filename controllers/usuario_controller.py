from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from auth.dependencies import get_current_user
from database.database import get_db
from repository.usuario_repository_impl import UsuarioRepositoryImpl
from service.usuario_service import UsuarioService
from models.models import Usuario
from models.schemas import UsuarioCreate, UsuarioResponse, UsuarioUpdateXP

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


def get_service(db: Session = Depends(get_db)):
    repo = UsuarioRepositoryImpl(db)
    return UsuarioService(repo)


@router.get("/me", response_model=UsuarioResponse)
def leer_perfil(current_user: Usuario = Depends(get_current_user)):
    return current_user


@router.get("/ver", response_model=List[UsuarioResponse])
def listar_usuarios(
        current_user: Usuario = Depends(get_current_user),  # seguridad
        service: UsuarioService = Depends(get_service)  # servicio
):
    return service.obtener_usuarios()


# Obtener usuario por ID (protegido)
@router.get("/{id_usuario}", response_model=UsuarioResponse)
def obtener_usuario(
    id_usuario: int,
    current_user: Usuario = Depends(get_current_user),
    service: UsuarioService = Depends(get_service)
):
    usuario = service.obtener_usuario_por_id(id_usuario)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario


# Obtener usuario por email (protegido)
@router.get("/email/{email}", response_model=UsuarioResponse)
def obtener_usuario_por_email(
    email: str,
    current_user: Usuario = Depends(get_current_user),
    service: UsuarioService = Depends(get_service)
):
    usuario = service.obtener_usuario_por_email(email)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario


# Crear un usuario (público)
@router.post("/create", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, service: UsuarioService = Depends(get_service)):
    nuevo = Usuario(**usuario.dict())
    return service.crear_usuario(nuevo)


@router.patch("/{id_usuario}/xp", response_model=UsuarioResponse)
def actualizar_xp_usuario(
    id_usuario: int,
    xp_update: UsuarioUpdateXP,
    current_user: Usuario = Depends(get_current_user),  # seguridad
    service: UsuarioService = Depends(get_service)
):
    usuario = service.actualizar_xp(id_usuario, xp_update.xp_total)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario