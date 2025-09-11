from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from database.database import get_db
from repository.usuario_repository_impl import UsuarioRepositoryImpl
from service.usuario_service import UsuarioService
from auth.auth_utils import SECRET_KEY, ALGORITHM
from models.auth_schema import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_user_service(db: Session = Depends(get_db)):
    repo = UsuarioRepositoryImpl(db)
    return UsuarioService(repo)


def get_current_user(token: str = Depends(oauth2_scheme), service: UsuarioService = Depends(get_user_service)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar el token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = service.obtener_usuario_por_email(email)
    if user is None:
        raise credentials_exception
    return user
