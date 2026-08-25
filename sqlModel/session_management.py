from sqlmodel import Field, SQLModel, create_engine, Session


class Workout(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str


class Exercise(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str


sqlite_url = "sqlite:///:memory:"
engine = create_engine(sqlite_url, echo=False)


def create_tables() -> None:
    SQLModel.metadata.create_all(engine)


def add_workout(name: str) -> Workout:
    """Create a workout, save it to the database, and return it with its id."""
    workout = Workout()
    workout.name = name
    with Session(engine) as session:
        session.add(workout)
        session.commit()
        session.refresh(workout)
    return workout


def add_exercise(name: str) -> Exercise:
    """Create an exercise, save it to the database, and return it with its id."""
    exercise = Exercise()
    exercise.name = name
    with Session(engine) as session:
        session.add(exercise)
        session.commit()
        session.refresh(exercise)
    return exercise