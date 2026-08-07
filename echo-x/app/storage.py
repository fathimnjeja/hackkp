
from typing import List, Dict, Any, Optional
import uuid
import datetime

# Pre-populated rich operational dataset for ECHO-X Command Center

MOCK_CASES = [
    {
        "id": "CASE-2026-07",
        "title": "Operation Nexus - Cyber Extortion & Syndicate Wiretap",
        "case_number": "CASE-2026-07",
        "investigator": "Inspector Arjun Kumar",
        "department": "Cyber Crime Special Task Force",
        "description": "Multinational darknet extortion gang targeting critical infra servers with ransomware. Intercepted encrypted audio notes, chat transcripts, and crypto transactions.",
        "priority": "Critical",
        "crime_type": "Cybercrime",
        "location": "Metro Command / Distributed",
        "victim_details": "Apex Tech Solutions, InfraCorp Global",
        "suspect_details": "Alias 'CipherGhost', Viktor Vance, Unknown Handler 'V-9'",
        "tags": ["Ransomware", "Crypto", "Deepfake", "GPS-Correlated"],
        "created_at": "2026-08-04 10:24:00",
        "status": "In Progress",
        "confidence_score": 92.4,
        "evidence_count": 139,
        "ai_agent_status": "Active Analysis"
    },
    {
        "id": "CASE-2026-06",
        "title": "Operation Midnight Shadow - Syndicate Homicide",
        "case_number": "CASE-2026-06",
        "investigator": "Captain Sarah Vance",
        "department": "Homicide & Tactical Intelligence",
        "description": "High-profile robbery and homicide at Central Vault. ANPR cameras matched license plate, CCTV captured masked suspects entering fleeing sedan.",
        "priority": "High",
        "crime_type": "Homicide",
        "location": "Downtown Financial District",
        "victim_details": "Marcus Thorne (Vault Manager)",
        "suspect_details": "Dmitri Rostov (Primary), Alexi Drake (Accomplice)",
        "tags": ["CCTV", "ANPR", "Ballistics", "Biometric Match"],
        "created_at": "2026-08-01 14:15:00",
        "status": "In Progress",
        "confidence_score": 88.7,
        "evidence_count": 48,
        "ai_agent_status": "Correlating"
    },
    {
        "id": "CASE-2026-05",
        "title": "Vanguard Syndicate - Crypto Laundering & Narc-Trafficking",
        "case_number": "CASE-2026-05",
        "investigator": "Det. Marcus Reed",
        "department": "Financial Crime & Narcotics Unit",
        "description": "Multi-million dollar laundering scheme disguised through shell tech companies and offshore crypto wallets.",
        "priority": "Medium",
        "crime_type": "Fraud",
        "location": "Harbor Bay Marina",
        "victim_details": "State Revenue Department",
        "suspect_details": "Elena Rostova, Sovereign Holdings LLC",
        "tags": ["Crypto", "Shell Company", "Wire Transfer"],
        "created_at": "2026-07-28 09:30:00",
        "status": "Solved",
        "confidence_score": 96.1,
        "evidence_count": 82,
        "ai_agent_status": "Archived"
    }
]

