from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from routes.lesson_routes import router as lesson_router
from routes.whatsapp_route import router as whatsapp_router

from services.ai_service import generate_explanation, generate_quiz
from services.voice_service import generate_voice

app=FastAPI(title="DarasaAI")

app.include_router(lesson_router)
app.include_router(whatsapp_router)

app.mount("/audio",StaticFiles(directory="audio"),name="audio")

@app.get("/")
def home():
    return {
        "message": "Welcome to DarasaAI",
        "description":"AI classroom assistant for low-resource schools",
        "docs": "/docs"
    }

#OFFLINE USSD CLI INTERFACE

'''def start_cli():
    print("Welcome to DarasaAI USSD CLI Interface!")

    while True:
        print("\nPlease select an option:")
        print("1. Generate Explanation")
        print("2. Generate Quiz")
        print("3. Generate Voice Explanation")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            question = input("Enter the question you want explained: ").strip()
            if not question:
                print("Question cannot be empty.")
                continue
            try:
                explanation = generate_explanation(question)
                print(f"Explanation:\n{explanation}")
            except Exception as e:
                print(f"Failed: {e}")

        elif choice == "2":
            lesson_content = input("Enter the lesson content for quiz generation: ").strip()
            if not lesson_content:
                print("Lesson content cannot be empty.")
                continue
            try:
                quiz = generate_quiz(lesson_content)
                print(f"Quiz:\n{quiz}")
            except Exception as e:
                print(f"Failed: {e}")

        elif choice == "3":
            text = input("Enter the text for voice explanation: ").strip()
            if not text:
                print("Text cannot be empty.")
                continue
            try:
                audio_path = generate_voice(text)
                if audio_path:
                    print(f"Voice explanation generated at: {audio_path}")
                else:
                    print("Failed to generate voice explanation.")
            except Exception as e:
                print(f"Failed: {e}")

        elif choice == "4":
            print("Exiting DarasaAI USSD CLI Interface. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            '''
