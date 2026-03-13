from fastapi import APIRouter,Form
from services.ai_service import generate_explanation, generate_quiz

router = APIRouter()

def detect_intent(message: str):
    """Detects the type of WhatsApp message."""
    message = message.strip().lower()
    if message.startswith("explain"):
        return "explain", message.replace("explain", "", 1).strip()
    if message.startswith("quiz"):
        return "quiz", message.replace("quiz", "", 1).strip()
    return "unknown", message

@router.post("/whatsapp/webhook")
def whatsapp_webhook(Body: str = Form(...)):
    intent, content = detect_intent(Body)

    if intent == "explain":
        try:
            response = generate_explanation(content)
        except Exception as e:
            response = f"Sorry, I couldn't generate an explanation: {str(e)}"
    
    elif intent == "quiz":
        try:
            response = generate_quiz(content)
        except Exception as e:
            response = f"Sorry, I couldn't generate a quiz: {str(e)}"
    
    else:
        response = (
            "You can ask me to explain a concept by starting your message with 'explain' "
            "or request a quiz by starting with 'quiz'."
        )
    
    return {"response": response}