
# Sales Call Service Microservice

## Overview
This project is a scalable, modular Python-based microservice for processing sales-call audio snippets, identifying coachable moments, providing structured transcripts, and generating executive summaries. It is designed for production use, with clear separation of concerns, extensibility, and fault tolerance.

## Features
- **Speech-to-Text (STT):** Upload audio via `/transcribe` and receive a transcript with speaker diarization.
- **Text-to-Speech (TTS):** Convert text to audio via `/speak`.
- **Coachable Moments:** Identify and replay key moments in calls via `/replay`.
- **Sentiment Analysis:** (Bonus) Analyze sentiment of each speaker's utterances.
- **Persistent Storage:** All data is stored in a relational database (SQLite by default).
- **Dockerized:** Easy deployment and local development with Docker and docker-compose.
- **CI/CD:** Automated testing and build with GitHub Actions.

## Setup & Run

### Prerequisites
- Docker & Docker Compose (recommended)
- Or: Python 3.8+

### Run with Docker
```sh
docker-compose up --build
```
The service will be available at http://localhost:8000

### Run Locally (Dev)
```sh
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Usage

### 1. Transcribe Audio
```sh
curl -F "audio=@sample.wav" -F "call_id=1" -F "agent_id=2" -F "customer_id=3" http://localhost:8000/transcribe
```

### 2. Text-to-Speech
```sh
curl -X POST -H "Content-Type: application/json" -d '{"text": "Let's move forward."}' http://localhost:8000/speak --output speech.wav
```

### 3. Replay Coachable Moment
```sh
curl -X POST -F "call_id=1" http://localhost:8000/replay --output replay.wav
```

## Testing
```sh
pytest app/tests
```

## Documentation
- See `DESIGN.md` for architecture, key functions, and design decisions.
- FastAPI interactive docs: http://localhost:8000/docs

## Project Structure
```
app/
  api/endpoints/    # API endpoints
  core/             # Config, DB, models, logging
  services/         # STT, TTS, coachable moment, sentiment
  tests/            # Unit/integration tests
  main.py           # FastAPI app entrypoint
Dockerfile
docker-compose.yml
requirements.txt
README.md
DESIGN.md
.github/workflows/ci.yml
```
