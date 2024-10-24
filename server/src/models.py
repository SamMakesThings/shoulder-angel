from datetime import datetime
import os
import weave
import google.generativeai as genai
from typing import List, Dict
from .types import GroqMessage

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

class GeminiScheduler(weave.Model):
    model: str
    system_message: str

    @weave.op()
    def predict(self, user_sched: str, now_ts: str):
        model = genai.GenerativeModel(self.model)
        
        chat = model.start_chat(history=[
            {"role": "user", "parts": [self.system_message]},
            {"role": "model", "parts": ["Understood. I'll help check the user's schedule."]},
            {"role": "user", "parts": [f"My preferred schedule is {user_sched}"]},
            {"role": "user", "parts": [f"Current time is {now_ts}"]},
        ])
        
        response = chat.send_message("Return a single word `True` or `False`. Say 'True' if the current time is within the user's schedule. Say 'False' if it's outside the schedule.")
        return response.text

class GeminiOnTaskAnalyzer(weave.Model):
    model: str
    system_message: str

    @weave.op()
    def predict(
        self, user_goals: str, recent_ocr: str, recent_messages: List[GroqMessage] = []
    ):
        model = genai.GenerativeModel(self.model)

        print(f"recent_messages: {recent_messages}")
        
        history = [
            {"role": "user", "parts": [self.system_message]},
            {"role": "model", "parts": ["Understood. I'll analyze if the user is on task."]},
            {"role": "user", "parts": [f"The user's current goals are: {user_goals}"]},
            {"role": "user", "parts": ["The following messages are your most recent conversation with the user."]}
        ]
        
        for message in recent_messages:
            history.append({"role": "user", "parts": [f"{message["role"]}: {message["content"]}"]})
        
        history.append({"role": "user", "parts": [f"The user's screen last showed the following OCR'd text: {recent_ocr}"]})
        
        chat = model.start_chat(history=history)
        response = chat.send_message("Return a single word `True` or `False`. Return 'True' if the text on the screen seems to line up with the user's stated goals. If it doesn't line up with the user's stated goals, return 'False' with nothing else. Also return 'False' if there doesn't seem to be any OCR'd text.\n\nE.g. 'True' or 'False'. Don't explain anything.")
        return response.text

class GeminiTaskReminderFirstMsg(weave.Model):
    model: str
    system_message: str

    @weave.op()
    def predict(
        self, user_goals: str, recent_ocr: str, recent_messages: List[GroqMessage] = []
    ):
        model = genai.GenerativeModel(self.model)
        
        messages = [
            {"role": "user", "parts": [self.system_message]},
            {"role": "model", "parts": ["Understood. I'll generate a task reminder message."]},
            {"role": "user", "parts": [f"The user's current goals are: {user_goals}"]},
            {"role": "user", "parts": [f"The user's screen last showed the following OCR'd text: {recent_ocr}"]}
        ]
        
        for message in recent_messages:
            messages.append({"role": "user", "parts": [f"{message["role"]}: {message["content"]}"]})
        
        messages.append({"role": "user", "parts": ["Greet the user and ask them about their current activity, especially how it relates to their stated goals. Keep it within two sentences."]})

        chat = model.start_chat(history=messages)
        response = chat.send_message("Greet the user and ask them about their current activity, especially how it relates to their stated goals. Keep it within two sentences.")
        return response.text

class GeminiGoalUpdater(weave.Model):
    model: str
    system_message: str = "You are an assistant that updates user goals based on new information from conversations."

    @weave.op()
    def update_goals(self, current_goals: str, conversation_history: List[GroqMessage]):
        model = genai.GenerativeModel(self.model)
        
        messages = [
            {"role": "user", "parts": [self.system_message]},
            {"role": "model", "parts": ["Understood. I'll update the user's goals based on new information."]},
            {"role": "user", "parts": [f"Current goals: {current_goals}\n\nPlease update the goals based on any new information in the following conversation. Return only the updated goals as a concise string."]}
        ]
        
        for message in conversation_history:
            messages.append({"role": "user", "parts": [f"{message["role"]}: {message["content"]}"]})
        
        chat = model.start_chat(history=messages)
        response = chat.send_message("Please update the goals based on the conversation history provided.")

        # response = model.generate_content(messages)
        updated_goals = response.text.strip()
        return updated_goals
