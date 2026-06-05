from fastapi import APIRouter

from app.models.profile import ProfileSummary
from app.services.argovis_service import argovis_service
from app.services.profile_transformer import transform_profiles

router = APIRouter(
    prefix="/api/argo",
    tags=["Argovis"]
)


@router.get(
    "/profiles",
    response_model=list[ProfileSummary]
)
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

    return transform_profiles(profiles)