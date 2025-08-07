
# Design Brief & Detailed Documentation

## Project Architecture

**Overview:**
This microservice is designed for scalable, production-grade audio processing for sales calls. It is modular, extensible, and ready for real-time and high-reliability use cases.

**Key Layers:**
- **API Layer:** FastAPI serves as the entrypoint, exposing endpoints for STT, TTS, and coachable moment replay. Routers are organized in `app/api/endpoints/` for separation of concerns.
- **Service Layer:** All business logic (STT, TTS, coachable moment, sentiment) is implemented in `app/services/`. Each service is a standalone module, making it easy to swap or extend models.
- **Core Layer:** Configuration, database models, and logging are in `app/core/`. SQLAlchemy is used for ORM, and the database can be easily switched from SQLite to PostgreSQL.
- **Persistence:** All transcriptions and metadata are stored in a relational database. The ORM layer ensures portability and maintainability.
- **Testing:** Unit and integration test stubs are provided in `app/tests/` for all endpoints.
- **Deployment:** Dockerfile and docker-compose.yml enable containerized, reproducible deployments. GitHub Actions provides CI/CD for testing and Docker builds.

## Key Functions & Endpoints

- **/transcribe** (`POST`): Accepts audio (WAV/MP3) and metadata, returns transcript and diarization. Calls `transcribe_audio` in `stt_service.py`.
- **/speak** (`POST`): Accepts text, returns TTS audio. Calls `synthesize_speech` in `tts_service.py`.
- **/replay** (`POST`): Accepts call_id, identifies a coachable moment, and returns TTS audio for that segment. Uses `get_coachable_moment` and `replay_moment` in `coachable_moment.py`.
- **Database Models:** `Transcription` model in `core/models.py` stores all call data, transcripts, diarization, and sentiment.
- **Sentiment Analysis:** (Bonus) `analyze_sentiment` in `sentiment.py` is ready for Hugging Face integration.

## Overall Approach

- **Modularity:** Each concern (API, business logic, persistence) is isolated for maintainability and extensibility.
- **Scalability:** Stateless API and modular services allow for horizontal scaling (multiple containers/VMs). Ready for async task queues (Celery/RabbitMQ) for heavy jobs.
- **Fault Tolerance:** Logging, error handling, and structure for retries/background jobs. DB migrations and health checks can be added for production.
- **Extensibility:** Easy to add new endpoints, swap models, or integrate with external services.
- **CI/CD:** Automated tests and Docker builds ensure code quality and deployment reliability.

## Trade-offs
- SQLite for dev simplicity; swap for Postgres in prod.
- Placeholder AI logic for STT/TTS/Coachable Moment; swap for real models/services as needed.
- No queue in MVP, but code is structured for easy addition.
