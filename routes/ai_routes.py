from fastapi import APIRouter, Body
from services.ai_service import (
    generate_lesson,
    generate_quiz,
    generate_explanation,
    generate_hint,
    generate_summary,
    generate_practice_problems,
    generate_interactive_exercise,
    generate_flashcards,
    generate_discussion_questions,
    generate_case_study,
    generate_real_world_application,
    generate_project_idea,
    generate_voice_explanation
)
from services.voice_service import generate_voice

router = APIRouter()

SERVICE_MAP = {
    "lesson": generate_lesson,
    "quiz": generate_quiz,
    "explanation": generate_explanation,
    "hint": generate_hint,
    "summary": generate_summary,
    "practice": generate_practice_problems,
    "interactive": generate_interactive_exercise,
    "flashcards": generate_flashcards,
    "discussion": generate_discussion_questions,
    "case_study": generate_case_study,
    "real_world": generate_real_world_application,
    "project": generate_project_idea,
    "voice": generate_voice_explanation
}

@router.post("/generate")
def generate_content(
    type: str = Body(..., embed=True, description="Type of content to generate, e.g., lesson, quiz, explanation, voice"),
    content: str = Body(..., embed=True, description="Topic or question content")
):
    
    if not content.strip():
        return {"success": False, "error": "Content cannot be empty"}

    
    if type not in SERVICE_MAP:
        return {"success": False, "error": f"Invalid type. Available types: {list(SERVICE_MAP.keys())}"}

    try:
        result = SERVICE_MAP[type](content)
    except Exception as e:
        return {"success": False, "error": f"Generation failed: {str(e)}"}

    
    if type == "voice":
        try:
            audio_file = generate_voice(result)
        except Exception:
            audio_file = None
        return {"success": True, "type": type, "text": result, "audio_file": audio_file}

    return {"success": True, "type": type, "data": result}