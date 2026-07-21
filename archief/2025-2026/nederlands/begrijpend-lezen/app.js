// Begrijpend Lezen App Logic - 2 Mavo Level
// Acts as Meester Max - motivating, patient, and precise.

document.addEventListener("DOMContentLoaded", () => {
  // App State variables
  let currentRound = 0; // 0 to 3 (4 rounds per exam)
  let startingRound = 0; // where the user started this session
  let answersChosen = {}; // e.g. { q1: 'A', q2: 'C', ... }
  let roundScores = []; // scores per round (array of numbers)
  let totalScore = 0;
  let isDarkMode = false;
  let appState = "START"; // START, QUIZ, FEEDBACK, FINAL
  let audioContext = null;
  let currentExamIndex = 0; // 0 to 9
  let activeTexts = []; // active texts in the selected exam

  // DOM Elements
  const themeToggle = document.getElementById("theme-toggle");
  const spiekToggle = document.getElementById("spiek-toggle");
  const sidebar = document.getElementById("sidebar");
  const mainContent = document.getElementById("main-content");
  const progressContainer = document.getElementById("progress-container");
  const progressBarFill = document.getElementById("progress-fill");
  const currentRoundName = document.getElementById("current-round-name");
  const totalScoreBadge = document.getElementById("total-score-badge");
  const teacherAvatar = document.getElementById("teacher-avatar");
  const teacherSpeechText = document.getElementById("teacher-speech-text");
  const floatMotiveBtn = document.getElementById("float-motivation");

  // Web Audio Synthesizer (Zero asset dependency sound effects)
  const initAudio = () => {
    if (!audioContext) {
      audioContext = new (window.AudioContext || window.webkitAudioContext)();
    }
  };

  const playSound = (type) => {
    try {
      initAudio();
      if (!audioContext) return;

      const osc = audioContext.createOscillator();
      const gain = audioContext.createGain();
      osc.connect(gain);
      gain.connect(audioContext.destination);

      const now = audioContext.currentTime;

      if (type === "correct") {
        // High-pitched pleasant double chime (C5 then G5)
        osc.type = "sine";
        osc.frequency.setValueAtTime(523.25, now); // C5
        osc.frequency.setValueAtTime(783.99, now + 0.08); // G5
        gain.gain.setValueAtTime(0.15, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
        osc.start(now);
        osc.stop(now + 0.35);
      } else if (type === "incorrect") {
        // Low warm downward tone
        osc.type = "triangle";
        osc.frequency.setValueAtTime(220, now); // A3
        osc.frequency.exponentialRampToValueAtTime(110, now + 0.25); // A2
        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.25);
        osc.start(now);
        osc.stop(now + 0.25);
      } else if (type === "complete") {
        // Ascending major chord sweep (C4 - E4 - G4 - C5)
        const notes = [261.63, 329.63, 392.00, 523.25];
        notes.forEach((freq, idx) => {
          const noteOsc = audioContext.createOscillator();
          const noteGain = audioContext.createGain();
          noteOsc.connect(noteGain);
          noteGain.connect(audioContext.destination);
          
          noteOsc.type = "sine";
          noteOsc.frequency.setValueAtTime(freq, now + idx * 0.1);
          noteGain.gain.setValueAtTime(0.12, now + idx * 0.1);
          noteGain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.1 + 0.4);
          noteOsc.start(now + idx * 0.1);
          noteOsc.stop(now + idx * 0.1 + 0.4);
        });
      }
    } catch (e) {
      console.warn("Audio Context could not start:", e);
    }
  };

  // Light / Dark Mode Toggle Handler
  themeToggle.addEventListener("click", () => {
    isDarkMode = !isDarkMode;
    document.documentElement.setAttribute("data-theme", isDarkMode ? "dark" : "light");
    themeToggle.textContent = isDarkMode ? "☀️" : "🌙";
    localStorage.setItem("theme", isDarkMode ? "dark" : "light");
  });

  // Check saved theme
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark") {
    isDarkMode = true;
    document.documentElement.setAttribute("data-theme", "dark");
    themeToggle.textContent = "☀️";
  }

  // Sidebar Toggling for mobile responsiveness
  spiekToggle.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    spiekToggle.style.backgroundColor = sidebar.classList.contains("open") 
      ? "var(--color-primary-light)" 
      : "var(--bg-sidebar)";
  });

  // Floating motivation quotes button
  floatMotiveBtn.addEventListener("click", () => {
    const randomQuote = teacherQuotes[Math.floor(Math.random() * teacherQuotes.length)];
    updateTeacherSpeech(randomQuote, "😊");
    
    // Quick button tap micro-animation
    floatMotiveBtn.style.transform = "scale(0.9) rotate(-10deg)";
    setTimeout(() => { floatMotiveBtn.style.transform = ""; }, 150);
  });

  // Update teacher speech widget
  const updateTeacherSpeech = (text, emoji = "👨‍🏫") => {
    teacherAvatar.textContent = emoji;
    teacherSpeechText.innerHTML = text;
  };

  // Update Timeline dots and main progress bar
  const updateProgressBar = () => {
    const totalQuestions = activeTexts.length * 4;
    const answeredCount = roundScores.reduce((acc, curr) => acc + curr, 0); // correct answers total
    
    // Fill based on current round
    const percentage = (currentRound / activeTexts.length) * 100;
    progressBarFill.style.width = `${percentage}%`;
    
    currentRoundName.textContent = `Tekst ${Math.min(currentRound + 1, activeTexts.length)} van ${activeTexts.length}`;
    totalScoreBadge.textContent = `Score: ${totalScore} / ${(currentRound - startingRound) * 4}`;

    // Update node states
    for (let i = 0; i < activeTexts.length; i++) {
      const nodeTitle = document.getElementById(`node-title-${i}`);
      if (nodeTitle) {
        if (i === currentRound && appState !== "FINAL") {
          nodeTitle.classList.add("active");
        } else {
          nodeTitle.classList.remove("active");
        }
      }
    }
  };

  // Start the Quiz Session
  const startQuiz = (startFromRound = 0) => {
    initAudio();
    appState = "QUIZ";
    activeTexts = quizData[currentExamIndex].texts;
    currentRound = startFromRound;
    startingRound = startFromRound;
    roundScores = [];
    totalScore = 0;
    answersChosen = {};
    
    // Show progress bar
    progressContainer.style.display = "flex";
    
    // Initialize Timeline Dots
    initTimelineDots();
    updateProgressBar();
    
    renderCurrentRound();
    updateTeacherSpeech(`Veel succes met Tekst ${currentRound + 1}! Lees de tekst rustig door en check altijd even je Spiekbriefje als je twijfelt. Zet 'm op! 💪`, "🚀");
  };

  // Generate blank timeline dots
  const initTimelineDots = () => {
    const progressNodes = document.querySelector(".progress-nodes");
    if (progressNodes) {
      progressNodes.innerHTML = "";
      for (let i = 0; i < activeTexts.length; i++) {
        const nodeGroup = document.createElement("div");
        nodeGroup.className = "progress-node-group";
        if (i < startingRound) {
          nodeGroup.classList.add("skipped");
        }
        
        const nodeTitle = document.createElement("span");
        nodeTitle.className = "node-title";
        if (i === currentRound) nodeTitle.classList.add("active");
        nodeTitle.id = `node-title-${i}`;
        nodeTitle.textContent = `Tekst ${i + 1}`;
        
        const dotsContainer = document.createElement("div");
        dotsContainer.className = "node-dots";
        dotsContainer.id = `node-dots-${i}`;
        
        for (let q = 0; q < 4; q++) {
          const dot = document.createElement("div");
          dot.className = "node-dot";
          if (i < startingRound) {
            dot.classList.add("skipped");
          }
          dot.id = `dot-${i}-${q}`;
          dotsContainer.appendChild(dot);
        }
        
        nodeGroup.appendChild(nodeTitle);
        nodeGroup.appendChild(dotsContainer);
        progressNodes.appendChild(nodeGroup);
      }
    }
  };

  // Highlight dot currently being solved
  const highlightCurrentDots = () => {
    if (appState !== "QUIZ") return;
    for (let q = 0; q < 4; q++) {
      const dot = document.getElementById(`dot-${currentRound}-${q}`);
      if (dot && !dot.classList.contains("correct") && !dot.classList.contains("incorrect")) {
        dot.className = "node-dot current";
      }
    }
  };

  // Render the current text and its 4 questions
  const renderCurrentRound = () => {
    const roundData = activeTexts[currentRound];
    answersChosen = {}; // clear round choices

    const quizGrid = document.createElement("div");
    quizGrid.className = "quiz-grid";

    // Column 1: Reading Text
    const leftCol = document.createElement("div");
    leftCol.className = "reading-card";
    leftCol.innerHTML = `
      <div class="badge-container">
        <span class="badge badge-primary">Ronde ${currentRound + 1}</span>
        <span class="badge badge-warning">Doel: ${roundData.goal}</span>
      </div>
      <h2>${roundData.title}</h2>
      <div class="reading-text">${roundData.text}</div>
    `;

    // Column 2: Questions Cards
    const rightCol = document.createElement("div");
    rightCol.className = "questions-card";

    roundData.questions.forEach((q, index) => {
      const qBlock = document.createElement("div");
      qBlock.className = "question-block";
      qBlock.id = `q-block-${index}`;
      qBlock.innerHTML = `
        <div class="question-number">Vraag ${q.id}</div>
        <div class="question-title">${q.question}</div>
        <div class="options-list">
          ${q.options.map(opt => `
            <label class="option-label" for="opt-${q.id}-${opt.key}">
              <input type="radio" name="q-${q.id}" id="opt-${q.id}-${opt.key}" class="option-input" value="${opt.key}">
              <div class="option-circle">${opt.key}</div>
              <div>${opt.text}</div>
            </label>
          `).join("")}
        </div>
      `;
      rightCol.appendChild(qBlock);
    });

    // Add listeners to option-labels to update custom visual styles dynamically
    rightCol.querySelectorAll(".option-input").forEach(input => {
      input.addEventListener("change", (e) => {
        const qId = e.target.name.replace("q-", "");
        answersChosen[qId] = e.target.value;
      });
    });

    // Submit button container
    const actionContainer = document.createElement("div");
    actionContainer.className = "action-bar";
    const submitBtn = document.createElement("button");
    submitBtn.className = "btn-primary";
    submitBtn.innerHTML = `Controleer antwoorden <span style="font-size: 1.1rem">✔️</span>`;
    submitBtn.addEventListener("click", evaluateRound);
    
    actionContainer.appendChild(submitBtn);
    rightCol.appendChild(actionContainer);

    quizGrid.appendChild(leftCol);
    quizGrid.appendChild(rightCol);

    mainContent.innerHTML = "";
    mainContent.appendChild(quizGrid);

    highlightCurrentDots();
  };

  // Evaluate current round answers
  const evaluateRound = () => {
    const roundData = activeTexts[currentRound];
    
    // Check if all 4 questions are answered
    const unanswered = [];
    roundData.questions.forEach((q, index) => {
      if (!answersChosen[q.id]) {
        unanswered.push(index + 1);
      }
    });

    if (unanswered.length > 0) {
      playSound("incorrect");
      updateTeacherSpeech(`Ho eens even! Je bent vergeten om <strong>Vraag ${unanswered.join(" en ")}</strong> te beantwoorden. Kijk er nog eens rustig naar!`, "⚠️");
      
      // Flash the background of unanswered blocks
      unanswered.forEach(index => {
        const block = document.getElementById(`q-block-${index - 1}`);
        if (block) {
          block.style.borderColor = "var(--color-error)";
          block.style.boxShadow = "0 0 15px rgba(239, 68, 68, 0.15)";
          setTimeout(() => {
            block.style.borderColor = "";
            block.style.boxShadow = "";
          }, 1500);
        }
      });
      return;
    }

    // Process evaluation
    appState = "FEEDBACK";
    let roundCorrectCount = 0;
    const feedbackListContainer = document.createElement("div");
    feedbackListContainer.className = "quiz-grid";
    
    // Re-render text card in feedback mode for reference
    const leftCol = document.createElement("div");
    leftCol.className = "reading-card";
    leftCol.innerHTML = `
      <div class="badge-container">
        <span class="badge badge-primary">Ronde ${currentRound + 1} Evaluatie</span>
        <span class="badge badge-warning">Doel: ${roundData.goal}</span>
      </div>
      <h2>${roundData.title}</h2>
      <div class="reading-text">${roundData.text}</div>
    `;
    feedbackListContainer.appendChild(leftCol);

    const rightCol = document.createElement("div");
    rightCol.className = "questions-card";

    // Feedback Header Card
    const headerBox = document.createElement("div");
    headerBox.className = "feedback-header-box";
    rightCol.appendChild(headerBox);

    // Process each question
    roundData.questions.forEach((q, idx) => {
      const userChoice = answersChosen[q.id];
      const isCorrect = userChoice === q.correct;
      const dot = document.getElementById(`dot-${currentRound}-${idx}`);

      if (isCorrect) {
        roundCorrectCount++;
        if (dot) dot.className = "node-dot correct";
      } else {
        if (dot) dot.className = "node-dot incorrect";
      }

      const qFeedbackCard = document.createElement("div");
      qFeedbackCard.className = `feedback-item ${isCorrect ? "correct-box" : "incorrect-box"}`;
      
      // Get full text of option
      const selectedOptionText = q.options.find(o => o.key === userChoice).text;
      const correctOptionText = q.options.find(o => o.key === q.correct).text;

      qFeedbackCard.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center">
          <div class="question-number" style="color: ${isCorrect ? "var(--color-success)" : "var(--color-error)"}">Vraag ${q.id}</div>
          <span class="feedback-badge ${isCorrect ? "correct" : "incorrect"}">
            ${isCorrect ? "Goed! 🎉" : "Fout! ❌"}
          </span>
        </div>
        <div class="question-title">${q.question}</div>
        <div style="font-size: 0.95rem; line-height: 1.4">
          ${isCorrect 
            ? `<strong>Jouw antwoord:</strong> <span style="color: var(--color-success)">[${userChoice}] ${selectedOptionText}</span>` 
            : `<strong>Jouw antwoord:</strong> <span style="color: var(--color-error)">[${userChoice}] ${selectedOptionText}</span><br>
               <strong>Het juiste antwoord:</strong> <span style="color: var(--color-success)">[${q.correct}] ${correctOptionText}</span>`
          }
        </div>
        <div class="explanation-text">
          ${q.explanation}
        </div>
      `;
      rightCol.appendChild(qFeedbackCard);
    });

    // Update global scores
    roundScores.push(roundCorrectCount);
    totalScore += roundCorrectCount;
    updateProgressBar();

    // Add round scores inside headerBox
    headerBox.innerHTML = `
      <div class="feedback-score-display">
        <div class="feedback-score-circle">${roundCorrectCount}/4</div>
        <div class="feedback-score-text">
          <h3>Ronde ${currentRound + 1} compleet!</h3>
          <p>Je behaalde een score van ${roundCorrectCount} goed.</p>
        </div>
      </div>
    `;

    // Action button for next round
    const actionContainer = document.createElement("div");
    actionContainer.className = "action-bar";
    const nextBtn = document.createElement("button");
    nextBtn.className = "btn-primary";
    
    const isFinalRound = currentRound === activeTexts.length - 1;
    if (isFinalRound) {
      nextBtn.innerHTML = `Bekijk Eindresultaat <span style="font-size: 1.1rem">🏆</span>`;
      nextBtn.addEventListener("click", showFinalResults);
    } else {
      nextBtn.innerHTML = `Volgende Tekst <span style="font-size: 1.1rem">➔</span>`;
      nextBtn.addEventListener("click", () => {
        currentRound++;
        appState = "QUIZ";
        updateProgressBar();
        renderCurrentRound();
        const randQuote = teacherQuotes[Math.floor(Math.random() * teacherQuotes.length)];
        updateTeacherSpeech(`Klaar voor de volgende ronde? Super! Hier is tekst ${currentRound + 1}. ${randQuote}`, "🔥");
      });
    }

    actionContainer.appendChild(nextBtn);
    rightCol.appendChild(actionContainer);
    feedbackListContainer.appendChild(rightCol);

    mainContent.innerHTML = "";
    mainContent.appendChild(feedbackListContainer);

    // Sound effects and teacher speech based on score
    if (roundCorrectCount === 4) {
      playSound("correct");
      const randComp = positiveCompliments[Math.floor(Math.random() * positiveCompliments.length)];
      updateTeacherSpeech(`<strong>${randComp}</strong> Dat is een perfecte score van 4 uit 4! Je hebt alle regels van het spiekbriefje meesterlijk toegepast! 🌟`, "😎");
    } else if (roundCorrectCount >= 2) {
      playSound("correct");
      updateTeacherSpeech(`Heel netjes gedaan! Je hebt er ${roundCorrectCount} van de 4 goed. Lees de uitleg bij de fouten goed door om er nóg beter in te worden!`, "👍");
    } else {
      playSound("incorrect");
      updateTeacherSpeech(`Geeft helemaal niks! We zijn hier om te leren. Fouten maken is juist hoe je slimmer wordt. Lees mijn uitgebreide uitleg hieronder rustig door. Je kunt dit! 📚`, "❤️");
    }
  };

  // Show final results screen with circular progress, animations and grade
  const showFinalResults = () => {
    playSound("complete");
    appState = "FINAL";
    
    // Hide top progress bar since we are done
    progressContainer.style.display = "none";

    const attemptedRounds = activeTexts.length - startingRound;
    const totalQuestions = attemptedRounds * 4;
    const percentage = (totalScore / totalQuestions) * 100;
    
    // Custom Grade (Dutch school grading scale: 1.0 to 10.0)
    // Formula: (Score / totalQuestions) * 9 + 1
    const rawGrade = (totalScore / totalQuestions) * 9 + 1;
    const finalGrade = rawGrade.toFixed(1);

    // Save attempt to history
    saveTestResult(totalScore, totalQuestions, finalGrade, startingRound);

    // Feedback rating description
    let rankName = "";
    let rankColor = "";
    let emoji = "";
    let speechText = "";

    if (totalScore >= Math.round(0.9 * totalQuestions)) {
      rankName = "Meester-Lezer 🏆";
      emoji = "🤩";
      speechText = `Wauw, wat een fabelachtige prestatie! Je hebt een <strong>${finalGrade}</strong> gehaald. Je snapt de opbouw, tekstdoelen en signaalwoorden echt perfect. Je bent helemaal klaar voor de klas 2 toetsen!`;
      triggerConfetti();
    } else if (totalScore >= Math.round(0.7 * totalQuestions)) {
      rankName = "Tekst-Expert 💎";
      emoji = "😎";
      speechText = `Supergoed gedaan! Een <strong>${finalGrade}</strong> is een fantastisch resultaat. Je hebt de grote lijnen en het Spiekbriefje heel goed gebruikt. Nog een klein beetje extra oefening en je haalt die perfecte score!`;
      triggerConfetti();
    } else if (totalScore >= Math.round(0.5 * totalQuestions)) {
      rankName = "Voldoende op Zak 👍";
      emoji = "🙂";
      speechText = `Keurig! Een mooie voldoende met een <strong>${finalGrade}</strong>. Je bent op de goede weg! Kijk nog eens goed naar de onderdelen die je lastig vond (zoals citeren of signaalwoorden) zodat je volgende keer nóg hoger scoort.`;
    } else {
      rankName = "Onderweg naar Succes 🚀";
      emoji = "💪";
      speechText = `Je hebt hard gewerkt! Hoewel je score nu een <strong>${finalGrade}</strong> is, heb je vandaag heel veel geleerd. Het begrijpen van teksten kost tijd. Neem het Spiekbriefje er nog eens bij en probeer het gerust nog een keer. Ik geloof in je!`;
    }

    updateTeacherSpeech(speechText, emoji);

    // Build the final dashboard page
    const resultsCard = document.createElement("div");
    resultsCard.className = "results-card";
    resultsCard.innerHTML = `
      <div class="welcome-illustration">🏆</div>
      <h2>Gefeliciteerd met het afronden!</h2>
      <p>Je hebt ${totalQuestions} vragen beantwoord en bent nu helemaal getraind door Meester Max.</p>
      
      <div class="radial-progress-container">
        <svg class="radial-circle-svg">
          <circle class="circle-bg" cx="90" cy="90" r="80"></circle>
          <circle id="circle-fill" class="circle-fill" cx="90" cy="90" r="80"></circle>
        </svg>
        <div class="radial-score-text">
          <span class="radial-score-num" id="radial-num">0</span>
          <span class="radial-score-label">van de ${totalQuestions} goed</span>
        </div>
      </div>

      <div class="grade-badge">Schoolcijfer: ${finalGrade}</div>
      <h3>Titel behaald: <span style="color: var(--color-primary)">${rankName}</span></h3>
      <div class="closing-speech">${speechText}</div>
      
      <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 1.5rem; flex-wrap: wrap; width: 100%;">
        <button class="btn-primary" id="restart-btn">
          Probeer Opnieuw <span style="font-size: 1.1rem">🔄</span>
        </button>
        <button class="btn-secondary" id="create-exam-btn-final" style="background-color: var(--color-primary-light); color: var(--color-primary); border: 2px dashed var(--color-primary); padding: 12px 24px; font-weight: 700; border-radius: 50px; cursor: pointer; display: flex; align-items: center; gap: 8px; transition: all 0.2s;">
          Yeni Sınav Yarat 🪄
        </button>
      </div>
    `;

    mainContent.innerHTML = "";
    mainContent.appendChild(resultsCard);

    // Animate the radial circular progress bar
    setTimeout(() => {
      const circleFill = document.getElementById("circle-fill");
      const radialNum = document.getElementById("radial-num");
      
      if (circleFill) {
        // Calculate offset (527.7 is the full stroke circumference)
        const offset = 527.7 - (527.7 * totalScore) / totalQuestions;
        circleFill.style.strokeDashoffset = offset;
      }

      // Count up animation
      let count = 0;
      if (totalScore === 0) {
        radialNum.textContent = "0";
        return;
      }
      const interval = setInterval(() => {
        count++;
        if (radialNum) radialNum.textContent = count;
        if (count >= totalScore) {
          clearInterval(interval);
        }
      }, 50);
    }, 150);

    // Event listeners
    document.getElementById("restart-btn").addEventListener("click", () => {
      appState = "START";
      renderStartScreen();
    });

    document.getElementById("create-exam-btn-final").addEventListener("click", () => {
      openCreateExamModal();
    });
  };

  // Interactive modal for creating a new exam via AI assistant
  const initCreateExamModal = () => {
    if (document.getElementById("create-exam-modal")) return;

    const modal = document.createElement("div");
    modal.className = "modal-overlay";
    modal.id = "create-exam-modal";
    modal.innerHTML = `
      <div class="modal-card">
        <div class="modal-header">
          <h2><span>🪄</span> Yeni Sınav Yarat</h2>
          <button class="modal-close-btn" id="modal-close">&times;</button>
        </div>
        <div class="modal-body">
          <p>Examen genereren door Meester Max AI! Vul een onderwerp in en plak de gegenereerde instructie in onze chat om direct een gloednieuw examen toe te voegen.</p>
          
          <div class="form-group">
            <label for="exam-topic-input">Onderwerp / Topic van het examen:</label>
            <input type="text" id="exam-topic-input" class="modal-input" placeholder="Bijv. Ruimtevaart, Klimaatverandering, Social Media..." />
          </div>

          <div class="instruction-box" id="instruction-box" style="display: none;">
            <p style="font-weight: 600; margin-bottom: 0.25rem; color: var(--text-main);">📋 Kopieer deze tekst en plak het in onze chat:</p>
            <div class="instruction-text" id="instruction-text-content"></div>
            <button class="btn-primary" id="copy-instruction-btn" style="padding: 8px 16px; font-size: 0.9rem; align-self: flex-start;">Kopieer Instructie 📋</button>
          </div>

          <div class="modal-actions">
            <button class="btn-secondary" id="modal-cancel-btn" style="padding: 10px 20px;">Annuleren</button>
            <button class="btn-primary" id="modal-generate-btn" style="padding: 10px 24px;">Genereer Instructie ⚡</button>
          </div>
        </div>
      </div>
    `;

    document.body.appendChild(modal);

    const closeBtn = modal.querySelector("#modal-close");
    const cancelBtn = modal.querySelector("#modal-cancel-btn");
    const generateBtn = modal.querySelector("#modal-generate-btn");
    const copyBtn = modal.querySelector("#copy-instruction-btn");
    const input = modal.querySelector("#exam-topic-input");
    const instrBox = modal.querySelector("#instruction-box");
    const instrText = modal.querySelector("#instruction-text-content");

    const closeModal = () => {
      modal.classList.remove("open");
      input.value = "";
      instrBox.style.display = "none";
    };

    closeBtn.addEventListener("click", closeModal);
    cancelBtn.addEventListener("click", closeModal);
    modal.addEventListener("click", (e) => {
      if (e.target === modal) closeModal();
    });

    generateBtn.addEventListener("click", () => {
      const topic = input.value.trim();
      if (!topic) {
        playSound("incorrect");
        alert("Vul alsjeblieft een onderwerp in!");
        return;
      }

      playSound("correct");
      const instructionStr = `Genereer een nieuw examen over het onderwerp: "${topic}". Voeg dit examen automatisch toe aan de Begrijpend Lezen Trainer.`;
      instrText.textContent = instructionStr;
      instrBox.style.display = "flex";
    });

    copyBtn.addEventListener("click", () => {
      navigator.clipboard.writeText(instrText.textContent).then(() => {
        playSound("correct");
        copyBtn.innerHTML = "Gekopieerd! ✓";
        copyBtn.style.backgroundColor = "var(--color-success)";
        setTimeout(() => {
          copyBtn.innerHTML = "Kopieer Instructie 📋";
          copyBtn.style.backgroundColor = "";
        }, 2000);
      }).catch(err => {
        console.error("Copy failed:", err);
      });
    });
  };

  const openCreateExamModal = () => {
    initCreateExamModal();
    const modal = document.getElementById("create-exam-modal");
    if (modal) {
      modal.classList.add("open");
      const input = modal.querySelector("#exam-topic-input");
      if (input) input.focus();
    }
  };

  // Render original Start / Welcome screen
  const renderStartScreen = () => {
    progressContainer.style.display = "none";
    const totalQuestions = 16; // 4 texts * 4 questions
    updateTeacherSpeech(`Welkom! Klik op een van de examens hieronder om een Begrijpend Lezen oefening te starten! 📚`, "👨‍🏫");

    const startCard = document.createElement("div");
    startCard.className = "welcome-card";
    startCard.innerHTML = `
      <div class="welcome-illustration">📖</div>
      <h2>Oefen je Begrijpend Lezen!</h2>
      <p>Klaar om je lees-skills een flinke boost te geven? We hebben 10 unieke examens voor je klaargezet. Elk examen bevat 4 verschillende leesteksten en 16 uitdagende vragen die precies aansluiten op jouw 2 mavo niveau!</p>
      
      <div style="background-color: var(--bg-sidebar); border: 1px solid var(--border-color); border-radius: 16px; padding: 1.25rem; margin: 0.5rem 0; width: 100%; text-align: left">
        <h4 style="color: var(--color-primary); margin-bottom: 0.5rem">💡 Handige Tips voor een Topscore:</h4>
        <ul style="list-style-position: inside; font-size: 0.95rem; line-height: 1.5; color: var(--text-muted)">
          <li>Houd het <strong>Spiekbriefje</strong> aan de linkerkant altijd goed in de gaten!</li>
          <li>Lees de teksten <em>intensief</em> door voordat je antwoordt.</li>
          <li>Kijk goed uit bij het bepalen van het <em>onderwerp</em> (max. 4 woorden!).</li>
          <li>Probeer te horen of de geluidseffecten goed klinken bij je antwoorden! 🎧</li>
        </ul>
      </div>

      <div class="test-selector-container">
        <h4 style="color: var(--color-primary); margin-bottom: 0.5rem; text-align: left; font-family: 'Outfit', sans-serif;">🎯 Kies je examen:</h4>
        <div class="test-grid" id="test-selector-grid"></div>
      </div>

      <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 1.5rem; flex-wrap: wrap; width: 100%;">
        <button class="btn-primary" id="start-btn">
          Start het Examen! <span style="font-size: 1.15rem">🚀</span>
        </button>
        <button class="btn-secondary" id="create-exam-btn" style="background-color: var(--color-primary-light); color: var(--color-primary); border: 2px dashed var(--color-primary); padding: 12px 24px; font-weight: 700; border-radius: 50px; cursor: pointer; display: flex; align-items: center; gap: 8px; transition: all 0.2s;">
          Yeni Sınav Yarat 🪄
        </button>
      </div>
    `;

    mainContent.innerHTML = "";
    mainContent.appendChild(startCard);

    const grid = document.getElementById("test-selector-grid");
    let chosenExamIndex = 0;
    const history = JSON.parse(localStorage.getItem("begrijpend_lezen_history") || "[]");

    quizData.forEach((exam, index) => {
      const card = document.createElement("div");
      card.className = "test-card";
      if (index === 0) card.classList.add("selected");
      card.dataset.index = index;

      // Find all attempts for this exam
      const examAttempts = history.filter(item => item.startingText === exam.examTitle);
      
      let statusHtml = '';
      if (examAttempts.length > 0) {
        // Find latest attempt (first in the unshifted history list)
        const latestAttempt = examAttempts[0];
        const latestGradeStr = latestAttempt.grade;

        // Find best attempt
        let bestGradeNum = 0;
        let bestGradeStr = "";
        examAttempts.forEach(item => {
          const gNum = parseFloat(String(item.grade).replace(",", "."));
          if (gNum > bestGradeNum) {
            bestGradeNum = gNum;
            bestGradeStr = item.grade;
          }
        });

        // Determine classes/colors for grade badges
        const getGradeClass = (gStr) => {
          const gNum = parseFloat(String(gStr).replace(",", "."));
          if (gNum >= 7.5) return "grade-high";
          if (gNum >= 5.5) return "grade-medium";
          return "grade-low";
        };

        statusHtml = `
          <div class="test-card-status" style="margin-top: 8px; display: flex; flex-direction: column; gap: 4px; font-size: 0.8rem; text-align: left; width: 100%;">
            <div class="gemaakt-status-label" style="font-size: 0.75rem; font-weight: 700; color: #16a34a; display: inline-flex; align-items: center; gap: 4px;">
              <span>✓ Gemaakt</span>
            </div>
            <div class="score-details-row" style="display: flex; flex-direction: column; gap: 2px; color: var(--text-muted);">
              <span>🏆 Beste: <strong class="history-grade-tag ${getGradeClass(bestGradeStr)}" style="font-size: 0.75rem; padding: 1px 4px; min-width: auto; border-radius: 4px; display: inline-block; font-weight: 800; font-family: sans-serif;">${bestGradeStr}</strong></span>
              <span>⏱️ Laatste: <strong class="history-grade-tag ${getGradeClass(latestGradeStr)}" style="font-size: 0.75rem; padding: 1px 4px; min-width: auto; border-radius: 4px; display: inline-block; font-weight: 800; font-family: sans-serif;">${latestGradeStr}</strong></span>
            </div>
          </div>
        `;
      } else {
        statusHtml = `
          <div class="test-card-status" style="margin-top: 8px; display: flex; flex-direction: column; gap: 4px; font-size: 0.8rem; text-align: left; width: 100%;">
            <div class="gemaakt-status-label" style="font-size: 0.75rem; font-weight: 700; color: var(--text-muted); display: inline-flex; align-items: center; gap: 4px;">
              <span>Nog niet gemaakt</span>
            </div>
          </div>
        `;
      }

      card.innerHTML = `
        <span class="test-card-title">${exam.examTitle}</span>
        <span class="test-card-goal" title="Examenomvang">4 Teksten</span>
        <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: 500; display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical; overflow: hidden;" title="16 Vragen">16 Vragen</span>
        ${statusHtml}
      `;

      card.addEventListener("click", () => {
        document.querySelectorAll(".test-card").forEach(c => c.classList.remove("selected"));
        card.classList.add("selected");
        chosenExamIndex = index;
        playSound("correct");
        updateTeacherSpeech(`Geweldige keuze! We starten straks met <strong>${exam.examTitle}</strong>. Dit examen bevat 4 leesteksten en 16 leerzame vragen. Zet 'm op! 📚`, "🔥");
      });

      grid.appendChild(card);
    });

    document.getElementById("start-btn").addEventListener("click", () => {
      currentExamIndex = chosenExamIndex;
      startQuiz(0);
    });

    document.getElementById("create-exam-btn").addEventListener("click", () => {
      openCreateExamModal();
    });

    // Render results history panel at the bottom
    const historySection = renderHistorySection();
    if (historySection) {
      mainContent.appendChild(historySection);
    }
  };

  // Canvas Confetti animation (Pure JS - zero dependencies)
  const triggerConfetti = () => {
    const canvas = document.createElement("canvas");
    canvas.style.position = "fixed";
    canvas.style.top = "0";
    canvas.style.left = "0";
    canvas.style.width = "100vw";
    canvas.style.height = "100vh";
    canvas.style.pointerEvents = "none";
    canvas.style.zIndex = "999";
    document.body.appendChild(canvas);

    const ctx = canvas.getContext("2d");
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;

    window.addEventListener("resize", () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    });

    const colors = ["#6366f1", "#10b981", "#f59e0b", "#f43f5e", "#8b5cf6", "#06b6d4"];
    const particles = [];

    // Generate confetti particles
    for (let i = 0; i < 120; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height - height,
        r: Math.random() * 6 + 4,
        d: Math.random() * height,
        color: colors[Math.floor(Math.random() * colors.length)],
        tilt: Math.random() * 10 - 5,
        tiltAngleIncremental: Math.random() * 0.07 + 0.02,
        tiltAngle: 0
      });
    }

    const draw = () => {
      ctx.clearRect(0, 0, width, height);

      particles.forEach((p, idx) => {
        p.tiltAngle += p.tiltAngleIncremental;
        p.y += (Math.cos(p.d) + 3 + p.r / 2) / 2;
        p.x += Math.sin(p.tiltAngle);
        p.tilt = Math.sin(p.tiltAngle - idx / 3) * 15;

        ctx.beginPath();
        ctx.lineWidth = p.r;
        ctx.strokeStyle = p.color;
        ctx.moveTo(p.x + p.tilt + p.r / 2, p.y);
        ctx.lineTo(p.x + p.tilt, p.y + p.tilt + p.r / 2);
        ctx.stroke();
      });

      // Keep animating if particles are still on screen
      const activeParticles = particles.some(p => p.y < height);
      if (activeParticles) {
        requestAnimationFrame(draw);
      } else {
        canvas.remove();
      }
    };

    draw();
  };

  // Results History Functions
  const saveTestResult = (score, total, grade, startingIndex) => {
    try {
      const history = JSON.parse(localStorage.getItem("begrijpend_lezen_history") || "[]");
      const timestamp = new Date().toISOString();
      
      const examTitle = quizData[currentExamIndex].examTitle;
      
      history.unshift({
        timestamp,
        score,
        total,
        grade,
        startingText: examTitle,
        startingTitle: "Examen voltooid"
      });
      
      localStorage.setItem("begrijpend_lezen_history", JSON.stringify(history));
    } catch (e) {
      console.error("Could not save result to history:", e);
    }
  };

  const renderHistorySection = () => {
    const history = JSON.parse(localStorage.getItem("begrijpend_lezen_history") || "[]");
    
    const container = document.createElement("div");
    container.className = "history-container collapsed";
    
    const header = document.createElement("div");
    header.className = "history-header";
    header.innerHTML = `
      <div class="history-header-title">
        <span>📊</span> Resultatenhistorie (${history.length})
      </div>
      <div class="history-arrow">▼</div>
    `;
    
    const content = document.createElement("div");
    content.className = "history-content";
    
    if (history.length === 0) {
      content.innerHTML = `
        <div class="history-empty">
          Nog geen resultaten opgeslagen. Start een oefening om je eerste resultaat te zien!
        </div>
      `;
    } else {
      // --- Summary block ---
      const grades = history.map(item => parseFloat(String(item.grade).replace(",", ".")));
      const avgGrade = grades.reduce((sum, g) => sum + g, 0) / grades.length;
      const highGrade = Math.max(...grades);
      const fmtGrade = val => val.toFixed(1).replace(".", ",");

      const summary = document.createElement("div");
      summary.className = "history-summary";
      summary.innerHTML = `
        <div class="stat-card stat-card--avg">
          <div class="stat-card__icon">🎯</div>
          <div class="stat-card__value stat-card__value--primary">${fmtGrade(avgGrade)}</div>
          <div class="stat-card__label">Gemiddeld cijfer</div>
        </div>
        <div class="stat-card stat-card--high">
          <div class="stat-card__icon">🏆</div>
          <div class="stat-card__value stat-card__value--success">${fmtGrade(highGrade)}</div>
          <div class="stat-card__label">Hoogste cijfer</div>
        </div>
        <div class="stat-card stat-card--count">
          <div class="stat-card__icon">📝</div>
          <div class="stat-card__value">${history.length}</div>
          <div class="stat-card__label">Toetsen gemaakt</div>
        </div>
      `;
      content.appendChild(summary);
      // --- End summary block ---

      const list = document.createElement("div");
      list.className = "history-list";
      
      history.forEach(item => {
        const date = new Date(item.timestamp);
        const formattedDate = date.toLocaleDateString("nl-NL", {
          day: "2-digit",
          month: "2-digit",
          year: "numeric",
          hour: "2-digit",
          minute: "2-digit"
        });
        
        const gradeNum = parseFloat(item.grade);
        let gradeClass = "grade-low";
        if (gradeNum >= 7.5) {
          gradeClass = "grade-high";
        } else if (gradeNum >= 5.5) {
          gradeClass = "grade-medium";
        }
        
        const itemDiv = document.createElement("div");
        itemDiv.className = "history-item";
        itemDiv.innerHTML = `
          <div class="history-meta">
            <span class="history-date">${formattedDate}</span>
            <span class="history-test-title" title="${item.startingTitle}">Startte bij ${item.startingText}</span>
          </div>
          <div class="history-stats">
            <span class="history-score-badge">${item.score} / ${item.total}</span>
            <span class="history-grade-tag ${gradeClass}">${item.grade}</span>
          </div>
        `;
        list.appendChild(itemDiv);
      });
      
      content.appendChild(list);
      
      const actions = document.createElement("div");
      actions.className = "history-actions";
      
      const exportBtn = document.createElement("button");
      exportBtn.className = "btn-secondary";
      exportBtn.innerHTML = `📁 Export JSON`;
      exportBtn.addEventListener("click", exportHistoryJSON);
      
      const clearBtn = document.createElement("button");
      clearBtn.className = "btn-secondary";
      clearBtn.innerHTML = `🗑️ Wis geschiedenis`;
      clearBtn.addEventListener("click", () => {
        if (confirm("Weet je zeker dat je alle resultaten wilt wissen?")) {
          localStorage.removeItem("begrijpend_lezen_history");
          renderStartScreen();
        }
      });
      
      actions.appendChild(clearBtn);
      actions.appendChild(exportBtn);
      content.appendChild(actions);
    }
    
    header.addEventListener("click", () => {
      container.classList.toggle("collapsed");
    });
    
    container.appendChild(header);
    container.appendChild(content);
    
    return container;
  };

  const exportHistoryJSON = () => {
    try {
      const history = localStorage.getItem("begrijpend_lezen_history") || "[]";
      const blob = new Blob([history], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `begrijpend-lezen-resultaten-${new Date().toISOString().slice(0, 10)}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    } catch (e) {
      console.error("Export failed:", e);
    }
  };

  // Initialize
  renderStartScreen();
});
