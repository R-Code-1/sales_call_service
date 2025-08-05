# Design Brief

## Architectural Decisions
- **FastAPI** for async, high-performance API layer.
- **Modular structure**: Each service (STT, TTS, Coachable Moment, Sentiment, DB) is isolated for maintainability and extensibility.
- **SQLAlchemy** for ORM and DB abstraction (SQLite for dev, PostgreSQL for prod).
- **Docker** for consistent deployment; **docker-compose** for local dev.
- **CI/CD** with GitHub Actions for tests and builds.

## Scalability
- Stateless API: Can scale horizontally (multiple containers/VMs).
- DB can be swapped for managed Postgres for scale.
- Ready for async task queues (Celery/RabbitMQ) for heavy audio jobs.

## Fault Tolerance
- Logging and error handling in all services.
- Can add retry logic and background job queues for robustness.
- DB migrations and health checks can be added for production.

## Trade-offs
- SQLite for dev simplicity; swap for Postgres in prod.
- Placeholder AI logic for STT/TTS/Coachable Moment; swap for real models/services as needed.
- No queue in MVP, but code is structured for easy addition.
