from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from auth.dependencies import get_current_user
from database.database import get_db
from repository.logro_repository_impl import LogroRepositoryImpl
from service.logro_service import LogroService
from models.models import Logro, UsuarioLogro, Usuario
from models.schemas import LogroCreate, LogroResponse, UsuarioLogroCreate, UsuarioLogroResponse

router = APIRouter(prefix="/logros", tags=["Logros"])


def get_service(db: Session = Depends(get_db)):
    repo = LogroRepositoryImpl(db)
    return LogroService(repo)

# Listar todos los logros
@router.get("/ver", response_model=List[LogroResponse])
def listar_logros(
    current_user: Usuario = Depends(get_current_user),
    service: LogroService = Depends(get_service)
):
    return service.obtener_logros()


# Crear un nuevo logro
@router.post("/create", response_model=LogroResponse)
def crear_logro(
    logro: LogroCreate,
    current_user: Usuario = Depends(get_current_user),
    service: LogroService = Depends(get_service)
):
    nuevo = Logro(**logro.dict())
    return service.crear_logro(nuevo)


# Asignar un logro a un usuario
@router.post("/logrousuario", response_model=UsuarioLogroResponse)
def asignar_logro(
    usuario_logro: UsuarioLogroCreate,
    current_user: Usuario = Depends(get_current_user),
    service: LogroService = Depends(get_service)
):
    nuevo = UsuarioLogro(**usuario_logro.dict())
    return service.asignar_logro_a_usuario(nuevo)


# obtener logros de un usuario
@router.get("/usuario/{id_usuario}", response_model=List[LogroResponse])
def obtener_logros_usuario(
    id_usuario: int,
    current_user: Usuario = Depends(get_current_user),
    service: LogroService = Depends(get_service)
):
    return service.obtener_logros_por_usuario(id_usuario)