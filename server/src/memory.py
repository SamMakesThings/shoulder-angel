import os
from fastapi import APIRouter, HTTPException
import sqlite3
import weave

from src.models import GeminiGoalUpdater
from src.types import (
    VapiEvent,
    AddMemoryFunctionArgs,
    FetchMemoriesFunctionArgs,
)

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


# @router.post("/add_memory")
# @weave.op()
# async def add_memory(data: VapiEvent):
#     """Add a memory to the user's memory store"""

#     if not data.message["toolCalls"]:
#         raise HTTPException(
#             status_code=400, detail="No tool calls found in the request"
#         )

#     tool_call = data.message["toolCalls"][0]
#     if tool_call.function.name != "add_new_memory":
#         raise HTTPException(status_code=400, detail="Unexpected function name")

#     try:
#         function_args = AddMemoryFunctionArgs(**tool_call.function.arguments)
#     except ValueError:
#         raise HTTPException(status_code=400, detail="Invalid arguments structure")

#     # m.add(
#     #     function_args.content,
#     #     user_id="samstowers",
#     #     metadata={"category": function_args.category},
#     # )

#     return {"status": "success", "message": "Memory added successfully"}


# @router.post("/fetch_memories")
# @weave.op()
# async def fetch_memories(data: VapiEvent):
#     """Fetch recent memories from the user's memory store"""

#     if not data.message["toolCalls"]:
#         raise HTTPException(
#             status_code=400, detail="No tool calls found in the request"
#         )

#     tool_call = data.message["toolCalls"][0]
#     if tool_call.function.name != "fetch_recent_memories":
#         raise HTTPException(status_code=400, detail="Unexpected function name")

#     try:
#         function_args = FetchMemoriesFunctionArgs(**tool_call.function.arguments)
#     except ValueError:
#         raise HTTPException(status_code=400, detail="Invalid arguments structure")

#     # recent_memories = m.search(
#     #     function_args.content,
#     #     user_id="samstowers",
#     #     # limit=function_args.limit if hasattr(function_args, "limit") else 5,
#     #     limit=5,
#     #     # metadata=(
#     #     #     {"category": function_args.category}
#     #     #     if hasattr(function_args, "category")
#     #     #     else None
#     #     # ),
#     # )

#     return {"result": "Not implemented"}

    # return {"result": "Relevant memories: " + str(recent_memories)}
