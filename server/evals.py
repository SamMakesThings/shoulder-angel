import weave 
import asyncio
import dotenv

dotenv.load_dotenv()

from src.evals_dataset import task_analyzer_dataset
from src.models import GeminiOnTaskAnalyzer

weave.init("shoulder-angel")

on_task_analyzer = GeminiOnTaskAnalyzer(
    model="gemini-1.5-flash-8b",
    system_message="Your role is to analyze the user's OCR output and determine if it's relevant to their stated goals (infer this from recent conversation). Return the single word 'True' if it is otherwise return 'False', with nothing else. Use recent messages to understand a user's goals, but only use the OCR for current activity.",
)


@weave.op()
def is_on_task_judge(target_output: str, model_output: str) -> bool:
    return str(model_output).strip() == str(target_output).strip()

evaluation = weave.Evaluation(
    name='general_evals',  
    dataset=task_analyzer_dataset,
    scorers=[is_on_task_judge]
)

print(asyncio.run(evaluation.evaluate(on_task_analyzer)))
