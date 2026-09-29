import asyncio
from hindsight_client import Hindsight


client = Hindsight(
    base_url="http://localhost:8888"
)

BANK_ID = "cyberguard"


async def main():

    print("Connecting to Hindsight...")

    # Store previous cybersecurity incident
    incident = """
    Incident ID: INC-001

    A server experienced 500 failed SSH login attempts
    from IP address 192.168.1.50 within 10 minutes.

    The incident was classified as a brute-force attack.

    The security team blocked the IP address and monitored
    authentication logs.

    The response successfully stopped the suspicious activity.
    """

    print("Storing incident in Hindsight...")

    await client.aretain(
        bank_id=BANK_ID,
        content=incident,
        context="Cybersecurity incident response"
    )

    print("Incident stored successfully!")

    # Recall previous incident
    print("\nSearching previous incidents...")

    results = await client.arecall(
        bank_id=BANK_ID,
        query="What happened previously with SSH brute-force attacks?"
    )

    print("\nRelevant memories:")

    for result in results.results:
        print("\n---")
        print(result.text)

    # Generate response using remembered experience
    print("\nGenerating response using remembered experience...")

    response = await client.areflect(
        bank_id=BANK_ID,
        query="""
        A server has experienced 450 failed SSH login attempts
        from IP address 192.168.1.50 within 10 minutes.

        Based on previous cybersecurity incidents stored in memory,
        what response should the security team take?
        """
    )

    print("\nCyberGuard Recommendation:")
    print(response.text)

    print("\nHindsight test completed!")


if __name__ == "__main__":
    asyncio.run(main())