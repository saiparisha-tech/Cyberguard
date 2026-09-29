import os
from hindsight_client import Hindsight

HINDSIGHT_URL = os.getenv(
    "HINDSIGHT_URL",
    "http://localhost:8888"
)

client = Hindsight(
    base_url=HINDSIGHT_URL
)

BANK_ID = "cyberguard"


async def store_incident(incident):
    return await client.aretain(
        bank_id=BANK_ID,
        content=incident,
        context="Cybersecurity incident response"
    )


async def recall_incidents(query):
    return await client.arecall(
        bank_id=BANK_ID,
        query=query
    )


async def generate_response(query):
    return await client.areflect(
        bank_id=BANK_ID,
        query=query
    )