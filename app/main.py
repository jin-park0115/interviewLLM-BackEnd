from fastapi import FastAPI
from app.api.interview import router as interview_router

app = FastAPI(title="Interview Practice Bot")

app.include_router(interview_router, prefix='/interview')

@app.get('/')
def root():
  return {"status": "ok"}