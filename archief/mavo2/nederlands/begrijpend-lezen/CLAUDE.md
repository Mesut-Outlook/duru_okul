# CLAUDE.md - Developer Guidelines & Commands

Welcome! This document provides essential guidelines and commands for developers and AI assistants working on the **Begrijpend Lezen Trainer** project.

## 🚀 Commands & Development Workflow

### 1. Running the Web Application
The application is a pure client-side frontend app (`index.html`, `style.css`, `app.js`, `questions.js`). Since modern browsers block local file loading via the `file://` protocol due to CORS, it should be run using our local network HTTP server:
```bash
# Start the customized network HTTP server
python3 server.py
```
Then visit: `http://localhost:8000` (or `http://<your-local-ip>:8000` from another device on the same LAN)

### 2. Generating a New Exam (Otonom / Automated)
You can automatically generate a brand new, curriculum-aligned exam (4 texts, 16 questions) on any topic using the **Google Antigravity (AGY) SDK**:
```bash
# Make sure your Gemini API Key is set in the environment
export GEMINI_API_KEY="your-api-key"

# Generate a new exam
python3 generate_exam_agy.py "[Onderwerp]"
# Example:
python3 generate_exam_agy.py "Klimaatverandering"
```

---

## 🛠️ Codebase Structure

- **`index.html`**: Main single-page application structure.
- **`app.js`**: Core app logic, UI rendering, game state, history logging, and the custom premium dialog overlay for generating exams.
- **`questions.js`**: Central database declaring the global `quizData` array containing all exams, plus `teacherQuotes` and `positiveCompliments`.
- **`generate_exam_agy.py`**: Automated Python script leveraging the **Google Antigravity (AGY) SDK** and Pydantic schemas to safely generate and append new exams.
- **`style.css`**: Styling sheets, variables for HSL colors (supporting dark mode), animations, layouts, and custom modal overlays.

---

## 📝 Design & Pedagogical Guidelines

This app acts as **"Meester Max"**, an encouraging, patient, and precise Dutch reading comprehension tutor for **2 Mavo / VMBO-T** level students.

### 1. Exam Structure (Strict Rule)
Every exam MUST have exactly:
- **4 Texts** (sequentially numbered inside the exam).
- **4 Questions per text** (totaling exactly **16 questions** per exam).
- Sequential globally unique IDs for questions (e.g., Exam 1 has Q1-16, Exam 11 has Q161-176, Exam 12 has Q177-192, etc.).

### 2. Spiekbriefje Rules & Question Design
Each of the 4 questions in a text must test a specific curriculum concept from **"Het Spiekbriefje"**:
1. **Onderwerp (Subject):** "Where the text is about, max. 4 words". The correct option MUST be exactly 4 words or less.
2. **Tekstdoel (Goal):** Evalueer of de tekst bedoeld is om te *Informeren*, *Overtuigen*, *Activeren*, of *Amuseren*.
3. **Tekstverband (Relationship):** Identify text relations using signal words (e.g., *echter* = tegenstelling, *bovendien* = opsomming, *dus* = gevolg, *daarna* = tijd).
4. **Citeren (Citing):** Letterlijk citeren met aanhalingstekens: **“...”** (double curly quotes). The correct answer must follow this format precisely.

### 3. Voice and Tone
All questions, options, and explanations must be written in **Dutch**.
- Explanations must be written in Meester Max's voice: highly encouraging, educational, explaining why the correct choice is right and referencing the **Spiekbriefje** directly.
