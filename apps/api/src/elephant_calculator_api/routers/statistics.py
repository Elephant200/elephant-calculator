from fastapi import APIRouter

from elephant_calculator_api.models.common import LabeledValue
from elephant_calculator_api.models.statistics import Dataset, SpreadRequest
from elephant_calculator.services import statistics as stats

router = APIRouter()


@router.post("/summary", response_model=list[LabeledValue])
def descriptive_summary(data: Dataset):
    """
    Compute a full descriptive-statistics summary of a data set.

    Args:
        data (Dataset): The list of values to summarise.

    Returns:
        list[LabeledValue]: Ordered label/value rows (count, mean, median,
        quartiles, variance, standard deviation, skewness, and more).
    """
    return stats.summary(data.data)


@router.post("/mean", response_model=float)
def arithmetic_mean(data: Dataset):
    """
    Compute the arithmetic mean (average) of a data set.

    Args:
        data (Dataset): The list of values.

    Returns:
        float: The mean.
    """
    return stats.mean(data.data)


@router.post("/median", response_model=float)
def median_value(data: Dataset):
    """
    Compute the median (middle value) of a data set.

    Args:
        data (Dataset): The list of values.

    Returns:
        float: The median.
    """
    return stats.median(data.data)


@router.post("/mode", response_model=list[float])
def modal_values(data: Dataset):
    """
    Find the most frequent value(s) in a data set.

    Args:
        data (Dataset): The list of values.

    Returns:
        list[float]: The mode(s); empty if every value occurs once.
    """
    return stats.mode(data.data)


@router.post("/variance", response_model=float)
def variance_value(data: SpreadRequest):
    """
    Compute the variance of a data set.

    Args:
        data (SpreadRequest): The values plus a `sample` flag (n − 1 vs n).

    Returns:
        float: The variance.
    """
    return stats.variance(data.data, data.sample)


@router.post("/standard-deviation", response_model=float)
def standard_deviation_value(data: SpreadRequest):
    """
    Compute the standard deviation of a data set.

    Args:
        data (SpreadRequest): The values plus a `sample` flag (n − 1 vs n).

    Returns:
        float: The standard deviation.
    """
    return stats.standard_deviation(data.data, data.sample)
