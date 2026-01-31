# AI Voice Receptionist Agent

A real-time, phone-based AI receptionist that answers live inbound calls with natural, human-like conversation. Built for service businesses, it focuses on low-latency voice interaction, controlled LLM dialog, and realistic service booking flows.

## 🚀 Features
- **FastAPI Backend**: High-performance streaming support.
- **Real-time Voice**: Integration with Twilio & Deepgram (planned).
- **Latency Optimized**: Async architecture for sub-second responses.

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.10+
- [Git](https://git-scm.com/)

### 1. Clone & Install
```bash
git clone <repository-url>
cd voice-receptionist-agent

# Create virtual environment (optional but recommended)
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration
Copy the example environment file and add your API keys:
```bash
copy .env.example .env
```
Edit `.env` and fill in your keys (Twilio, OpenAI, Deepgram, ElevenLabs).

### 3. Running Locally
Start the development server:
```bash
uvicorn app.main:app --reload
```
or with specific host/port:
```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

## 🔍 Verification
Open your browser or use curl to check the health status:
- URL: `http://127.0.0.1:8000/health`
- Expected Response: `{"status": "ok", ...}`

## 📚 API Documentation
Once running, visit:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
