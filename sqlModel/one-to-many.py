from sqlmodel import Field, SQLModel, create_engine
from datetime import date
from sqlmodel import Relationship, Session, select

class Workout(SQLModel, table=True):
    """
    The back_populates="workout" 
    tells SQLModel it pairs with a workout attribute on the LogEntry side
    """
    id: int | None = Field(default=None, primary_key=True)
    name: str
    # Add log_entries relationship
    log_entries: list["LogEntry"] = Relationship(back_populates="workout")

class LogEntry(SQLModel, table=True):
    """
    Fields needed: workout_id (foreign key), set_number, weight, reps, date_recorded.
    Also add a relationship back to Workout.
    workout here = the table name of the Workout model.
    SQLModel auto-generates the table name by lowercasing the class name: Workout → table workout.
    id = the id column in that table.
    """
    id: int | None = Field(default=None, primary_key=True)
    workout_id: int | None = Field(foreign_key="workout.id")
    set_number: int
    weight: int
    reps: int
    date_recorded: date = Field(default_factory=date.today)
    workout: Workout = Relationship(back_populates="log_entries")


sqlite_url = "sqlite:///:memory:"
engine = create_engine(sqlite_url, echo=False)


def create_tables() -> None:
    SQLModel.metadata.create_all(engine)


def add_log_entry(workout_id: int, set_number: int, weight: int, reps: int) -> LogEntry:
    """Create a log entry for a workout. Raise ValueError if workout doesn't exist."""
    ...
    with Session(engine) as session:
        workout = session.get(Workout, workout_id)

        if workout:
            log = LogEntry()
            log.workout_id = workout_id
            log.set_number = set_number
            log.weight = weight
            log.reps = reps
            session.add(log)
            session.commit()
            session.refresh(log)
        else:
            raise ValueError(f"Workout {workout_id} does not exist")

    return log


def get_log_entries(workout_id: int) -> list[LogEntry]:
    """Get all log entries for a workout, ordered by set_number."""
    ...
    with Session(engine) as session:
        statement = (
            select(LogEntry)
            .where(LogEntry.workout_id == workout_id)
            .order_by(LogEntry.set_number)
        )
        return list(session.exec(statement))
