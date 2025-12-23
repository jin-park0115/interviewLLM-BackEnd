from fastapi import APIRouter
from app.schemas.interview import JobRequest, AnswerRequest, FeedbackResponse
from app.services.gemini import ask_gemini
import json
import re

router = APIRouter()

@router.post("/question")
def generate_question(req: JobRequest):
    prompt = f"""
너는 {req.job} 개발자 면접관이다. 신입 기준 질문을 하나 만들어줘.
조건:
1. 질문은 실무에 바로 관련 있는 내용이어야 함.
2. 질문 유형: 이론 또는 실습
3. 난이도 신입
4. 답변 예상 길이: 3~5문장
5. JSON 형태로만 응답
형식:
{{
  "question: "여기에 질문내용",
  "category: "이론/실습",
  "difficulty: "신입"
}}
"""
    try:
        question = ask_gemini(prompt)
        cleaned = re.sub(r"```json|```", "", question).strip()
        return json.loads(cleaned)
    except Exception as e:
        return {"error": str(e)}

@router.post("/answer", response_model=FeedbackResponse)
def analyze_answer(req: AnswerRequest):
    prompt = f"""
질문:
{req.question}

답변:
{req.answer}

아래 JSON 형식으로만 응답해라.

{{
  "scores": {{
    "concept": 0,
    "logic": 0,
    "practice": 0,
    "communication": 0
  }},
  "total": 0,
  "strengths": "",
  "weaknesses": "",
  "improvement": ""
}}
"""
    raw_result = ask_gemini(prompt)  # <- 들여쓰기 수정

    # Gemini가 ```json ... ``` 형태로 보내면 제거
    cleaned = re.sub(r"```json|```", "", raw_result).strip()

    try:
        parsed = json.loads(cleaned)
    except json.JSONDecodeError:
        # JSON 파싱 실패 시 디버그용
        return {
            "error": "Gemini 응답이 JSON이 아님",
            "raw": raw_result
        }

    return parsed