MOCK_EVIDENCE = [
    {
        "id": "EVD-101",
        "case_id": "CASE-2026-07",
        "title": "Encrypted WhatsApp Chat Export (screenshot_07.png)",
        "file_type": "chat",
        "file_size": "2.4 MB",
        "uploaded_at": "2026-08-05 14:35:10",
        "url": "/static/assets/chat_evidence.png",
        "ocr_text": "OCR Text Extracted:\n'Transfer 45.5 BTC to 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa before 02:00 AM or server wipes kick off. See you at Metro Terminal 2.'\nDetected Phone: +91 98765 43210",
        "transcription": None,
        "detected_objects": ["Smartphone Screen", "Text Messaging Interface", "BTC Address String", "Timestamp UI"],
        "metadata": {"Resolution": "1170x2532", "Device": "iPhone 15 Pro", "GPS": "10.0168° N, 76.3418° E", "Software": "WhatsApp 2.24.12"},
        "threat_level": "High",
        "ai_summary": "Extracted extortion demand and BTC wallet string. Matched phone number to target suspect alias 'CipherGhost'."
    },
    {
        "id": "EVD-102",
        "case_id": "CASE-2026-07",
        "title": "Voice Intercept Wiretap (voice_recording_03.mp3)",
        "file_type": "audio",
        "file_size": "11.8 MB",
        "uploaded_at": "2026-08-05 14:35:54",
        "url": "/static/assets/audio_wiretap.mp3",
        "ocr_text": None,
        "transcription": "[00:01:23] Suspect A: 'The payload is ready. Meets at Railway Station Platform 2 at 20:45. Make sure the phone is switched off right after.'\n[00:01:45] Suspect B: 'Understood. Signal confirmed.'",
        "detected_objects": ["Voice Print: Male (Pitch 110Hz)", "Background Noise: Train Horn (Acoustic Match 94%)"],
        "metadata": {"Duration": "02:45", "Format": "MP3 Audio", "SampleRate": "44.1kHz", "VoiceprintID": "VP-9982-CIPHER"},
        "threat_level": "High",
        "ai_summary": "Voiceprint match 94.2% with CipherGhost (Viktor Vance). Mentioned location 'Railway Station Platform 2'."
    },
    {
        "id": "EVD-103",
        "case_id": "CASE-2026-07",
        "title": "CCTV Footage - Metro Station Entrance (CCTV_Station_01.mp4)",
        "file_type": "video",
        "file_size": "24.5 MB",
        "uploaded_at": "2026-08-05 15:10:00",
        "url": "/static/assets/cctv_sample.mp4",
        "ocr_text": "ANPR License Plate Detected: KA-01-MJ-8899",
        "transcription": None,
        "detected_objects": ["Masked Male (Height ~182cm)", "Black Audi Sedan", "Duffle Bag", "Smart Watch"],
        "metadata": {"FPS": "30", "Codec": "H.264", "CameraID": "CAM-METRO-04", "Timestamp": "2026-08-05 20:41:00"},
        "threat_level": "High",
        "ai_summary": "Facial similarity algorithm identified 89.4% match with suspect Viktor Vance despite partial face mask."
    },
    {
        "id": "EVD-104",
        "case_id": "CASE-2026-07",
        "title": "Bank Transaction Ledger (complaint_document.pdf)",
        "file_type": "document",
        "file_size": "4.2 MB",
        "uploaded_at": "2026-08-05 16:00:00",
        "url": "/static/assets/bank_ledger.pdf",
        "ocr_text": "Wire Transfer #TXN-998812\nAmount: $450,000 USD\nOrigin: Shell Corp 'Vanguard Tech Ltd'\nDestination: Offshore Cayman Trust #88129",
        "transcription": None,
        "detected_objects": ["Bank Stamp", "Official Signature", "Routing Code"],
        "metadata": {"Pages": "14", "Author": "Audit AI", "Encryption": "None"},
        "threat_level": "Medium",
        "ai_summary": "Correlated wire transfer of $450,000 to shell account linked with suspect Viktor Vance."
    }
]

