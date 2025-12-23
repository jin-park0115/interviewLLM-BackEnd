from pydantic import BaseModel

class JobRequest(BaseModel):
    job: str

class AnswerRequest(BaseModel):
    question: str
    answer: str

class Score(BaseModel):
    concept: int
    logic: int
    practice: int
    communication: int

class FeedbackResponse(BaseModel):
    scores: Score
    total: int
    strengths: str
    weaknesses: str
    improvement: str
