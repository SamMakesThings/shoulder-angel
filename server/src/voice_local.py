from vapi_python import Vapi
import os
from typing import List
from fastapi import APIRouter
import weave
from src.types import VapiEvent, VapiCallEndReport
from src.state import convo_history, save_convo, get_convo_history_as_vapi

default_first_msg = "Hello Sam. This is your Shoulder Angel."

router = APIRouter()

# Initialize Vapi client
vapi = Vapi(api_key=os.environ["VAPI_PUBLIC_API_KEY"])

@weave.op()
def call_user(first_msg=default_first_msg, user_goal_m: str = "", recent_ocr: str = ""):
    """Trigger a call thru Vapi to a user, with context"""
    llm_model = "llama3-70b-8192"

    assistant = {
        "firstMessage": first_msg,
        "model": {
            "provider": "groq",
            "model": llm_model,
            "messages": [
                {
                    "role": "system",
                    "content": """Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are.""",
                },
                {
                    "role": "system",
                    "content": f"Here is the most recent OCR of the user's screen: {recent_ocr}",
                },
                *get_convo_history_as_vapi()[-45:],
            ],
            "toolIds": [
                "84d7620b-83ef-4e75-a42f-9f22c3a407a7",  # add_new_memory
                # "e7f0b7c1-fb3a-43f1-a4e1-dca78e3d0675",  # fetch_memories
            ],
        },
        "voice": "jennifer-playht",
        "serverUrl": f'{os.environ["BACKEND_URL"]}/handle_vapi',
    }

    # assistant_overrides = {
    #     "phoneNumberId": os.environ["VAPI_PHONE_NUMBER_ID"],
    #     "customer": {
    #         "number": os.environ["TEST_NUMBER"],
    #     },
    # }

    print("Starting Vapi call...")
    res = vapi.start(assistant=assistant)
    return res


@weave.op()
@router.post("/handle_vapi")
def handle_vapi(event: VapiEvent):
    """Handle events from Vapi"""
    if isinstance(event, VapiEvent) and event.message["type"] == "end-of-call-report":

        # Append resulting messages to the convo history
        print("it's a call end report!")
        try:
            report = VapiCallEndReport(**event.message)
        except Exception as e:
            print(f"Error parsing VapiCallEndReport: {e}")
            # return {"result": "error"}
        convo_history.extend(event.message["messages"])
        # Save convo history to pickled file
        save_convo()

        return {"result": "success"}
    else:
        return {"result": "Not a call end report"}