MOCK_GRAPH_DATA = {
    "nodes": [
        {"id": "N-1", "label": "Viktor Vance (CipherGhost)", "category": "Suspect", "risk": "High", "details": {"Status": "Primary Suspect", "Wanted": "Yes", "Threat": "98%"}},
        {"id": "N-2", "label": "Marcus Thorne", "category": "Victim", "risk": "Low", "details": {"Status": "Victim", "Company": "Apex Tech"}},
        {"id": "N-3", "label": "+91 98765 43210", "category": "Phone", "risk": "High", "details": {"Carrier": "CyberTel", "SIM Status": "Burner"}},
        {"id": "N-4", "label": "Black Audi (KA-01-MJ-8899)", "category": "Car", "risk": "Medium", "details": {"Owner": "Shell Lease Ltd", "ANPR Matches": 14}},
        {"id": "N-5", "label": "1A1zP1eP5QGefi2DMPTf...", "category": "Money", "risk": "High", "details": {"Crypto": "Bitcoin", "Balance": "145.2 BTC"}},
        {"id": "N-6", "label": "Railway Station Platform 2", "category": "Place", "risk": "Medium", "details": {"Location": "Kochi/Metro", "Predicted Scene": "91% Confidence"}},
        {"id": "N-7", "label": "@user_echo (Insta)", "category": "Social", "risk": "Medium", "details": {"Followers": "14.2k", "Linked IP": "192.168.1.45"}},
        {"id": "N-8", "label": "Cipher Laptop (MacBook M3)", "category": "Device", "risk": "High", "details": {"MAC": "00:1A:2B:3C:4D:5E", "Storage": "Encrypted APFS"}}
    ],
    "edges": [
        {"id": "E-1", "source": "N-1", "target": "N-3", "relation": "Operates Burner Phone", "strength": 0.95, "type": "direct"},
        {"id": "E-2", "source": "N-1", "target": "N-4", "relation": "Seen in CCTV Fleeing Vehicle", "strength": 0.89, "type": "geo"},
        {"id": "E-3", "source": "N-3", "target": "N-2", "relation": "Sent Extortion Threat SMS", "strength": 0.98, "type": "encrypted"},
        {"id": "E-4", "source": "N-1", "target": "N-5", "relation": "Receiving Wallet Address", "strength": 0.92, "type": "financial"},
        {"id": "E-5", "source": "N-1", "target": "N-6", "relation": "Interception Meeting Point", "strength": 0.91, "type": "geo"},
        {"id": "E-6", "source": "N-3", "target": "N-7", "relation": "Linked Recovery Phone", "strength": 0.84, "type": "social"},
        {"id": "E-7", "source": "N-1", "target": "N-8", "relation": "Primary Workstation", "strength": 0.96, "type": "direct"}
    ]
}

MOCK_TIMELINE = [
    {
        "id": "TL-1",
        "case_id": "CASE-2026-07",
        "timestamp": "2026-08-05 07:35:00",
        "time_label": "07:35 AM",
        "title": "Victim Device Last Active at Home",
        "category": "gps",
        "description": "Victim's iPhone pinged home Wi-Fi base station. Normal morning movement detected.",
        "location": "MG Road Residence",
        "confidence": 99.0
    },
    {
        "id": "TL-2",
        "case_id": "CASE-2026-07",
        "timestamp": "2026-08-05 08:02:00",
        "time_label": "08:02 AM",
        "title": "Fuel Purchase Captured on CCTV",
        "category": "camera",
        "description": "Black Audi KA-01-MJ-8899 refueled at Metro Shell Station. Driver paid cash.",
        "location": "Shell Station #4",
        "confidence": 94.5
    },
    {
        "id": "TL-3",
        "case_id": "CASE-2026-07",
        "timestamp": "2026-08-05 08:18:00",
        "time_label": "08:18 AM",
        "title": "Victim Phone Abruptly Switched Off",
        "category": "phone",
        "description": "Cell tower handover dropped abruptly near Metro Overpass. Cell signal severed.",
        "location": "Metro Overpass",
        "confidence": 98.2
    },
    {
        "id": "TL-4",
        "case_id": "CASE-2026-07",
        "timestamp": "2026-08-05 09:03:00",
        "time_label": "09:03 AM",
        "title": "Extortion Email Received",
        "category": "ai_reconstruction",
        "description": "Encrypted email delivered to corporate board containing server lock notice.",
        "location": "Apex HQ Server Room",
        "confidence": 96.0
    },
    {
        "id": "TL-5",
        "case_id": "CASE-2026-07",
        "timestamp": "2026-08-05 14:35:00",
        "time_label": "02:35 PM",
        "title": "Intercepted Wiretap Audio Broadcast",
        "category": "phone",
        "description": "AI Wiretap agent flagged keyphrase 'Platform 2 meeting'. Identified audio frequency.",
        "location": "Telecom Switching Hub",
        "confidence": 94.2
    },
    {
        "id": "TL-6",
        "case_id": "CASE-2026-07",
        "timestamp": "2026-08-05 20:41:00",
        "time_label": "08:41 PM",
        "title": "Suspect Appears in CCTV at Railway Station",
        "category": "camera",
        "description": "Facial similarity match confirmed suspect entering Metro Station Platform 2.",
        "location": "Railway Station Platform 2",
        "confidence": 91.0
    }
]

