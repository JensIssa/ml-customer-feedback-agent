from typing import List, TypedDict, Literal
import json
import os

class Feedback(TypedDict):
    id: str
    text: str
    source: Literal["email", "chat", "survey"]


current_dir = os.path.dirname(os.path.abspath(__file__))
feedback_file = os.path.join(current_dir, "feedback.json")


def query_feedback() -> List[Feedback]:
    with open(feedback_file, 'r') as f:
        feedback_store: List[Feedback] = json.load(f)
    return feedback_store
