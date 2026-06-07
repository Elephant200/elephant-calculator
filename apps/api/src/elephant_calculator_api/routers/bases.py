from fastapi import APIRouter

from elephant_calculator_api.models.common import LabeledValue
from elephant_calculator_api.models.bases import BaseConversion
from elephant_calculator.services import bases

router = APIRouter()


@router.post("/convert", response_model=list[LabeledValue])
def convert_base(data: BaseConversion):
    """
    Convert a number written in any base (2–36) to decimal, binary, octal and
    hexadecimal.

    Args:
        data (BaseConversion): The number and the base it is written in.

    Returns:
        list[LabeledValue]: Label/value rows for each target base.
    """
    return bases.convert(data.number, data.from_base)
