from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import (Table, Column, Integer, Numeric, String, DateTime,
 ForeignKey) 
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://win:123-09qwe'
 '@82.157.251.139/cspj', pool_recycle=3600)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
class Hello(Base):
    __tablename__ = "hello"
    
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50), default="Hello!")
    
    def __repr__(self) -> str:
        return "id:{self.id}, name:{self.name}\n".format(self=self)

# Base.metadata.create_all(engine)

"""
h1 = Hello(name="Hello, gogo")
session.add(h1)
session.commit()

print(h1)
print(h1.id, h1.name)
"""

res = session.query(Hello).filter(Hello.name=="Hello, gogo")
print(res)
res.update({Hello.name: Hello.name + " in 1029!"})
session.commit()
print(res)