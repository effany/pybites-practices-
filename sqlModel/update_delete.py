from sqlmodel import Field, SQLModel, create_engine, select, Session


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


def update_workout(workout_id: int, new_name: str) -> Workout | None:
    """Update a workout's name. Return None if not found."""
    ...
    with Session(engine) as session:
        workout = session.get(Workout, workout_id)
        if workout:
            workout.name = new_name
            session.commit()
            session.refresh(workout)
            return workout
        else:
            return None



def delete_workout(workout_id: int) -> bool:
    """Delete a workout. Return False if not found."""
    ...
    with Session(engine) as session:
        workout = session.get(Workout, workout_id)
        if workout:
            session.delete(workout)
            session.commit()
            return True
        else:
            return False


def update_exercise(exercise_id: int, new_name: str) -> Exercise | None:
    """Update an exercise's name. Return None if not found."""
    ...
    with Session(engine) as session:
        exercise = session.get(Exercise, exercise_id)
        if exercise:
            exercise.name = new_name
            session.commit()
            session.refresh(exercise)
            return exercise
        else:
            return None
        


def delete_exercise(exercise_id: int) -> bool:
    """Delete an exercise. Return False if not found."""
    ...
    with Session(engine) as session:
        exercise = session.get(Exercise, exercise_id)
        if exercise:
            session.delete(exercise)
            session.commit()
            return True
        else:
            return False