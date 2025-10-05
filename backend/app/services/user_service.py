from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from models.user import User as UserModel
from schemas.user import UserCreate
from core.security import get_password_hash

async def create_new_user(user_in: UserCreate, db: AsyncSession):
    existing_user_query = await db.execute(UserModel.__table__.select().where(UserModel.email == user_in.email))
    if existing_user_query.first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un usuario con este email.",
        )

    hashed_password = get_password_hash(user_in.password)
    
    db_user = UserModel(
        first_name=user_in.first_name,
        last_name=user_in.last_name,
        email=user_in.email,
        password_hash=hashed_password,
    )

    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    return db_user