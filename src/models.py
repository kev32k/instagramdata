import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Login(Base):
    __tablename__ = 'Login'
    id = Column(Integer, primary_key=True)
    Nombre_Usuario = Column(String(20))
    Primer_Apellido = Column(String(20))
    Segundo_Apellido = Column(String(20))
    Password = Column(String(20))
    Confirmacion_Password = Column(String(20))
    Estado_Cuenta = Column(Boolean, default=True)

class Usuario(Base):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True)
    Nickname = Column(String(15))
    Correo = Column(String(30))
    Telefono = Column(Integer)
    Sexo = Column(Integer)
    Estado_Cuenta = Column(Integer, ForeignKey('Login.Estado_Cuenta'))
    Nombre_Usuario = Column(Integer, ForeignKey('Login.Nombre_Usuario'))
    Primer_Apellido = Column(Integer, ForeignKey('Login.Primer_Apellido'))
    Segundo_Apellido = Column(Integer, ForeignKey('Login.Segundo_Apellido'))
    Password = Column(Integer, ForeignKey('Login.Password'))
    Confirmacion_Password = Column(Integer, ForeignKey('Login.Confirmacion_Password'))
    Login = relationship(Login)

class Like(Base):
    __tablename__ = 'Like'    
    id = Column(Integer, primary_key=True)
    Cantidad_Like = Column(Integer)
    Nombre_Usuario = Column(String(25))
    Nickname = Column(String(25))
    Seguir = Column(Boolean, default=True)

class Publicacion(Base):
    __tablename__ = 'Publicacion'  
    id = Column(Integer, primary_key=True)
    Titulo = Column(String(20))
    Foto = Column(String(25))
    Video = Column(String(30))
    Texto = Column(String(45))
    Comentario = Column(String(200))
    Cantidad_Like = Column(Integer, ForeignKey('Like.Cantidad_Like'))
    Like = relationship(Like)    

class Home(Base):
    __tablename__ = 'Home' 
    id = Column(Integer, primary_key=True)
    N_Publicaciones = Column(Integer)
    N_Seguidos = Column(Integer)
    Biografia = Column(String(150))
    Publicacion_id = Column(Integer, ForeignKey('Publicacion.id'))
    Publicacion = relationship(Publicacion)
    Usuario_id = Column(Integer, ForeignKey('Usuario.id'))
    Nickname = Column(Integer, ForeignKey('Usuario.Nickname'))
    Nombre_Usuario = Column(Integer, ForeignKey('Usuario.Nombre_Usuario'))
    Usuario = relationship(Usuario)    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')