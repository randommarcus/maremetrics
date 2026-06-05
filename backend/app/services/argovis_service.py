import httpx

from app.config import ARGOVIS_BASE_URL


class ArgovisService:

    async def get_profiles(
        self,
        start_date: str,
        end_date: str,
        polygon: str
    ):

        params = {
            "startDate": start_date,
            "endDate": end_date,
            "polygon": polygon
        }

        async with httpx.AsyncClient() as client:

            response = await client.get(
                f"{ARGOVIS_BASE_URL}/argo",
                params=params,
                timeout=30
            )

            response.raise_for_status()

            return response.json()


argovis_service = ArgovisService()