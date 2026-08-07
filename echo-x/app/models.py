
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class CaseCreate(BaseModel):
    title: str
    case_number: Optional[str] = None
    investigator: str
    department: str
    description: str
    priority: str  # Critical, High, Medium, Low
    crime_type: str  # Cybercrime, Homicide, Fraud, Narcotics, Kidnapping, Harassment
    location: str
    victim_details: str
    suspect_details: str
    tags: List[str] = []

class Case(CaseCreate):
    id: str
    created_at: str
    status: str  # Active, In Progress, Solved, Pending Review
    confidence_score: float
    evidence_count: int
    ai_agent_status: str

class EvidenceItem(BaseModel):
    id: str
    case_id: str
    title: str
    file_type: str  # image, video, audio, document, chat, social, gps
    file_size: str
    uploaded_at: str
    url: Optional[str] = None
    ocr_text: Optional[str] = None
    transcription: Optional[str] = None
    detected_objects: List[str] = []
    metadata: Dict[str, Any] = {}
    threat_level: str  # High, Medium, Low
    ai_summary: str

class GraphNode(BaseModel):
    id: str
    label: str
    category: str  # Victim, Suspect, Phone, Car, Weapon, Money, Place, Social, Device
    risk: str  # High, Medium, Low
    details: Dict[str, Any] = {}
    x: Optional[float] = None
    y: Optional[float] = None

class GraphEdge(BaseModel):
    id: str
    source: str
    target: str
    relation: str
    strength: float  # 0.0 to 1.0
    type: str  # encrypted, direct, financial, geo, social

class TimelineEvent(BaseModel):
    id: str
    case_id: str
    timestamp: str
    time_label: str
    title: str
    category: str  # phone, gps, bank, camera, witness, ai_reconstruction
    description: str
    source_evidence_id: Optional[str] = None
    location: Optional[str] = None
    confidence: float

class AlertItem(BaseModel):
    id: str
    case_id: str
    timestamp: str
    severity: str  # CRITICAL, HIGH, WARNING, INFO
    title: str
    message: str
    action_required: bool

class AIReasoningFlow(BaseModel):
    step_number: int
    agent_name: str
    action: str
    findings: str
    timestamp: str
    confidence: float
    source_ids: List[str]
