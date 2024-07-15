import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    usuario_id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    fecha_suscripcion = Column(String(250))

  

class Personaje(Base):
    __tablename__ = 'personaje'
    personaje_id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    genero = Column(String(250))
    especie = Column(String(250))


class Planeta(Base):
    __tablename__ = 'planeta'
    planeta_id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    clima = Column(String(250))
    terreno = Column(String(250))


class Favorito(Base):
    __tablename__ = 'favorito'
    favorito_id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personaje.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'))

    usuario = relationship('Usuario')
    personaje = relationship('Personaje')
    planeta = relationship('Planeta')


render_er(Base, 'diagram.png')
