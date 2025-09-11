from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from auth.dependencies import get_current_user
from database.database import get_db
from repository.mision_repository_impl import MisionRepositoryImpl
from service.mision_service import MisionService
from models.models import Mision, Usuario
from models.schemas import MisionCreate, MisionResponse

router = APIRouter(prefix="/misiones", tags=["Misiones"])


def get_service(db: Session = Depends(get_db)):
    repo = MisionRepositoryImpl(db)
    return MisionService(repo)


# Listar todas las misiones
@router.get("/", response_model=List[MisionResponse])
def listar_misiones(
    current_user: Usuario = Depends(get_current_user),
    service: MisionService = Depends(get_service)
):
    return service.obtener_misiones()


# Obtener misión por ID
@router.get("/{id_mision}", response_model=MisionResponse)
def obtener_mision(
    id_mision: int,
    current_user: Usuario = Depends(get_current_user),
    service: MisionService = Depends(get_service)
):
    mision = service.obtener_mision_por_id(id_mision)
    if not mision:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Misión no encontrada")
    return mision


# Listar misiones por nivel
@router.get("/nivel/{id_nivel}", response_model=List[MisionResponse])
def listar_misiones_por_nivel(
    id_nivel: int,
    current_user: Usuario = Depends(get_current_user),
    service: MisionService = Depends(get_service)
):
    return service.obtener_misiones_por_nivel(id_nivel)


# Crear misión (🔒 protegido con JWT)
@router.post("/", response_model=MisionResponse)
def crear_mision(
    mision: MisionCreate,
    current_user: Usuario = Depends(get_current_user),
    service: MisionService = Depends(get_service)
):
    nueva = Mision(**mision.dict())
    return service.crear_mision(nueva)

@router.post("/bulk_create", response_model=List[MisionResponse])
def crear_misiones(
    misiones: List[MisionCreate],
    current_user: Usuario = Depends(get_current_user),
    service: MisionService = Depends(get_service)
):
    nuevas = [Mision(**m.dict()) for m in misiones]
    return service.crear_misiones(nuevas)