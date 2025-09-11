from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.database import get_db
from repository.progreso_repository_impl import ProgresoRepositoryImpl
from service.progreso_service import ProgresoService
from models.models import Progreso
from models.schemas import ProgresoCreate, ProgresoResponse

router = APIRouter(prefix="/progreso", tags=["Progreso"])


def get_service(db: Session = Depends(get_db)):
    repo = ProgresoRepositoryImpl(db)
    return ProgresoService(repo)


from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from auth.dependencies import get_current_user
from database.database import get_db
from repository.progreso_repository_impl import ProgresoRepositoryImpl
from service.progreso_service import ProgresoService
from models.models import Progreso, Usuario
from models.schemas import ProgresoCreate, ProgresoResponse

router = APIRouter(prefix="/progreso", tags=["Progreso"])


# Inyección del servicio
def get_service(db: Session = Depends(get_db)):
    repo = ProgresoRepositoryImpl(db)
    return ProgresoService(repo)


# Obtener progreso de un usuario
@router.get("/usuario/{id_usuario}", response_model=List[ProgresoResponse])
def progreso_por_usuario(
    id_usuario: int,
    current_user: Usuario = Depends(get_current_user),
    service: ProgresoService = Depends(get_service)
):
    return service.obtener_progreso_por_usuario(id_usuario)


# Obtener progreso de un usuario en una misión específica
@router.get("/usuario/{id_usuario}/mision/{id_mision}", response_model=ProgresoResponse)
def progreso_mision(
    id_usuario: int,
    id_mision: int,
    current_user: Usuario = Depends(get_current_user),
    service: ProgresoService = Depends(get_service)
):
    progreso = service.obtener_progreso_mision(id_usuario, id_mision)
    if not progreso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Progreso no encontrado")
    return progreso


# Registrar/actualizar progreso
@router.post("/saveprogres", response_model=ProgresoResponse)
def guardar_progreso(
    data: ProgresoCreate,
    db: Session = Depends(get_db)
):
    progreso = db.query(Progreso).filter_by(
        id_usuario=data.id_usuario,
        id_mision=data.id_mision
    ).first()

    if progreso:
        if progreso.estado == "completada":
            # ⚠️ Ya estaba completada, no sumamos XP otra vez
            return progreso
        else:
            # 🔄 Actualizar progreso existente
            progreso.estado = data.estado
            progreso.intentos = data.intentos
            progreso.fecha_completado = datetime.utcnow()
            db.commit()
    else:
        # 🆕 Nuevo progreso
        progreso = Progreso(
            id_usuario=data.id_usuario,
            id_mision=data.id_mision,
            estado=data.estado,
            intentos=data.intentos,
            fecha_completado=datetime.utcnow()
        )
        db.add(progreso)
        db.commit()

    # ✅ Solo sumamos XP si se completó por primera vez
    if data.estado == "completada":
        usuario = db.query(Usuario).filter_by(id_usuario=data.id_usuario).first()
        if usuario:
            usuario.xp_total += 6  # 👈 XP fijo por misión (puedes parametrizarlo)
            db.commit()

    return progreso