from openai import OpenAI

client = OpenAI()

def _generate_ai_response(system_prompt: str, user_prompt: str, model: str = "gpt-3.5-turbo") -> str:
    """
    Helper function to generate AI responses with OpenAI chat API.
    """
    if not user_prompt.strip():
        return "No content provided."

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI generation failed: {str(e)}"


# Example specialized functions
def generate_lesson(prompt: str) -> str:
    system_prompt = "You are a helpful assistant that generates educational content."
    return _generate_ai_response(system_prompt, f"Generate a lesson based on the following prompt: {prompt}")

def generate_quiz(lesson_content: str) -> str:
    system_prompt = "You are a helpful assistant that generates quizzes based on lesson content."
    return _generate_ai_response(system_prompt, f"Generate a quiz based on the following lesson content: {lesson_content}")

def generate_explanation(question: str) -> str:
    system_prompt = "You are a helpful assistant that provides explanations for quiz questions."
    return _generate_ai_response(system_prompt, f"Provide an explanation for the following question: {question}")

def generate_hint(question: str) -> str:
    system_prompt = "You are a helpful assistant that provides hints for quiz questions."
    return _generate_ai_response(system_prompt, f"Provide a hint for the following question: {question}")

def generate_summary(lesson_content: str) -> str:
    system_prompt = "You are a helpful assistant that generates summaries for lesson content."
    return _generate_ai_response(system_prompt, f"Generate a summary for the following lesson content: {lesson_content}")

# You can similarly refactor all other functions (practice problems, flashcards, etc.)
# For voice explanation, you can just return text here and call generate_voice() elsewhere
def generate_voice_explanation(question: str) -> str:
    system_prompt = "You are a helpful assistant that provides explanations for quiz questions."
    return _generate_ai_response(system_prompt, f"Provide a voice-friendly explanation for the following question: {question}")