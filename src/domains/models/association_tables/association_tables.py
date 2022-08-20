
from src.database.database import Table,ForeignKey,Column,Base


country_indicator_association_table = Table(
    "Country_Indicator",
    Base.metadata,
    Column("Country", ForeignKey("Country.CountryID"), primary_key=True),
    Column("Indicators", ForeignKey("indicators.indicatorsID"), primary_key=True),
)


indicators_period_association_table = Table(
    "Indicators_Period",
    Base.metadata,
    Column("Indicators", ForeignKey("indicators.indicatorsID"), primary_key=True),
    Column("Period", ForeignKey("period.PeriodID"), primary_key=True),
)