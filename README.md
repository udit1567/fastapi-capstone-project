```bash
 ██████╗ █████╗ ██████╗     ██████╗ ██████╗ ██╗ ██████╗███████╗
██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗██║██╔════╝██╔════╝
██║     ███████║██████╔╝    ██████╔╝██████╔╝██║██║     █████╗
██║     ██╔══██║██╔══██╗    ██╔═══╝ ██╔══██╗██║██║     ██╔══╝
╚██████╗██║  ██║██║  ██║    ██║     ██║  ██║██║╚██████╗███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝

        🚀 FastAPI + Machine Learning + Redis + Docker


══════════════════════════════════════════════════════════════════

📦 PROJECT FEATURES

✔ JWT-based Authentication
✔ API Key Validation
✔ ML-Based Used Car Price Prediction
✔ Redis Caching for Faster Predictions
✔ Prometheus Metrics Integration
✔ Grafana Dashboard Monitoring
✔ Dockerized Setup
✔ Render Cloud Deployment Ready


══════════════════════════════════════════════════════════════════

🧠 MODEL INPUT VARIABLES

┌─────────────────┬──────────────────────────────┬──────────────┐
│ Feature         │ Description                  │ Example      │
├─────────────────┼──────────────────────────────┼──────────────┤
│ company         │ Brand of the car             │ Maruti       │
│ year            │ Manufacturing year           │ 2015         │
│ owner           │ Previous owners              │ Second       │
│ fuel            │ Fuel type                    │ Petrol       │
│ seller_type     │ Dealer or Individual         │ Individual   │
│ transmission    │ Transmission type            │ Automatic    │
│ km_driven       │ Kilometers driven            │ 200000       │
│ mileage_mpg     │ Mileage in MPG               │ 55           │
│ engine_cc       │ Engine capacity              │ 1250         │
│ max_power_bhp   │ Maximum power output         │ 80           │
│ torque_nm       │ Torque in Newton meters      │ 200          │
│ seats           │ Seating capacity             │ 5            │
└─────────────────┴──────────────────────────────┴──────────────┘


══════════════════════════════════════════════════════════════════

⚙️ GETTING STARTED (LOCAL)

1️⃣ Clone Repository

git clone https://github.com/your-username/fastapi-project.git

cd fastapi-project


2️⃣ Setup Environment Variables

Create .env file:

API_KEY=demo-key
JWT_SECRET_KEY=your-secret
REDIS_URL=redis://localhost:6379


3️⃣ Build & Run with Docker

docker-compose up --build


══════════════════════════════════════════════════════════════════

🌐 ACCESS SERVICES

FastAPI Docs       → http://localhost:8000/docs
Metrics Endpoint   → http://localhost:8000/metrics
Prometheus UI      → http://localhost:9090
Grafana Dashboard  → http://localhost:3000


══════════════════════════════════════════════════════════════════

🔐 AUTHENTICATION

JWT Authentication:

Authorization: Bearer <your_token>

API Key Validation:

x-api-key: demo-key


══════════════════════════════════════════════════════════════════

🚀 PREDICTION ENDPOINT

POST /predict


Example Request:

{
  "company": "Maruti",
  "year": 2015,
  "owner": "Second",
  "fuel": "Petrol",
  "seller_type": "Individual",
  "transmission": "Automatic",
  "km_driven": 200000,
  "mileage_mpg": 55,
  "engine_cc": 1250,
  "max_power_bhp": 80,
  "torque_nm": 200,
  "seats": 5
}


Example Response:

{
  "predicted_price": 425000
}


══════════════════════════════════════════════════════════════════

📊 MONITORING STACK

FastAPI  --->  Prometheus  --->  Grafana

Tracks:
✔ API Requests
✔ Latency
✔ Cache Hits
✔ System Metrics
✔ Prediction Performance


══════════════════════════════════════════════════════════════════

🐳 RUN EVERYTHING

docker-compose up --build


☁️ DEPLOYMENT

Ready for deployment on:
✔ Render
✔ Railway
✔ AWS
✔ DigitalOcean
✔ Azure


══════════════════════════════════════════════════════════════════
```