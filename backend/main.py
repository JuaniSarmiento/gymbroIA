from fastapi import FastAPI
from api.endpoints import user

app = FastAPI(title="GymBro AI API", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a GymBro AI, papá! El motor está encendido."}

# Incluimos el router de usuarios
app.include_router(user.router, prefix="/users", tags=["Users"])