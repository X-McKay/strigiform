"""Data model for table containing taxonomy data."""
from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel


class Taxonomy(SQLModel, table=True):
    """Schema for table containing taxonomy data."""

    scientific_name: str
    common_name: str
    species_code: str
    category: str
    taxon_order: int = Field(default=None, primary_key=True)
    com_name_codes: str
    sci_name_codes: str
    banding_codes: str
    order_name: str
    family_com_name: str
    family_sci_name: str
    report_as: float
    extinct: bool
    extinct_year: Optional[int] = None
    family_code: str
