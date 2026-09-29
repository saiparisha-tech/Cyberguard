from fastapi import FastAPI
from pydantic import BaseModel

from hindsight_service import (
    store_incident,
    recall_incidents,
    generate_response
)

app = FastAPI(title="CyberGuard")


class Incident(BaseModel):
    incident_id: str
    description: str


@app.get("/")
async def home():
    return {
        "message": "CyberGuard AI Incident Response Agent is running"
    }


@app.post("/incident")
async def analyze_incident(incident: Incident):

    incident_text = f"""
Incident ID: {incident.incident_id}

Cybersecurity Incident:
{incident.description}
"""

    # 1. Store the incident
    await store_incident(incident_text)

    # 2. Recall similar previous incidents
    memories = await recall_incidents(
        incident.description
    )

    recalled = []

    for memory in memories.results:
        recalled.append({
            "text": memory.text,
            "type": memory.type
        })

    # 3. Generate a response using remembered experience
    response = await generate_response(
        f"""
A cybersecurity incident has occurred:

{incident.description}

Based on previous cybersecurity incidents stored in memory,
what response should the security team take?
"""
    )

    return {
        "incident_id": incident.incident_id,
        "recalled_memories": recalled,
        "recommended_response": response.text
    }