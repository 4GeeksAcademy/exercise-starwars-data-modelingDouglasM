import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


usuario_personaje = Table('usuario_personaje', Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuario.id'), primary_key=True),
    Column('personaje_id', Integer, ForeignKey('personaje.id'), primary_key=True)
)


usuario_planeta = Table('usuario_planeta', Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuario.id'), primary_key=True),
    Column('planeta_id', Integer, ForeignKey('planeta.id'), primary_key=True)
)

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    fecha_suscripcion = Column(String(250))

    personajes = relationship('Personaje', secondary=usuario_personaje, back_populates='usuarios')
    planetas = relationship('Planeta', secondary=usuario_planeta, back_populates='usuarios')

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    genero = Column(String(250))
    especie = Column(String(250))

    usuarios = relationship('Usuario', secondary=usuario_personaje, back_populates='personajes')

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    clima = Column(String(250))
    terreno = Column(String(250))

    usuarios = relationship('Usuario', secondary=usuario_planeta, back_populates='planetas')

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personaje.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'))

    usuario = relationship('Usuario')
    personaje = relationship('Personaje')
    planeta = relationship('Planeta')


render_er(Base, 'diagram.png')
