import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'




class Post(Base):
    __tablename__ = "post"
    title = Column(String(255), nullable=False)
    id = Column(Integer, primary_key=True, autoincrement=True)
    views = Column(Integer, default=0)
    likes= Column(Integer, default=0)
    created_at = Column(String(50), default=(
        datetime.utcnow().strftime('%Y-%m-%d %H:%M')))
    edit_time = Column(String(50), default=(datetime.utcnow().strftime('%Y-%m-%d %H:%M')),
        onupdate=datetime.utcnow().strftime('%Y-%m-%d %H:%M'))
    content=Column(String(99999999), nullable=False)
    img_path = Column(String(1000), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'title': self.title,
            'views': self.views,
            'likes':self.likes,
            'content':self.content,
            'created at': self.created_at,
            'edit time': self.edit_time,
            'id': self.id,
        }

engine = create_engine(
  'sqlite:///item.dp')
Base.metadata.create_all(engine)
