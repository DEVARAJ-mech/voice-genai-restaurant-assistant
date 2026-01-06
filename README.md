# 🎙️ Voice-Enabled GenAI Restaurant Assistant

A fully interactive, voice-driven **Generative AI restaurant assistant**
that acts as a virtual receptionist.\
The system listens to customers via a microphone, understands their
intent, and responds with **natural, real-time speech**.

The application is designed with an **offline-first architecture**,
leveraging **Ollama + Whisper** for local inference, with an optional
**cloud fallback using Gemini**.

------------------------------------------------------------------------

## 📌 Key Features

-   🎤 **Live Speech Input** (microphone-based, no file uploads)
-   🧠 **Conversational AI** using Ollama (local LLM)
-   🗣️ **Natural Speech Output** using Edge TTS
-   💾 **Conversation Memory** for contextual continuity
-   📅 **Table Reservation Management** (SQLite)
-   🖥️ **Interactive User Interface** (Streamlit)
-   🔌 **Offline-First Design**
-   🧪 **Evaluation-Ready & Viva-Oriented Architecture**

------------------------------------------------------------------------

## 🏗️ Project Architecture

    voice-genai-restaurant-assistant/
    ├── app/
    │   ├── api/
    │   │   └── chat.py
    │   ├── core/
    │   │   └── config.py
    │   ├── db/
    │   │   └── __init__.py
    │   ├── graph/
    │   │   └── dialogue_graph.py
    │   ├── llm/
    │   │   ├── base.py
    │   │   ├── ollama.py
    │   │   └── gemini.py
    │   ├── services/
    │   │   └── dialogue.py
    │   ├── ui/
    │   │   └── streamlit_app.py
    │   ├── __init__.py
    │   └── main.py
    ├── requirements.txt
    ├── .env
    ├── .gitignore
    └── README.md

------------------------------------------------------------------------

## 🔄 Execution Flow (Runtime)

1.  User clicks **🎤 Speak**
2.  Microphone captures live audio
3.  **Whisper (faster-whisper)** transcribes speech to text
4.  Conversation context is retrieved from memory
5.  Prompt is sent to **Ollama (local LLM)**
6.  Response is generated
7.  **Edge-TTS** converts text to speech
8.  Assistant speaks the response
9.  Memory and reservation data are updated

------------------------------------------------------------------------

## ⚙️ System Requirements

-   **OS:** Windows 10 / 11\
-   **Python:** 3.11.x (recommended)\
-   **RAM:** ≥ 8 GB\
-   **Disk:** ≥ 5 GB free\
-   **Microphone:** Required\
-   **GPU:** Optional (CPU-only mode supported)

------------------------------------------------------------------------

## 🔧 Installation

### 1️⃣ Clone the Repository

``` bash
git clone https://github.com/your-username/voice-genai-restaurant-assistant.git
cd voice-genai-restaurant-assistant
```

### 2️⃣ Create & Activate Virtual Environment

``` bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

⚠️ **If PyAudio fails on Windows:**

``` bash
pip install pipwin
pipwin install pyaudio
```

### 4️⃣ Install & Run Ollama

Download Ollama:\
👉 https://ollama.com/download

Pull a lightweight model (recommended):

``` bash
ollama pull llama3.2:3b
```

Run Ollama in **CPU-only mode**:

``` powershell
$env:OLLAMA_NO_GPU=1
ollama serve
```

------------------------------------------------------------------------

## ▶️ Running the Application

### 🖥️ Streamlit UI (Recommended)

``` bash
python -m streamlit run app/ui/streamlit_app.py
```

Open in browser:

    http://localhost:8501

Click **🎤 Speak** to begin interaction.

### 🖧 Terminal-Only Voice Mode

``` bash
python -m app.main
```

------------------------------------------------------------------------

## 🧪 Evaluation Metrics (Suggested)

  Metric                     Description
  -------------------------- ------------------------------------
  STT Accuracy               Whisper transcription quality
  Response Latency           Time from speech input to response
  Task Completion Rate       Successful reservations or queries
  Conversational Coherence   Context retention
  System Stability           Crash-free runtime

------------------------------------------------------------------------

## 📊 Results (Example)

  Scenario            Outcome
  ------------------- ---------------------
  Table Reservation   ✅ Successful
  Menu Query          ✅ Correct
  General Inquiry     ✅ Accurate
  Offline Mode        ✅ Fully Functional

------------------------------------------------------------------------

## 🔐 Environment Variables

Create a `.env` file (optional):

``` env
GEMINI_API_KEY=your_api_key_here
```

------------------------------------------------------------------------

## 🧠 Supported Use Cases

-   Restaurant reception
-   Table booking
-   Menu and allergen queries
-   Order clarification
-   General restaurant information

------------------------------------------------------------------------

## 🚀 Future Enhancements

-   Wake-word detection
-   Streaming Whisper
-   Structured intent extraction (JSON)
-   Multi-language support
-   WebSocket audio streaming
-   Dockerized deployment

------------------------------------------------------------------------

## 📚 Technologies Used

-   Python 3.11
-   Streamlit
-   Ollama
-   Whisper (faster-whisper)
-   Edge-TTS
-   SQLite
-   SpeechRecognition
-   FastAPI

------------------------------------------------------------------------

## 🧑‍🎓 Academic Use

Suitable for: - Final year projects - Research internships - Viva and
demos - AI / NLP coursework

------------------------------------------------------------------------

## 📄 License

Released for **educational and research purposes** only.
