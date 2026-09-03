from datetime import date

from sqlmodel import Field, Relationship, SQLModel, create_engine, Session, select


class WorkoutExercise(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    workout_id: int | None = Field(default=None, foreign_key="workout.id")
    exercise_id: int | None = Field(default=None, foreign_key="exercise.id")
    # Add log_entries relationship
    log_entries: list["LogEntry"] = Relationship(
        back_populates='workoutexercise'
    )


class Workout(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    exercises: list["Exercise"] = Relationship(
        back_populates="workouts", link_model=WorkoutExercise
    )


class Exercise(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    workouts: list[Workout] = Relationship(
        back_populates="exercises", link_model=WorkoutExercise
    )


class LogEntry(SQLModel, table=True):
    """
    Add workoutexercise_id (foreign key) and workoutexercise relationship
    instead of linking directly to workout.
    """

    id: int | None = Field(default=None, primary_key=True)
    set_number: int
    weight: int
    reps: int
    date_recorded: date = Field(default_factory=date.today)
    workoutexercise: WorkoutExercise | None = Relationship (
        back_populates='log_entries'
    )
    workoutexercise_id: int | None = Field(
        default=None, 
        foreign_key="workoutexercise.id"
    )


sqlite_url = "sqlite:///:memory:"
engine = create_engine(sqlite_url, echo=False)


def create_tables() -> None:
    SQLModel.metadata.create_all(engine)


def add_log_entry(
    workout_id: int, exercise_id: int, set_number: int, weight: int, reps: int
) -> LogEntry:
    """
    Create a log entry for a workout-exercise pair.
    Raise ValueError if the pair doesn't exist.
    """
    with Session(engine) as session:
            statement = select(WorkoutExercise).where(
                WorkoutExercise.workout_id == workout_id,
                WorkoutExercise.exercise_id == exercise_id
            )
            workoutexercise = session.exec(statement).first()
            if workoutexercise is None:
                raise ValueError("Workout-exercise pair does not exist")
            
            logentry = LogEntry(
                set_number=set_number, 
                weight=weight, 
                reps=reps)
            
            workoutexercise.log_entries.append(logentry)
            session.add(logentry)
            session.commit()
            session.refresh(logentry)
            return logentry
           

def get_log_entries(workout_id: int, exercise_id: int) -> list[LogEntry]:
    """
    Get log entries for a workout-exercise pair, ordered by date then set_number.
    Return empty list if pair not found.
    """
    with Session(engine) as session:
        statement = select(WorkoutExercise).where(
                        WorkoutExercise.workout_id == workout_id,
                        WorkoutExercise.exercise_id == exercise_id
                    )
        result = session.exec(statement).first()
        if result is None:
            return []

        statement = (
            select(LogEntry)
            .where(LogEntry.workoutexercise_id == result.id)
            .order_by(LogEntry.date_recorded, LogEntry.set_number)
        )

        return session.exec(statement).all()
