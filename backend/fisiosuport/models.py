from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

#importa a conexão
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    documento = Column(Integer, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_At = Column(DateTime(timezone=True), server_default=func.now())
    delete_at =  Column(DateTime(timezone=True), server_default=func.now())
    
    type_id = Column(Integer, ForeignKey("type.id"))
    
# Vou criar os users e o types primeiro pra teste
    
class Types(Base):
	__tablename__ = 'type'
    
	id = Column(Integer, primary_key=True, index=True)
	type = Column(String, index=True)
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True), server_default=func.now())
	owner = relationship("User", back_populates="type")

