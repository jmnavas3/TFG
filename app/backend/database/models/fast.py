from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.sql import func
from ..database import Base


class Fast(Base):
    __tablename__ = "fast"

    id = Column(Integer, primary_key=True)
    prioridad = Column(Integer, unique=False, nullable=True)
    protocolo = Column(String(10), unique=False, nullable=True)
    origen = Column(String(22), unique=False, nullable=False)
    destino = Column(String(22), unique=False, nullable=False)
    identificador = Column(String(15), unique=False, nullable=False)
    alerta = Column(Text, unique=False, nullable=False)
    clasificacion = Column(Text, unique=False, nullable=False)
    fecha = Column(Text, server_default=func.now())
