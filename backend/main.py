from fastapi import FastAPI

# Creamos la instancia de la aplicación.
# Esta variable "app" es el corazón de nuestro backend.
app = FastAPI(title="GymBro AI API", version="0.1.0")


@app.get("/")
def read_root():
    """
    Este es nuestro primer endpoint.
    Cuando alguien visite la raíz de nuestra API, le devolveremos este saludo.
    """
    return {"message": "¡Bienvenido a GymBro AI, papá! El motor está encendido."}