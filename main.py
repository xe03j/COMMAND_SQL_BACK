from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import create_tables
from controllers import (
    nivel_controller,
    mision_controller,
    usuario_controller,
    progreso_controller,
    logro_controller,
    auth_controller,
)

origins = ["*"]

app = FastAPI(title="API de Command SQL",
              version="1.0",
              description="Esta es una API para gestionar el juego Commad SQL",
            )

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_controller.router)
app.include_router(nivel_controller.router)
app.include_router(mision_controller.router)
app.include_router(usuario_controller.router)
app.include_router(progreso_controller.router)
app.include_router(logro_controller.router)

@app.on_event("startup")
def startup_event():
    create_tables()
