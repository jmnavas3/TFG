from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.sql import func
from ..database import Base


class Fast(Base):
    __tablename__ = "fast"

    id = Column(Integer, primary_key=True)
    prioridad = Column(Integer, unique=False, nullable=True)
    protocolo = Column(String(10), unique=False, nullable=True)
    ip_origen = Column(String(22), unique=False, nullable=False)
    puerto_origen = Column(Integer, unique=False, nullable=False)
    ip_destino = Column(String(22), unique=False, nullable=False)
    puerto_destino = Column(Integer, unique=False, nullable=False)
    identificador = Column(String(15), unique=False, nullable=False)
    alerta = Column(Text, unique=False, nullable=False)
    clasificacion = Column(Text, unique=False, nullable=False)
    fecha = Column(DateTime(), server_default=func.now())
