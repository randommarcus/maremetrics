from pydantic import BaseModel


class ProfileSummary(BaseModel):
    profile_id: str
    timestamp: str
    latitude: float
    longitude: float
    cycle_number: int
    profile_direction: str