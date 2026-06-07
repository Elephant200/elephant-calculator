from pydantic import BaseModel, Field


class LabeledValue(BaseModel):
    """A single labelled row in a tabular result (e.g. a statistics summary or
    a set of base conversions)."""

    label: str = Field(..., description="Human-readable name of the row.")
    value: str = Field(..., description="Formatted value for display.")
