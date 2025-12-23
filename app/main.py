from fastapi import FastAPI
from app.api.interview import router as interview_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Interview Practice Bot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js 개발 서버
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(interview_router, prefix='/interview')

@app.get('/')
def root():
  return {"status": "ok"}