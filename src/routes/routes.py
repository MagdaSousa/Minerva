from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.database.database import DBConnection, Base
from src.domains.models.association_tables.association_tables import Association
from src.domains.models.indicators.Gross_domestic_product import GrossDomesticProduct
from src.domains.models.indicators.indicators import Indicators
from src.domains.models.income_groups.invome_groups import IncomeGroups
from src.domains.models.country.region import Region
from src.domains.models.country.country import Country
from src.domains.models.period.period import Period
from src.domains.actions.gross_domestic_product_action import GDPAction
from src.domains.schemas.schemas import GDPCountryNameSchema, GDPFromRegion, GDPFromPeriod, \
    GDPResponseSchema, GrossRateResponseSchema, GrossRateByRegionSchema
from src.utils.utils import validating_user_input_data_type, validations_per_period

obj_connection = DBConnection()
engine = obj_connection.engine
get_db = obj_connection.get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/docs/Minerva')


@app.get("/gdp/country/{item}")
def get_by_country_name(item: str, db: Session = Depends(get_db)):
    """○ Todos os dados relacionados a um país informado (indicadores e descrição,
    com exceção da coluna SpecialNotes). input: Nome ou código do país"""
    validating_user_input_data_type(sent=item, expected=str)
    gdp = GDPAction.find_by_country_code_or_country_name(db, item)

    if not gdp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Country name not found"
        )

    return status.HTTP_200_OK, GDPResponseSchema(gdp).assemble_the_schematic_for_the_indicator()


@app.get("/gdp/rate/country/{item}")
def get_growth_rate(item: str, db: Session = Depends(get_db)):
    """○ Taxa de crescimento do PIB por país. input: Nome ou código do país"""
    validating_user_input_data_type(sent=item, expected=str)
    gdp = GDPAction.find_growth_rate_by_code_or_country_namey(db, item)

    if not gdp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Country name not found"
        )

    return status.HTTP_200_OK, GrossRateResponseSchema(gdp).formatting_growth_rate_data_by_country()


@app.get("/gdp/region/{item}", response_model=GDPFromRegion)
def get_gdp_by_region(item: str, db: Session = Depends(get_db)):

    """○ Consulta do PIB dos países por região (ordem alfabética). input: Região"""

    validating_user_input_data_type(sent=item, expected=str)

    gdp = GDPAction.find_by_region_name(db, item)

    if not gdp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Region name not found"
        )
    return status.HTTP_200_OK, GrossRateByRegionSchema(gdp).formatting_growth_rate_data_by_country()


@app.get("/gdp/rank/{intial_period}&{final_period}", response_model=GDPFromPeriod)
def get_by_period(intial_period: int, final_period: int, db: Session = Depends(get_db)):
    """○ Ranking dos 10 países (Nome e código) com maior e menor média de
    crescimento do PIB (GDP growth annual ) com o período sendo fornecido
    como parâmetro na API."""

    validations_per_period(intial_period, final_period)

    gdp = GDPAction.find_average_gdp_by_country(db, intial_period, final_period)

    if not gdp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado"
        )
    return status.HTTP_200_OK, GDPFromPeriod.from_orm(gdp)
