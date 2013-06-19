from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Float
from sqlalchemy import String, DateTime, Boolean, UnicodeText
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

def init_db(engine):
	Base.metadata.create_all(bind=engine)

def clean_db(engine):
	Base.metadata.drop_all(bind=engine)


class Company(Base):
	__tablename__='company'
	id=Column(Integer,primary_key=True)
	name=Column(String(32),index=True)
	def __init__(self,name):
		self.name=name;

class User(Base):
	__tablename__='user'
	id=Column(Integer,primary_key=True)
	username=Column(String(32),index=True,unique=True)
	password=Column(String(32))
	email=Column(String(32))
	time=Column(DateTime,default=datetime.now)
	#cid=Column(Integer)
	#goods=relationship("orders",backref="orders")

	def __init__(self,username,password,email):
		self.username=username
		self.password=password
		self.email=email

#	def __repr__(self):
#		return 'name %s' % self.username

class Goods(Base):
	__tablename__='goods'
	id=Column(Integer,primary_key=True)
	goodsname=Column(String(32))
	companyid=Column(Integer)
	def __init__(self,goodsname,companyid):
		self.goodsname=goodsname
		self.companyid=companyid

class Orders(Base):
	__tablename__='orders'
	id=Column(Integer,primary_key=True)
	goodsid=Column(Integer,ForeignKey('goods.id'))
	userid=Column(Integer,ForeignKey('user.id'))
	time=Column(DateTime,default=datetime.now)
	#goods=relationship("goods")
	
	def __init__(self,goodsid,userid):
		self.goodsid=goodsid
		self.userid=userid			
#
