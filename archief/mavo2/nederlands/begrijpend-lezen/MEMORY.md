# MEMORY.md - Project History, Decisions & Memory Log

This document serves as the project's memory log, preserving all design choices, architectural refactorings, and the history of modifications made to the **Begrijpend Lezen Trainer** project.

---

## 📅 Project Evolution & Milestones

### Milestone 1: Structuring & Expanding the Dataset (10 Exams)
* **Initial State:** The project had a flat, loosely structured list of reading comprehension texts.
* **Refactoring:** We restructured the data inside `questions.js` into exactly **10 distinct exams**. Each exam has exactly **4 texts**, and each text has exactly **4 questions** (total of 16 questions per exam, 160 questions in total).
* **Game Loop Update:** Refactored `app.js` state variables (`currentExamIndex` and `activeTexts`) so that the game loop dynamically runs the chosen exam over 4 rounds.
* **Start Screen & History Overhaul:** The starting screen was rewritten to show 10 interactive exam cards. The local storage history tracker was updated to store results by their specific exam title (e.g., *Sınav 1: Digitale Wereld*).

### Milestone 2: The "Create New Exam" UI Enabler
* **User Requirement:** Add a way to easily generate new exams directly from the UI without touching the code.
* **Solution:**
  1. Added a dashed, styled **"Yeni Sınav Yarat 🪄"** button to both the Start Screen and the Final Results screen.
  2. Created a beautiful backdrop-filtered glassmorphism **Modal Dialog Overlay** in HTML/CSS/JS.
  3. When clicked, it asks for an exam topic, generates a standard kopyalanabilir prompt, and copies it to the user's clipboard for pasting into the chat with the assistant.

### Milestone 3: Google Antigravity (AGY) SDK Otonom Integration
* **Implementation:**
  1. Created `generate_exam_agy.py`, an autonomous Python script powered by the **Google Antigravity SDK**.
  2. The script defines a custom agent configured with a Pydantic schema (`Exam`, `Text`, `Question`, `Option`) and system instructions to roleplay as **Meester Max**.
  3. When run via `python3 generate_exam_agy.py "[Onderwerp]"`, it queries the Gemini API for structured JSON matching the schema, automatically maps IDs sequentially, formats it as JavaScript, and appends it cleanly to `questions.js`.
  4. Verified syntax correctness using a bracket-checker utility to ensure zero syntax errors.

### Milestone 4: Newly Generated Exams
* **Sınav 11 (Klimaatverandering):** First automatically generated exam using the `exam_generator` subagent. Covers global warming, solar energy, meat consumption, and Lars the polar bear. Questions 161 to 176.
* **Sınav 12 (Eten & Wereldkeuken):** Generated via user trigger. Covers the history of sushi, local restaurants vs fast food, Italian cooking workshop, and Daan's spicy burrito. Questions 177 to 192.

### Milestone 5: Custom LAN Web Server Enabler
* **Implementation:**
  1. Created `server.py`, a custom HTTP server binding to all network interfaces (`0.0.0.0`) to make the app accessible from any device on the local network (LAN).
  2. Implemented dynamic IP detection inside the Python server using dummy UDP socket routing to detect the active network interface.
  3. Enabled `allow_reuse_address = True` on the TCPServer to prevent port binding blockages during consecutive restarts.
  4. Updated documentation inside `CLAUDE.md` to establish the new `python3 server.py` execution workflow.

---

## 🛠️ Architecture Details

### Schema Specification
All exams in `questions.js` follow this schema representation:
```json
{
  "examId": 12,
  "examTitle": "Sınav 12: Eten & Wereldkeuken",
  "texts": [
    {
      "title": "Tekst 45: De geheimen van sushi",
      "goal": "Informeren",
      "text": "...",
      "questions": [
        {
          "id": 177,
          "question": "...",
          "options": [
            { "key": "A", "text": "..." }
          ],
          "correct": "C",
          "explanation": "..."
        }
      ]
    }
  ]
}
```

### The Spiekbriefje Pedagogy
Every generated question adheres strictly to the following Dutch 2 Mavo curriculum principles:
- **Onderwerp (Subject):** Max 4 words. E.g., *"Opwarming van de aarde"*.
- **Tekstdoel (Goal):** Informeren (facts), Overtuigen (opinion + arguments), Activeren (call to action), Amuseren (story).
- **Tekstverband (Relationship):** Tests understanding of signal words: *Ten eerste* (opsomming), *Echter* (tegenstelling), *Omdat* (reden/oorzaak), *Dus* (gevolg), *Daarna* (tijd).
- **Citeren (Citing):** Letterlijk citeren met aanhalingstekens: **“...”**.
- **Meester Max Explanations:** Encouraging, explanatory, and always refers the student back to the Spiekbriefje rules.
