from sqlalchemy import Column, Integer, ForeignKey, String, Table
from sqlalchemy.orm import relationship

from ..database import Base

ip_port = Table('ip_port', Base.metadata,
                Column('ip_id', Integer, ForeignKey('ips.id'), primary_key=True),
                Column('port_id', Integer, ForeignKey('ports.id'), primary_key=True)
                )


class Ips(Base):
    __tablename__ = 'ips'

    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False, unique=True)
    packet_count = Column(Integer, default=0)
    byte_count = Column(Integer, default=0)
    name = Column(String, unique=True, nullable=True)

    ports = relationship('Port', secondary=ip_port, back_populates='ips')


class Port(Base):
    __tablename__ = 'ports'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    protocol = Column(String, nullable=False)
    packet_count = Column(Integer, default=0)
    byte_count = Column(Integer, default=0)

    ips = relationship('IP', secondary=ip_port, back_populates='ports')
