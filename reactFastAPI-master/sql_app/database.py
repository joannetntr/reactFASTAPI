from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://sonppaispvctmrgufiwf:pscale_pw_z4Vo3GMxAwdN6EYrRkbg2B3mPsn4q9PnhhhyIeKL7Ww@aws.connect.psdb.cloud/reactapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()