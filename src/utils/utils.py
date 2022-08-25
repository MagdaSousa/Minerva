import re

from fastapi import HTTPException, status

from src.exceptions.exception import ValueWithInvalidTypeException, QueryPeriodErrorException

from loguru import logger
from typing import Union


def calculate_growth_rate(dict_values):
    """calcular taxa de crescimento"""
    ordered_list = sorted(dict_values):


    growth_rate =  ((current_value – previous_years_value) / previous_years_value) * 100
    pass


def validating_user_input_data_type(sent: Union[str, int, float], expected: Union[str, int]):
    logger.info(f"[Validations].[validating_user_input_data_type]")
    number_pattern = re.compile('^[0-9]+$')
    string_pattern = re.compile('^[a-zA-Z]+$')
    if expected == str and not re.search(string_pattern, str(sent)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"{ValueWithInvalidTypeException(sent)}"
        )
    elif expected == int and not re.search(number_pattern, str(sent)):
        message = f"{sent} Deve ser passado somente um valor inteiro"

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"{ValueWithInvalidTypeException(sent, message)}"
        )



def validations_per_period(initial: int, final: int):
    validating_user_input_data_type(sent=initial, expected=int)

    validating_user_input_data_type(sent=final, expected=int)

    logger.info(f"[Validations].[validations_per_period]")

    if len(str(initial)) > 4 or len(str(initial)) < 4:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='deve ser passado um valor númerico '
                                                            'de 4 digitos como período inicial'
        )
    elif len(str(final)) > 4 or len(str(final)) < 4:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='deve ser passado um valor númerico '
                                                            'de 4 digitos como período final'
        )

    elif initial > final:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='o ano inicial deve ser inferior ao final'
        )

