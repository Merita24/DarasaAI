from fastapi import APIRouter
from pydantic import BaseModel, Field
from services.ai_service import generate_lesson

router = APIRouter()

# Input model
class LessonRequest(BaseModel):
    topic: str = Field(..., description="Lesson topic")
    grade: int = Field(..., description="Grade level of students")

@router.post("/lesson/start")
def start_lesson(data: LessonRequest):
    lesson = generate_lesson(data.topic, data.grade)
    return {"success": True, "topic": data.topic, "grade": data.grade, "lesson": lesson}

@router.post("/lesson/stop")
def stop_lesson():
    return {"success": True, "message": "Lesson stopped successfully."}