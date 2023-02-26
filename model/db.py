
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Substitua as informações abaixo pela URL de conexão do seu SQL Server
SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://sa:Tlps1127*@localhost/ESTUDO_2023?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True, 
	pool_size=10, 
	max_overflow=20, 
	connect_args={"autocommit": True}, 
	isolation_level="READ COMMITTED", 
	fast_executemany=True, 
	echo_pool=True, 
	pool_pre_ping=True, 
	pool_recycle=300

)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Cria as tabelas no SQL Server
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
