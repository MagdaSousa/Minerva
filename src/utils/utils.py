def calculate_growth_rate(gdp):
    """calcular taxa de crescimento"""
    pass


def verify_period(intial_period: int, final_period: int):
    if intial_period > final_period:
        raise ValueError('field country_code cannot be null')
    elif intial_period == final_period:
        raise ValueError('field country_code cannot be null')
    else:
        return None
