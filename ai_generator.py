import requests
import json

# Prompt templates
PROMPT_TEMPLATES = {
    "study_guide": """You're a helpful tutor. Given the topic text below, generate a clear and concise study guide with bullet points, definitions, and key ideas.

Topic Text:
\"\"\"{text}\"\"\"

Study Guide:
""",
    "flashcards": """You're an AI assistant that makes educational flashcards. From the following text, create a list of flashcards in the format: Q: ... A: ...

Topic Text:
\"\"\"{text}\"\"\"

Flashcards:
""",
    "practice_questions": """You're an exam coach. Based on the topic text below, write 3 practice questions (multiple choice or short answer) with answers.

Topic Text:
\"\"\"{text}\"\"\"

Practice Questions:
"""
}

def call_ollama(prompt, model="llama3:latest", temperature=0.7):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "temperature": temperature,
                "stream": False
            },
            headers={"Content-Type": "application/json"}
        )
        

        
        lines = response.text.strip().split("\n")
        full_response = ""
        for line in lines:
            try:
                data = json.loads(line)
                # Extracts the 'response' field from each JSON object
                full_response += data.get("response", "")
            except json.JSONDecodeError:
                print("⚠️ Warning: Skipping invalid JSON line.")
                continue

        

        return full_response.strip()

    except Exception as e:
        return f"❌ Error calling Ollama: {e}"

def generate_study_guide(text):
    return call_ollama(PROMPT_TEMPLATES["study_guide"].format(text=text))

def generate_flashcards(text):
    return call_ollama(PROMPT_TEMPLATES["flashcards"].format(text=text))

def generate_practice_questions(text):
    return call_ollama(PROMPT_TEMPLATES["practice_questions"].format(text=text))

if __name__ == "__main__":
    topic_text = input("📘 Paste cleaned topic text: ")

    print("\n📖 Study Guide:\n")
    print(generate_study_guide(topic_text))

    print("\n🧠 Flashcards:\n")
    print(generate_flashcards(topic_text))

    print("\n📝 Practice Questions:\n")
    print(generate_practice_questions(topic_text))
