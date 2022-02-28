"""Data model for table containing birding observations."""
import datetime
from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel
from sqlmodel import UniqueConstraint

# Note: column names as of 2022/02/27


class Observations(SQLModel, table=True):
    """Schema for table containing birding observations."""

    __table_args__ = (UniqueConstraint("submission_id", "taxonomic_order"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    submission_id: str
    common_name: str
    scientific_name: str
    taxonomic_order: int
    count: Optional[int] = None
    state_province: Optional[str] = None
    county: Optional[str] = None
    location_id: str
    location: str
    latitude: float
    longitude: float
    date: datetime.date
    time: Optional[datetime.time] = None
    protocol: str
    duration_min: Optional[float] = None
    all_obs_reported: bool
    distance_km: Optional[float] = None
    area_covered_ha: Optional[float] = None
    num_observers: Optional[int] = None
    breeding_code: Optional[str] = None
    observation_details: Optional[str] = None
    comments: Optional[str] = None
    ml_catalog_numbers: Optional[str] = None
