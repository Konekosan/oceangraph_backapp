from app.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

class Utilisateur(Base):
    __tablename__='Utilisateur'

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    prenom = Column(String, index=True)
    age = Column(Integer, index=True)
    username = Column(String, unique=True)
    hashed_pwd = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)