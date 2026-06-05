from fastapi import APIRouter, Query

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
async def get_profiles(
    start_date: str = Query(
        ...,
        description="Start date in ISO format"
    ),
    end_date: str = Query(
        ...,
        description="End date in ISO format"
    ),
    polygon: str = Query(
        ...,
        description="Polygon coordinates"
    )
):

    profiles = await argovis_service.get_profiles(
        start_date=start_date,
        end_date=end_date,
        polygon=polygon
    )

    return transform_profiles(profiles)