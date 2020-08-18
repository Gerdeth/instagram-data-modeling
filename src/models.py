import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__="follower"
    ID=Column(Integer,primary_key=True)
    user_from_id= Column (Integer,nullable=False)
    user_to_id= Column(Integer,ForeignKey("user.id"),nullable=False)
    user=relationship("User")

class User(Base):
    __tablename__ = "user"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    firstname= Column (String,nullable=False)
    lastname= Column(String,nullable=False)
    email= Column(String,nullable=False)
    follower=relationship("Follower")
    post=relationship("Post")
    comment=relationship("Comment")

class Post(Base):
    __tablename__="post"
    id= Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("user.id"),nullable=False)
    user=relationship("User")
    media=relationship("Media")

class Media(Base):
    __tablename__="media"
    id = Column(Integer, primary_key=True)
    type=Column(String,nullable=False)
    url= Column(String,nullable=False)
    post_id=Column(Integer, ForeignKey("post.id"),nullable=False)
    post=relationship("Post")

class Comment(Base):
     __tablename__="comment"
     id = Column(Integer, primary_key=True)
     comment_text=Column(String, nullable=False)
     author_id=Column(Integer, ForeignKey("user.id"),nullable=False)
     post_id=Column(Integer,ForeignKey("post.id") ,nullable=False)
     user=relationship("User")



# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')