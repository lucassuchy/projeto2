from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Date, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict

#importa a conexão
from ..database import Base

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	document = Column(BigInteger(), index=True)
	password = Column(String)
	birth_date = Column(Date, default=True)
	is_active = Column(Boolean, default=True)
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True))

	type_id = Column(Integer, ForeignKey("type.id"))
	physiotherapists = relationship("Physiotherapist", back_populates="user")

class Physiotherapist(Base):
	__tablename__ = 'physiotherapist'

	id = Column(Integer, primary_key=True, index=True)
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True))

	user_id = Column(Integer, ForeignKey("users.id"))
	specialty_id = Column(Integer, ForeignKey("specialty.id"))
	user = relationship("User", back_populates="physiotherapists")
    
class Types(Base):
	__tablename__ = 'type'

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True))

class Specialty(Base):
	__tablename__ = 'specialty'

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True))

    

    
class Treatment(Base):
	__tablename__ = 'treatment'

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)
	video = Column(String)
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True))

class Patient(Base):
	__tablename__ = 'patient'

	id = Column(Integer, primary_key=True, index=True)
	quantity = Column(Integer)
	duration = Column(Integer)
	description = Column(String)
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True))

	treatment_id = Column(Integer, ForeignKey("treatment.id"))
	user_id = Column(Integer, ForeignKey("users.id"))
	physiotherapist_id = Column(Integer, ForeignKey("physiotherapist.id"))



class Videos(Base):
	__tablename__ = 'videos'

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)
	videos = Column(MutableDict.as_mutable(JSONB))
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True))
