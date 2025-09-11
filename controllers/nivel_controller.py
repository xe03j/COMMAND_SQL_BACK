from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from auth.dependencies import get_current_user
from database.database import get_db
from repository.nivel_repository_impl import NivelRepositoryImpl
from service.nivel_service import NivelService
from models.models import Nivel, Usuario
from models.schemas import NivelCreate, NivelResponse

router = APIRouter(prefix="/niveles", tags=["Niveles"])


def get_service(db: Session = Depends(get_db)):
    repo = NivelRepositoryImpl(db)
    return NivelService(repo)

# Listar los niveles
@router.get("/ver", response_model=List[NivelResponse])
def listar_niveles(
    current_user: Usuario = Depends(get_current_user),
    service: NivelService = Depends(get_service)
):
    return service.obtener_niveles()


# Obtener un nivel por ID
@router.get("/{id_nivel}", response_model=NivelResponse)
def obtener_nivel(
    id_nivel: int,
    current_user: Usuario = Depends(get_current_user),
    service: NivelService = Depends(get_service)
):
    nivel = service.obtener_nivel_por_id(id_nivel)
    if not nivel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nivel no encontrado")
    return nivel


# Crear un nivel
@router.post("/create", response_model=NivelResponse)
def crear_nivel(
    nivel: NivelCreate,
    current_user: Usuario = Depends(get_current_user),
    service: NivelService = Depends(get_service)
):
    nuevo = Nivel(**nivel.dict())
    return service.crear_nivel(nuevo)

from typing import List

@router.post("/bulk_create", response_model=List[NivelResponse])
def crear_niveles(
    niveles: List[NivelCreate],
    current_user: Usuario = Depends(get_current_user),
    service: NivelService = Depends(get_service)
):
    nuevos = [Nivel(**nivel.dict()) for nivel in niveles]
    return service.crear_niveles(nuevos)
