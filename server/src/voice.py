import requests
import os
from typing import List
from fastapi import APIRouter
import weave
from src.types import VapiEvent, VapiCallEndReport
from src.state import convo_history, save_convo
from src.memory import write_goals_to_file, update_goals_str, get_goals_str

default_first_msg = "Hello Sam. This is your Shoulder Angel."

router = APIRouter()


@weave.op()
def call_user(first_msg=default_first_msg, user_goal_m: str = "", recent_ocr: str = "", conversation_history: List[dict] = []):
    """Trigger a call thru Vapi to a user, with context"""
    # Your Vapi API Authorization token
    auth_token = os.environ["VAPI_AUTH_TOKEN"]
    phone_number_id = os.environ["VAPI_PHONE_NUMBER_ID"]
    # The Phone Number ID, and the Customer details for the call
    customer_number = os.environ["TEST_NUMBER"]
    llm_model = "llama3-70b-8192"

    # Create the header with Authorization token
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }

    # Create the data payload for the API request
    data = {
        "assistant": {
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
                    *conversation_history[-45:],
                    {
                        "role": "system",
                        "content": f"The user's current goals are: {user_goal_m}",
                    },
                ],
                "toolIds": [
                    "84d7620b-83ef-4e75-a42f-9f22c3a407a7",  # add_new_memory
                    # "e7f0b7c1-fb3a-43f1-a4e1-dca78e3d0675",  # fetch_memories
                ],
            },
            "voice": "jennifer-playht",
            "serverUrl": f'{os.environ["BACKEND_URL"]}/handle_vapi',
        },
        "phoneNumberId": phone_number_id,
        "customer": {
            "number": customer_number,
        },
    }

    res = requests.post(
        os.environ["VAPI_ENDPOINT"],
        headers=headers,
        json=data,
    )
    if res.content:
        print(f"error content: {res.content}")

    return res


@router.post("/handle_vapi")
@weave.op()
def handle_vapi(event: dict):
    """Handle events from Vapi"""

    print(f"is vapi event: {isinstance(event, VapiEvent)}")

    # Print the incoming event
    print("Received Vapi event:")
    # print(event)
    print(event["message"])
    print(event["message"]["type"])

    # print(event["message"])
    # print(event["message"]["type"])

    if (event["message"]["type"] == "end-of-call-report"):
        print("Received end-of-call report")
        # try:
            # report = VapiCallEndReport(**event["message"])
            # print(f"Successfully parsed report: {report}")
        # except Exception as e:
        #     print(f"Error parsing VapiCallEndReport: {e}")
        #     return {"result": "error"}

        # Append resulting messages to the convo history
        convo_history.extend(event["message"]["messages"])
        save_convo()

        # Update user goals
        transcript = event["message"]["transcript"]
        updated_goals = update_goals_str(get_goals_str(), transcript)
        write_goals_to_file(updated_goals)

        return {"result": "success"}

    # if isinstance(event, VapiEvent) and event.message and event.message.type == "end-of-call-report":
    #     print("It's a call end report!")
    #     try:
    #         report = VapiCallEndReport(**event.message.dict())
    #     except Exception as e:
    #         print(f"Error parsing VapiCallEndReport: {e}")
    #         return {"result": "error"}

    #     # Append resulting messages to the convo history
    #     convo_history.extend(report.messages)
    #     save_convo()

    #     # Update user goals

    #     transcript = report.transcript
    #     updated_goals = update_goals_str(get_goals_str(), transcript)
    #     write_goals_to_file(updated_goals)

    #     return {"result": "success"}
    else:
        return {"result": "Not a call end report"}
