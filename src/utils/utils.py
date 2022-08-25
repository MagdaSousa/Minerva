import re

from fastapi import HTTPException, status

from src.exceptions.exception import ValueWithInvalidTypeException, QueryPeriodErrorException

from loguru import logger
from typing import Union


def calculate_growth_rate(dict_values):
    {"country_name": country.country_name,
     "country_code": country.country_code,
     "region_name": country.region_country_fk.region_name,
     "indicator_name": indicators[0].indicator_name,
     "list_values_indicators": [dict_values_indicators]}
    """calcular taxa de crescimento"""
    list_growth_rate = []
    ordered_list = sorted(dict_values)
    for x in range(0, len(ordered_list["list_values_indicators"]), -1):
        current_value = dict_values[x]
        previous_years_value = dict_values[x - 1]
        growth_rate = (current_value - previous_years_value) / previous_years_value * 100
        list_growth_rate.append({f"growth rate comparing the years {x} between {x - 1}": growth_rate})

    return {"country_name": country.country_name,
            "country_code": country.country_code,
            "region_name": country.region_country_fk.region_name,
            "indicator_name": indicators[0].indicator_name,
            "Growth Rate": [dict_values_indicators]}


def validating_user_input_data_type(sent: Union[str, int, float], expected: Union[str, int]):
    logger.info(f"[Validations].[validating_user_input_data_type]")

    number_pattern = re.compile('^[0-9]+$')
    # string_pattern = re.compile('^[a-zA-Z]+$')

    if expected == str and not str(sent).replace(" ", "").isalpha():
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
