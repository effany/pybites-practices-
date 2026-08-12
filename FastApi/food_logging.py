from datetime import datetime
from typing import Any, Dict, List

from fastapi import FastAPI, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel

# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# We'll export authentication further in a later Bite
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


class Food(BaseModel):
    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


class User(BaseModel):
    id: int
    username: str
    password: str

    def __init__(self, **data: Any):
        data["password"] = get_password_hash(data["password"])
        super().__init__(**data)


class FoodEntry(BaseModel):
    id: int
    user: User
    food: Food
    date_added: datetime = datetime.now()
    number_servings: float

    @property
    def total_calories(self):
        return self.food.kcal_per_serving * self.number_servings


app = FastAPI()
food_log: Dict[int, FoodEntry] = {}

# We've hidden the previous Food CRUD to keep it compact and to force you to
# repeat the API building process (deliberate practice is key!)

# Create CRUD endpoints for FoodEntry below as per instructions in the Bite ...
@app.post("/", status_code=201)
async def create_foodentry(foodentry: FoodEntry):
    food_log[foodentry.id] = foodentry
    return foodentry

@app.get("/users/{user_id}", status_code=200)
async def get_food_user(user_id: int):
    user_array = []
    for entry in food_log.values():
        if entry.user.id == user_id:
            user_array.append(entry)

    return user_array

@app.put("/{entry_id}", status_code=200)
async def update_food(entry_id: int, foodentry: FoodEntry):
    if entry_id in food_log:
        food_log[entry_id] = foodentry
        return foodentry
    else:
        raise HTTPException(status_code=404, detail="Food entry not found")

@app.delete("/{entry_id}", status_code=200)
async def delete_item(entry_id: int):
    if entry_id in food_log:
        food_log.pop(entry_id)
        return {"ok": True}
    else:
        raise HTTPException(status_code=404, detail="Food entry not found")