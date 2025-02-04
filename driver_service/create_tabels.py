from sqlmodel import SQLModel, create_engine
from core.config import settings  # Ensure you have your DB settings
from db.models import Driver  # Import all models
DATABASE_URL: str = "postgresql://postgres:123456789@localhost:5432/postgres"
engine = create_engine(DATABASE_URL,echo=True)

# Create tables if they don't exist
def create_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()
    print("✅ Tables created successfully!")
