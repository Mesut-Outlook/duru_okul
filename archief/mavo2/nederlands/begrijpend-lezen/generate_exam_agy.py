#!/usr/bin/env python3
import sys
import os
import re
import json
import asyncio
import pydantic

# 1. Define the target schema using Pydantic for structured generation
class Option(pydantic.BaseModel):
    key: str  # "A", "B", "C", "D"
    text: str

class Question(pydantic.BaseModel):
    id: int
    question: str
    options: list[Option]
    correct: str  # "A", "B", "C", "D"
    explanation: str

class Text(pydantic.BaseModel):
    title: str
    goal: str  # "Informeren", "Overtuigen", "Activeren", "Amuseren"
    text: str
    questions: list[Question]

class Exam(pydantic.BaseModel):
    examTitle: str
    texts: list[Text]

# 2. Asynchronous generation function using Google Antigravity SDK
async def run_generation(topic, next_exam_id, next_q_id):
    from google.antigravity import Agent, LocalAgentConfig
    
    system_instructions = (
        "Je bent Meester Max, een uiterst deskundige, bemoedigende en geduldige docent "
        "Begrijpend Lezen voor 2 Mavo. Je taak is om een nieuw, hoogwaardig examen te "
        "genereren over het opgegeven onderwerp.\n\n"
        "RICHTLIJNEN:\n"
        "- Genereer exact 4 teksten, met elk exact 4 vragen (totaal 16 vragen).\n"
        "- Elk van de 4 teksten heeft een specifiek tekstdoel: Informeren, Overtuigen, Activeren, Amuseren.\n"
        "- De teksten moeten rijke, boeiende verhalen of informatieve passages zijn van 100-150 woorden.\n"
        "- Zorg ervoor dat de teksten overduidelijke signaalwoorden bevatten zoals 'ten eerste', 'bovendien', 'echter', 'hoewel', 'omdat', 'dus', 'daardoor', 'daarom'.\n"
        "- De 4 vragen per tekst moeten exact de volgende structuur hebben:\n"
        "  1. Onderwerp-vraag: Het juiste antwoord MOET in maximaal 4 woorden zijn (volgens de regel van het Spiekbriefje)!\n"
        "  2. Tekstdoel-vraag: Evalueer het tekstdoel.\n"
        "  3. Tekstverband & Signaalwoord-vraag.\n"
        "  4. Citeervraag: Letterlijk citeren met aanhalingstekens: “...”\n"
        "- De feedback/uitleg per vraag moet in het Nederlands zijn, uiterst bemoedigend en expliciet "
        "verwijzend naar het Spiekbriefje."
    )
    
    # Configure the AGY SDK agent
    config = LocalAgentConfig(
        system_instructions=system_instructions,
        response_schema=Exam,
    )
    
    prompt = (
        f"Genereer een nieuw examen over het onderwerp: \"{topic}\".\n"
        f"Belangrijke technische vereisten:\n"
        f"- Start de vraag ID's exact bij {next_q_id} en nummer ze opeenvolgend door tot {next_q_id + 15}.\n"
        f"- De titel van het examen moet zijn: \"Sınav {next_exam_id}: [Onderwerp]\".\n"
        f"- De 4 teksten moeten de titels \"Tekst {next_exam_id*4 - 3}\", \"Tekst {next_exam_id*4 - 2}\", "
        f"\"Tekst {next_exam_id*4 - 1}\" en \"Tekst {next_exam_id*4}\" krijgen."
    )
    
    print("Verbinding maken met de Meester Max AI via de Google Antigravity SDK...")
    async with Agent(config=config) as agent:
        response = await agent.chat(prompt)
        print("Examen wordt gegenereerd...")
        exam_data = await response.structured_output()
        return exam_data

# 3. Main execution flow
def main():
    if len(sys.argv) < 2:
        print("Gebruik: python3 generate_exam_agy.py \"[Onderwerp]\"")
        sys.exit(1)
        
    topic = sys.argv[1]
    js_file = 'questions.js'
    
    if not os.path.exists(js_file):
        print(f"Fout: {js_file} niet gevonden!")
        sys.exit(1)
        
    # Read questions.js
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Determine the next Exam ID and Question ID using regex
    exam_ids = [int(x) for x in re.findall(r'examId:\s*(\d+)', content)]
    next_exam_id = max(exam_ids) + 1 if exam_ids else 1
    
    q_ids = [int(x) for x in re.findall(r'id:\s*(\d+)', content)]
    next_q_id = max(q_ids) + 1 if q_ids else 1
    
    print(f"Gedetecteerd: Enkele examens in database.")
    print(f"Volgende Examen ID: {next_exam_id}")
    print(f"Volgende Sınav Soru Başlangıç ID: {next_q_id} (tussen {next_q_id} ve {next_q_id + 15})")
    
    # Run the async generation
    try:
        exam_dict = asyncio.run(run_generation(topic, next_exam_id, next_q_id))
    except Exception as e:
        print(f"\nFout tijdens de AI-generatie: {e}")
        print("Zorg ervoor dat de GEMINI_API_KEY omgevingsvariabele correct is ingesteld.")
        print("U kunt uw API-sleutel ophalen via: https://aistudio.google.com/app/api-keys")
        sys.exit(1)
        
    if not exam_dict:
        print("Fout: Kon geen gestructureerd examen genereren.")
        sys.exit(1)
        
    # Add examId to the parsed dictionary for questions.js structure
    exam_dict['examId'] = next_exam_id
    
    # Format as JSON/JS Object
    exam_js = json.dumps(exam_dict, indent=4, ensure_ascii=False)
    
    # Locate the end of the quizData array and insert the new exam
    target_string = "\n];\n\n// Motivatie-uitspraken van \"Meester Max\""
    if target_string not in content:
        print("Fout: Kon het einde van de quizData array in questions.js niet vinden.")
        sys.exit(1)
        
    replacement_string = ",\n" + exam_js + "\n];\n\n// Motivatie-uitspraken van \"Meester Max\""
    new_content = content.replace(target_string, replacement_string)
    
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"\n🎉 Succes! Sınav {next_exam_id} ({exam_dict['examTitle']}) is succesvol toegevoegd aan {js_file}!")
    print(f"Open de site (http://localhost:8000) en ververs om te spelen!")

if __name__ == '__main__':
    main()
