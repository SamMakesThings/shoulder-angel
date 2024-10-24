Shoulder Angel!

Deploy server/main.py.

## Getting started

- Ensure you have Vapi, Google AI Studio, and WandB Weave accounts set up.
- Fill out .env file.
- Create your virtual environment with uv. `uv venv` and `source venv/bin/activate`
- Start screenpipe.
- If doing local calls: Make sure `portaudio` is installed. `brew install portaudio` if on MacOS.
- Run Ngrok. This is used to handle events from Vapi. E.g. `ngrok http 80`
- Run the server. `cd server && uvicorn src.main:app --reload`
- NOTE: When you run the server, you'll be prompted to provide your Weave API key. Just click the link and follow the instructions.
- Run the client. `cd client && python main.py`