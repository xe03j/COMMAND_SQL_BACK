from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from database.database import get_db
from repository.usuario_repository_impl import UsuarioRepositoryImpl
from service.usuario_service import UsuarioService
from auth.auth_utils import verify_password, create_access_token, hash_password
from models.auth_schema import Token, LoginRequest
from models.models import Usuario

router = APIRouter(prefix="/auth", tags=["Auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_user_service(db: Session = Depends(get_db)):
    repo = UsuarioRepositoryImpl(db)
    return UsuarioService(repo)


@router.post("/register", response_model=Token)
def register(request: LoginRequest, service: UsuarioService = Depends(get_user_service)):
    user = service.obtener_usuario_por_email(request.email)
    if user:
        raise HTTPException(status_code=400, detail="Email ya registrado")

    nuevo = Usuario(
        nombre=request.email.split("@")[0],
        email=request.email,
        contrasena_hash=hash_password(request.password),
    )
    user = service.crear_usuario(nuevo)

    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), service: UsuarioService = Depends(get_user_service)):
    user = service.obtener_usuario_por_email(form_data.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")

    if not verify_password(form_data.password, user.contrasena_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")

    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
