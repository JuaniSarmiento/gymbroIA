from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Creamos el motor de base de datos asincrónico
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Creamos una fábrica de sesiones asincrónicas
AsyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)
