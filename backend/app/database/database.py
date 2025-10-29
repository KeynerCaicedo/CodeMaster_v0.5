from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Cargar variables del .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Crear engine async
engine = create_async_engine(
    DATABASE_URL,
    echo=True, 
    future=True
)

# Crear session async
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base para los modelos ORM
Base = declarative_base()

# Dependencia para usar en FastAPI 
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
