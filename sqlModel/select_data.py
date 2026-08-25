from sqlmodel import Field, SQLModel, create_engine, Session, select


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


def get_workout(workout_id: int) -> Workout | None:
    """Fetch a workout by its primary key."""
    ...
    with Session(engine) as session:
        workout = session.get(Workout, workout_id)
    return workout

def list_workouts() -> list[Workout]:
    """Return all workouts ordered by id."""
    ...
    with Session(engine) as session:
        return list(session.exec(select(Workout).order_by(Workout.id)))


def find_exercise_by_name(name: str) -> Exercise | None:
    """Find an exercise by exact name match."""
    ...
    with Session(engine) as session:
        statement = select(Exercise).where(Exercise.name == name)
        exercise = session.exec(statement).first()
    return exercise

def list_exercises() -> list[Exercise]:
    """Return all exercises ordered by name."""
    ...
    statement = select(Exercise).order_by(Exercise.name)

    with Session(engine) as session:
        return list(session.exec(statement))
    