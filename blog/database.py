from sqlalchemy import create_engine
SQLALCHEMY_DATABASE_URL="sqlite:///./blog.db"
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})

Base = declarative_base()
Session = sessionmaker(bind=engine,autoflush=False,autocommit=False,)
