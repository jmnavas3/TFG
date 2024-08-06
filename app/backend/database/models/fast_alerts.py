from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from ..database import Base


class FastAlert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True)
    prioridad = Column(Integer, unique=False, nullable=True)
    protocolo = Column(String(10), unique=False, nullable=True)
    origen = Column(String(22), unique=False, nullable=False)
    destino = Column(String(22), unique=False, nullable=False)
    su_id = Column(String(15), unique=False, nullable=False)
    alerta = Column(Text, unique=False, nullable=False)
    clasificacion = Column(Text, unique=False, nullable=False)
