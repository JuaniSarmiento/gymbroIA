from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.user import UserCreate, User as UserSchema
from services import user_service
from database import AsyncSessionLocal

router = APIRouter()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user_endpoint(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Endpoint para crear un nuevo usuario.
    """
    return await user_service.create_new_user(user_in=user_in, db=db)