MOCK_REASONING_FLOW = [
    {
        "step_number": 1,
        "agent_name": "OCR AGENT",
        "action": "Extracted text & phone number from chat screenshot",
        "findings": "Extracted burner number +91 98765 43210 & BTC Wallet address.",
        "timestamp": "14:35:21",
        "confidence": 96.0,
        "source_ids": ["EVD-101"]
    },
    {
        "step_number": 2,
        "agent_name": "VISION AGENT",
        "action": "Facial Match & Object Detection in CCTV",
        "findings": "89.4% Face match with suspect Viktor Vance. Black Audi detected.",
        "timestamp": "14:35:42",
        "confidence": 94.0,
        "source_ids": ["EVD-103"]
    },
    {
        "step_number": 3,
        "agent_name": "AUDIO AGENT",
        "action": "Voiceprint Analysis & Speech-to-Text",
        "findings": "Identified voiceprint VP-9982. Phrase 'Railway Station Platform 2' extracted.",
        "timestamp": "14:35:54",
        "confidence": 93.0,
        "source_ids": ["EVD-102"]
    },
    {
        "step_number": 4,
        "agent_name": "LOCATION & CORRELATION AGENT",
        "action": "Geospatial & Time Reconstruction",
        "findings": "Cross-referenced CCTV timestamp (20:41) with wiretap call prediction (20:45). Location match 91%.",
        "timestamp": "14:36:05",
        "confidence": 91.0,
        "source_ids": ["EVD-102", "EVD-103"]
    },
    {
        "step_number": 5,
        "agent_name": "PREDICTION AGENT",
        "action": "Synthesized Threat Score & Next Move Prediction",
        "findings": "High probability of suspect attempt to flee via Railway Station Platform 2 train line at 21:00.",
        "timestamp": "14:36:30",
        "confidence": 92.4,
        "source_ids": ["EVD-101", "EVD-102", "EVD-103", "EVD-104"]
    }
]

MOCK_ALERTS = [
    {
        "id": "ALT-901",
        "case_id": "CASE-2026-07",
        "timestamp": "2 mins ago",
        "severity": "CRITICAL",
        "title": "High Risk Suspect Proximity Alert",
        "message": "ANPR Camera #42 flagged Black Audi (KA-01-MJ-8899) 450m from Railway Station.",
        "action_required": True
    },
    {
        "id": "ALT-902",
        "case_id": "CASE-2026-07",
        "timestamp": "14 mins ago",
        "severity": "HIGH",
        "title": "New Encrypted File Uploaded",
        "message": "OCR Agent processed 12 new chat logs. Found matching BTC address string.",
        "action_required": False
    },
    {
        "id": "ALT-903",
        "case_id": "CASE-2026-06",
        "timestamp": "1 hour ago",
        "severity": "WARNING",
        "title": "Missing Ballistics Evidence",
        "message": "Ballistics report pending signoff from Forensics Lab. Case score impacted.",
        "action_required": True
    },
    {
        "id": "ALT-904",
        "case_id": "CASE-2026-07",
        "timestamp": "2 hours ago",
        "severity": "INFO",
        "title": "AI Agent Synchronization Complete",
        "message": "All 8 specialized investigation subagents synthesized case updates successfully.",
        "action_required": False
    }
]
