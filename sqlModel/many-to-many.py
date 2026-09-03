from __future__ import annotations

from sqlmodel import Field, SQLModel, create_engine, Relationship, Session, select


class WorkoutExercise(SQLModel, table=True):
    """Link table with id, workout_id, and exercise_id fields."""
    id: int | None = Field(default=None, primary_key=True)
    workout_id: int | None = Field(foreign_key='workout.id')
    exercise_id: int | None = Field(foreign_key='exercise.id')


class Workout(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    # Add exercises relationship using link_model
    exercises: list["Exercise"] = Relationship (
        back_populates='workouts', 
        link_model=WorkoutExercise
    )


class Exercise(SQLModel, table=True):
    """Define id, name, and workouts relationship using link_model."""
    id: int | None = Field(default=None, primary_key=True)
    name: str
    workouts: list[Workout] = Relationship(
        back_populates='exercises',
        link_model=WorkoutExercise
    )


sqlite_url = "sqlite:///:memory:"
engine = create_engine(sqlite_url, echo=False)


def create_tables() -> None:
    SQLModel.metadata.create_all(engine)


def add_exercise_to_workout(workout_id: int, exercise_name: str) -> Exercise:
    """
    Add an exercise to a workout. Create the exercise if it doesn't exist.
    Raise ValueError if workout not found.
    """
    with Session(engine) as session:
        workout = session.get(Workout, workout_id)
        if workout is None:
            raise ValueError(f"Workout doesn't exist")
        
        exercise = session.exec(
            select(Exercise).where(Exercise.name == exercise_name)
        ).first()

        if exercise is None:
            exercise = Exercise(name=exercise_name)

        workout.exercises.append(exercise)
        session.add(workout)
        session.commit()
        session.refresh(exercise)
        return exercise



def get_workout_exercises(workout_id: int) -> list[Exercise]:
    """Get all exercises for a workout, sorted by name. Return empty list if not found."""
    with Session(engine) as session:
        workout = session.get(Workout, workout_id)
        if workout is None:
            return []
        return sorted(workout.exercises, key= lambda e: e.name)
        