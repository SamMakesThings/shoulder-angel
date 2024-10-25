import os
from fastapi import APIRouter, HTTPException
import sqlite3
import weave

from src.models import GeminiGoalUpdater

router = APIRouter()
config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
        },
    },
}


import os

@weave.op()
def get_goals_str() -> str:
    try:
        with open(os.path.join("..", "data", "goals.txt"), "r") as f:
            goals = f.read().strip()
        return goals
    except FileNotFoundError:
        return "No goals found."
    except IOError:
        return "Error reading goals file."

@weave.op()
def update_goals_str(goals: str, conversation: str) -> str:
    goal_updater = GeminiGoalUpdater(model="gemini-1.5-pro-002")
    updated_goals = goal_updater.update_goals(goals, [{"role": "user", "content": conversation}])
    
    write_goals_to_file(updated_goals)
    
    return updated_goals

@weave.op()
def write_goals_to_file(goals: str):
    with open(os.path.join("..", "data", "goals.txt"), "w") as f:
        f.write(goals)
