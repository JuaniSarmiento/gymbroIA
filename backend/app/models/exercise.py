from sqlalchemy import (Column, Integer, String, Text, Enum as SQLAlchemyEnum, 
                        Boolean, ForeignKey, Table)
from sqlalchemy.orm import relationship
from .base import Base

# Tabla de unión para la relación muchos-a-muchos entre Ejercicios y Músculos
exercise_muscles = Table(
    "exercise_muscles",
    Base.metadata,
    Column("exercise_id", Integer, ForeignKey("exercises.id"), primary_key=True),
    Column("muscle_id", Integer, ForeignKey("muscles.id"), primary_key=True),
    Column("is_primary", Boolean, default=True)
)

# Tabla de unión para la relación muchos-a-muchos entre Ejercicios y Tags
exercise_tags = Table(
    "exercise_tags",
    Base.metadata,
    Column("exercise_id", Integer, ForeignKey("exercises.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False, index=True)
    description = Column(Text)
    equipment_type = Column(
        SQLAlchemyEnum('Barra', 'Mancuerna', 'Máquina', 'Peso Corporal', 'Otro', name='equipment_type_enum'),
        nullable=False
    )
    media_url = Column(Text)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    owner = relationship("User")

    muscles = relationship("Muscle", secondary=exercise_muscles, backref="exercises")
    tags = relationship("Tag", secondary=exercise_tags, backref="exercises")