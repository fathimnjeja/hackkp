
import uuid
import datetime
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.models import CaseCreate
from app.storage import (
    MOCK_CASES, MOCK_EVIDENCE, MOCK_GRAPH_DATA, 
    MOCK_TIMELINE, MOCK_REASONING_FLOW, MOCK_ALERTS
)
from app.ai_engine import AIEngine

app = FastAPI(
    title="ECHO-X Digital Investigation Platform",
    version="2.4.0",
    description="Futuristic AI-Powered Police Command Center & Crime Reconstruction Engine"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serves static files (HTML, CSS, JS, Assets)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")

@app.get("/api/health")
async def health_check():
    return {
        "status": "OPERATIONAL",
        "system": "ECHO-X Neural Command Core",
        "version": "2.4.0",
        "ai_agents_online": 8,
        "active_pipelines": ["OCR", "VISION", "AUDIO", "METADATA", "TIMELINE", "GRAPH", "PREDICTION", "REPORT"]
    }

# Cases API
@app.get("/api/cases")
async def get_cases():
    return {"cases": MOCK_CASES}

@app.get("/api/cases/{case_id}")
async def get_case_detail(case_id: str):
    case = next((c for c in MOCK_CASES if c["id"] == case_id), None)
    if not case:
        # Return primary case if not found
        case = MOCK_CASES[0]
    return {"case": case}

@app.post("/api/cases")
async def create_case(case_data: CaseCreate):
    new_id = f"CASE-{datetime.datetime.now().strftime('%Y-%m')}-{len(MOCK_CASES) + 1:02d}"
    new_case = {
        "id": new_id,
        "title": case_data.title,
        "case_number": case_data.case_number or new_id,
        "investigator": case_data.investigator,
        "department": case_data.department,
        "description": case_data.description,
        "priority": case_data.priority,
        "crime_type": case_data.crime_type,
        "location": case_data.location,
        "victim_details": case_data.victim_details,
        "suspect_details": case_data.suspect_details,
        "tags": case_data.tags,
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Active",
        "confidence_score": 85.0,
        "evidence_count": 0,
        "ai_agent_status": "Initializing"
    }
    MOCK_CASES.insert(0, new_case)
    return {"status": "SUCCESS", "case": new_case}

# Evidence API
@app.get("/api/evidence")
async def get_evidence(case_id: str = "CASE-2026-07"):
    items = [e for e in MOCK_EVIDENCE if e["case_id"] == case_id]
    if not items:
        items = MOCK_EVIDENCE
    return {"evidence": items}

@app.post("/api/evidence/upload")
async def upload_evidence(file: UploadFile = File(...), file_type: str = Form("image")):
    analysis = AIEngine.process_evidence(file.filename, file_type)
    
    new_evd = {
        "id": f"EVD-{len(MOCK_EVIDENCE) + 101}",
        "case_id": "CASE-2026-07",
        "title": f"{file.filename} ({file_type})",
        "file_type": file_type,
        "file_size": f"{round(file.size / 1024 / 1024, 2) if file.size else 3.5} MB",
        "uploaded_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "url": f"/static/assets/sample_{file_type}.png",
        "ocr_text": analysis["ocr_text"],
        "transcription": analysis["transcription"],
        "detected_objects": analysis["detected_objects"],
        "metadata": analysis["extracted_metadata"],
        "threat_level": analysis["threat_level"],
        "ai_summary": analysis["ai_explanation"]
    }
    MOCK_EVIDENCE.insert(0, new_evd)
    
    # Update evidence count on case
    MOCK_CASES[0]["evidence_count"] += 1
    
    return {
        "status": "SUCCESS",
        "evidence": new_evd,
        "analysis": analysis
    }

# Graph API
@app.get("/api/graph/data")
async def get_graph_data():
    return MOCK_GRAPH_DATA

# Timeline API
@app.get("/api/timeline/events")
async def get_timeline(case_id: str = "CASE-2026-07"):
    return {"timeline": MOCK_TIMELINE}

# Reasoning API
@app.get("/api/reasoning/flow")
async def get_reasoning_flow():
    return {
        "overall_confidence": 92.4,
        "overall_threat_score": 94,
        "key_insights": [
            "Extracted phone number +91 98765 43210 appears in 4 different evidence files.",
            "Voiceprint match 94.2% identified suspect Viktor Vance.",
            "Intercepted call speech mentions location 'Railway Station Platform 2'.",
            "CCTV footage confirms Black Audi Sedan KA-01-MJ-8899 at location at 20:41."
        ],
        "flow": MOCK_REASONING_FLOW
    }

# Alerts API
@app.get("/api/alerts")
async def get_alerts():
    return {"alerts": MOCK_ALERTS}

# AI Chat API
@app.post("/api/ai/chat")
async def ai_chat(query: str = Form(...), case_id: str = Form("CASE-2026-07")):
    response = AIEngine.ask_assistant(query, case_id)
    return {
        "query": query,
        "response": response,
        "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
    }

# Reports API
@app.get("/api/reports/summary")
async def get_report_summary(case_id: str = "CASE-2026-07"):
    case = next((c for c in MOCK_CASES if c["id"] == case_id), MOCK_CASES[0])
    return {
        "report_id": f"RPT-{datetime.datetime.now().strftime('%Y-%m')}-001",
        "case": case,
        "total_evidence": case["evidence_count"],
        "connections_found": len(MOCK_GRAPH_DATA["edges"]),
        "confidence_score": case["confidence_score"],
        "analysis_time": "18h 24m",
        "evidence_breakdown": {
            "Images": 18,
            "Documents": 11,
            "Audio": 8,
            "Videos": 7,
            "Messages": 16,
            "Others": 8
        },
        "findings": [
            "Primary Suspect Identified: Viktor Vance (CipherGhost). Number +91 98765 43210 strongly linked.",
            "Multiple Accounts Linked: 3 social accounts and 2 wire wallets linked to suspect.",
            "Location Correlation: CCTV & ANPR activities match victim's reports in Metro District.",
            "Threatening Content Detected: Multiple extortion notes with active ransomware payload threats."
        ]
    }
