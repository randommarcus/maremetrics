import asyncio
import json

from app.services.argovis_service import (
    argovis_service
)

polygon = (
    "[[-30,30],[-20,30],"
    "[-20,40],[-30,40],[-30,30]]"
)


async def main():

    profiles = await argovis_service.get_profiles(
        start_date="2025-01-01T00:00:00Z",
        end_date="2025-01-02T00:00:00Z",
        polygon=polygon
    )

    print(f"Profiles Returned: {len(profiles)}")
    print(json.dumps(profiles[0], indent=2))


asyncio.run(main())