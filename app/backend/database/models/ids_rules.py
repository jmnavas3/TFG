from sqlalchemy import Column, Integer, Text, Boolean

from ..database import Base


class IdsRules(Base):
    __tablename__ = "ids_rules"

    id = Column(Integer, primary_key=True)
    rule = Column(Text, unique=False, nullable=False)
    sid = Column(Integer, unique=False, nullable=True)
    rev = Column(Integer, unique=False, nullable=True)
    msg = Column(Text, unique=False, nullable=False)
    active = Column(Boolean, unique=False, nullable=False, default=True)
