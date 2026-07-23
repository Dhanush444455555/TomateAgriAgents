# 🍅 Tomato Agri-Agent

## Multi-Agent Edge Intelligence Framework for Tomato Cultivation

A full-stack multi-agent system combining rule-based agents, ML vision models, RAG-based knowledge retrieval, and a React frontend — all orchestrated through a FastAPI backend.

### Architecture

- **Perception Layer**: Disease detection (YOLOv8), Growth stage classification (MobileNetV2)
- **Context Intelligence**: RAG knowledge retrieval (ChromaDB), Weather API integration
- **Decision Intelligence**: 9 specialized agents orchestrated with conflict resolution
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
| Crop Planning | Rule + RAG | Variety recommendations |
| Crop Calendar | Rule | Growth stage task scheduling |
| Growth Stage | ML (MobileNetV2) | Image-based stage detection |
| Soil & Irrigation | Rule | Irrigation recommendations |
| Weather | API | Weather data + risk flags |
| Nutrient | Rule + RAG | NPK fertilizer scheduling |
| Disease Detection | ML (YOLOv8) | Leaf/fruit disease detection |
| Pest Risk | Rule | Pest risk assessment |
| Knowledge | RAG | Agricultural knowledge retrieval |

### TODO

- [ ] Fine-tune growth stage model on real tomato dataset
- [ ] Fine-tune disease detection on PlantVillage dataset
- [ ] Add JWT authentication
- [ ] Add MQTT IoT sensor ingestion
- [ ] Add APScheduler background jobs for proactive reminders
