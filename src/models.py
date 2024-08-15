import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    subscription = Column(String(250))

    favorite = relationship('favorite', backref='user')

class character(Base):
    __tablename__ = 'character'
    character_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250))
    species = Column(String(250))

    favorite = relationship('favorite', backref='Character')

class planet(Base):
    __tablename__ = 'planet'
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    land = Column(String(250))

    favorite = relationship('favorite', backref='planet')

class favorite(Base):
    __tablename__ = 'favorite'
    favorite_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.character_id'))
    planet_id = Column(Integer, ForeignKey('planet.planet_id'))

    user = relationship('User', backref='favorite')
    character = relationship('character', backref='favorite')
    planet = relationship('planet', backref='favorite')


render_er(Base, 'diagram.png')
