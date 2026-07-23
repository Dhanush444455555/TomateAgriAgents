# 🍅 Tomato Agri-Agent

## Multi-Agent Edge Intelligence Framework for Tomato Cultivation

A full-stack industry-grade multi-agent system combining LLM-powered reasoning agents, ML vision models, RAG-grounded knowledge retrieval, and a React frontend — all orchestrated through a FastAPI backend.

### Architecture

- **Perception Layer**: Disease detection (YOLOv8), Growth stage classification (MobileNetV2)
- **Context Intelligence**: RAG knowledge retrieval (ChromaDB), Weather API tool integration
- **Decision Intelligence**: 9 specialized LLM reasoning agents orchestrated with dynamic topological routing & chief agronomist decision engine
- **Deployment**: Docker Compose, SQLite/PostgreSQL, edge-ready

### Quick Start

```bash
# Clone and start
docker-compose up --build

# Or run separately:
# Backend
cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload

# Frontend
cd frontend && npm install && npm run dev
```

### Agents

| Agent | Type | Purpose |
|-------|------|----------|
| Crop Planning | LLM Agent + RAG | Variety & ROI recommendations |
| Crop Calendar | Adaptive LLM Agent | Adaptive task scheduling & milestone planning |
| Growth Stage | ML (MobileNetV2) + LLM | Image & date-based growth stage reasoning |
| Soil & Irrigation | LLM Agent + Tools | Precision water requirement (ET₀) reasoning |
| Weather | LLM Agent + Weather API | Microclimate analysis & agricultural risk forecasting |
| Nutrient | LLM Agent + RAG | Soil science & NPK fertilizer optimization |
| Disease Detection | ML (YOLOv8) + LLM | Pathologist reasoning & IDM treatment plan |
| Pest Risk | LLM Agent + IPM | Entomologist pest risk & IPM escalation |
| Knowledge | RAG + LLM | Agronomic knowledge retrieval & grounding |

### TODO

- [ ] Fine-tune growth stage model on real tomato dataset
- [ ] Fine-tune disease detection on PlantVillage dataset
- [ ] Add JWT authentication
- [ ] Add MQTT IoT sensor ingestion
- [ ] Add APScheduler background jobs for proactive reminders
