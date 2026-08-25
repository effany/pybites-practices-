from sqlmodel import SQLModel, Field, create_engine


class Workout(SQLModel, table=True):
    """Define id (primary key) and name fields."""
    id: int | None = Field(default=None, primary_key=True)
    name: str 
    


class Exercise(SQLModel, table=True):
    """Define id (primary key) and name fields."""
    id : int | None = Field(default=None, primary_key=True)
    name: str


sqlite_url = "sqlite:///:memory:"
engine = create_engine(sqlite_url)  # Create engine using sqlite_url


def create_tables() -> None:
    """Create all tables in the database."""
    SQLModel.metadata.create_all(engine)