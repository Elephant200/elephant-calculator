from pydantic import BaseModel, Field


class BaseConversion(BaseModel):
    number: str = Field(..., description="The number to convert, written in the source base.")
    from_base: int = Field(
        ..., ge=2, le=36, description="The base the number is written in (2–36)."
    )
