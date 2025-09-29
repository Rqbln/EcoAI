import os
from typing import Dict, List


import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse


app = FastAPI(title="Plot Gateway")
app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)


# Simple static registry; extend as you add services
SERVICES: Dict[str, str] = {
"matplotlib-basic": os.getenv("MATPLOTLIB_BASIC_URL", "http://matplotlib-basic:8000")
}


@app.get("/services")
async def services() -> List[dict]:
    out = []
    async with httpx.AsyncClient(timeout=3) as client:
        for sid, base in SERVICES.items():
            try:
                r = await client.get(f"{base}/info")
                info = r.json()
            except Exception:
                info = {"name": sid, "status": "unreachable"}
            out.append({"id": sid, "url": base, **info})
    return out


@app.get("/plot/{service_id}")
async def plot(service_id: str, kind: str = "sine"):
    base = SERVICES.get(service_id)
    if not base:
        raise HTTPException(404, "Unknown service")
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(f"{base}/plot", params={"kind": kind})
        if r.status_code != 200:
            raise HTTPException(r.status_code, r.text)
        return StreamingResponse(iter([r.content]), media_type="image/png")


@app.get("/metrics/global")
async def get_global_metrics():
    """Endpoint pour récupérer le score global et ses composants"""
    return {
        "global_score": 0.84,
        "breakdown": {
            "performance": {"score": 0.85, "weight": 0.40},
            "fairness": {"score": 0.78, "weight": 0.30},
            "robustness": {"score": 0.82, "weight": 0.20},
            "sustainability": {"score": 0.90, "weight": 0.10}
        },
        "calculation": "Score = (0.85*0.40) + (0.78*0.30) + (0.82*0.20) + (0.90*0.10)"
    }

@app.get("/metrics/performance")
async def get_performance_metrics():
    """Métriques de performance du modèle"""
    return {
        "accuracy": 0.91,
        "precision": 0.89,
        "recall": 0.87,
        "f1_score": 0.88,
        "auc": 0.92,
        "calibration_error": 0.03,
        "benchmark_comparison": "+3 points vs baseline"
    }

@app.get("/metrics/fairness")
async def get_fairness_metrics():
    """Métriques de fairness et biais"""
    return {
        "demographic_parity": 0.12,
        "equalized_odds": 0.08,
        "fairness_score": 0.78,
        "groups": {
            "gender": {"male": 0.85, "female": 0.81, "disparity": 0.04},
            "age": {"young": 0.83, "senior": 0.79, "disparity": 0.04},
            "origin": {"group_a": 0.84, "group_b": 0.80, "disparity": 0.04}
        },
        "mitigation_applied": True,
        "ai_act_compliance": "OK"
    }

@app.get("/metrics/robustness")
async def get_robustness_metrics():
    """Métriques de robustesse et résistance aux attaques"""
    return {
        "robustness_score": 0.82,
        "adversarial_tests": {
            "fgsm": {"epsilon_0.1": 0.86, "epsilon_0.2": 0.79, "epsilon_0.3": 0.71},
            "pgd": {"epsilon_0.1": 0.84, "epsilon_0.2": 0.77, "epsilon_0.3": 0.69}
        },
        "performance_drop": {
            "epsilon_0.1": "< 5%",
            "epsilon_0.2": "< 12%",
            "epsilon_0.3": "< 22%"
        },
        "status": "robust"
    }

@app.get("/metrics/sustainability")
async def get_sustainability_metrics():
    """Métriques de durabilité et impact carbone"""
    return {
        "training": {
            "energy_kwh": 12.5,
            "co2_kg": 6.2,
            "duration_hours": 4.2
        },
        "inference": {
            "energy_kwh": 0.3,
            "co2_kg": 0.15,
            "per_1000_requests": True
        },
        "total_co2_kg": 8.2,
        "sustainability_index": 0.90,
        "eco_label": "Medium",
        "efficiency_score": 0.84
    }

@app.get("/metrics/monitoring")
async def get_monitoring_data():
    """Données de monitoring et détection de drift"""
    return {
        "drift_detected": False,
        "last_check": "2024-12-07T10:00:00Z",
        "kpi_evolution": {
            "dates": ["2024-12-01", "2024-12-02", "2024-12-03", "2024-12-04", "2024-12-05", "2024-12-06", "2024-12-07"],
            "accuracy": [0.91, 0.90, 0.91, 0.89, 0.90, 0.91, 0.91],
            "fairness": [0.78, 0.77, 0.79, 0.78, 0.78, 0.79, 0.78],
            "sustainability": [0.90, 0.89, 0.90, 0.91, 0.90, 0.90, 0.90]
        },
        "alerts": [],
        "threshold": 0.05
    }

@app.get("/")
async def root():
    return {"ok": True}