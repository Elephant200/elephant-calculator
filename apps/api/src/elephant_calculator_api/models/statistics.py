from pydantic import BaseModel, Field, field_validator


class Dataset(BaseModel):
    data: list[float] = Field(..., description="The data set to summarise.")

    @field_validator("data")
    def validate_non_empty(cls, v):
        if not v:
            raise ValueError("Provide at least one value.")
        return v


class SpreadRequest(Dataset):
    sample: bool = Field(
        True,
        description="Use the sample (n − 1) estimator. False uses the population (n) estimator.",
    )
