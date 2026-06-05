from fastapi import APIRouter

from app.services.argovis_service import (
    argovis_service
)

router = APIRouter(
    prefix="/api/argo",
    tags=["Argovis"]
)


@router.get("/profiles")
async def get_profiles():

    polygon = (
        "[[-30,30],[-20,30],"
        "[-20,40],[-30,40],[-30,30]]"
    )

    profiles = await argovis_service.get_profiles(
        start_date="2025-01-01T00:00:00Z",
        end_date="2025-01-02T00:00:00Z",
        polygon=polygon
    )

    return profiles