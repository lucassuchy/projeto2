from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

#importa a conexão
from ..database import Base

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	documento = Column(Integer, index=True)
	hashed_password = Column(String)
	birth = Column(Date, default=True)
	is_active = Column(Boolean, default=True)
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True))

	type_id = Column(Integer, ForeignKey("type.id"))
    
# Vou criar os users e o types primeiro pra teste
    
class Types(Base):
	__tablename__ = 'type'

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True))

# Tinha criado o tipo fisioterapeuta, mas com a tipagem do user não precisou

class Specialty(Base):
	__tablename__ = 'specialty'

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True))
    
class Physiotherapist(Base):
	__tablename__ = 'physiotherapist'

	id = Column(Integer, primary_key=True, index=True)
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True))
	user_id = Column(Integer, ForeignKey("users.id"))
	Specialty_id = Column(Integer, ForeignKey("specialty.id"))
    
class Treatment(Base):
	__tablename__ = 'treatment'

	id = Column(Integer, primary_key=True, index=True)
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
	user_id = Column(Integer, ForeignKey("users.id"))
	physiotherapist_id = Column(Integer, ForeignKey("physiotherapist.id"))
	treatment_id = Column(Integer, ForeignKey("treatment.id"))
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True))
