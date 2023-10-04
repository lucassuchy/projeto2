from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
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
class Especialidade(Base):
	__tablename__ = 'especialidade'
    
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True))

class Fisioterapeuta_especialidade(Base):
	__tablename__ = 'fisioterapeuta_especialidade'
    
	id = Column(Integer, primary_key=True, index=True)
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True))
	user_id = Column(Integer, ForeignKey("users.id"))
	especialidade_id = Column(Integer, ForeignKey("especialidade.id"))

# Aqui eu vou precisar fazer diferente do que ta no desenho
class Tratamento(Base):
	__tablename__ = 'tratamento'
    
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True))

class Tratamento_Paciente(Base):
	__tablename__ = 'tratamento_paciente'
    
	id = Column(Integer, primary_key=True, index=True)
	created_At = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), server_default=func.now())
	delete_at =  Column(DateTime(timezone=True))
	tratamento_id = Column(Integer, ForeignKey("tratamento.id"))
	paciente_id = Column(Integer, ForeignKey("users.id"))