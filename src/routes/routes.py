from fastapi import FastAPI, Depends, HTTPException, status, Response
from typing import Union
from sqlalchemy.orm import Session
from src.database.database import DatabaseConnection, Base
from src.domains.actions.gross_domestic_product_action import GDPAction
from src.domains.schemas.schemas import GDPCountryNameSchema, GDPFromRegion, GDPFromPeriod

# obj_connection = DatabaseConnection()
# engine = obj_connection.engine
# get_db = obj_connection.get_db()
#
# Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/gdp/country/{item}", response_model=GDPCountryNameSchema)
def get_by_country_name(item: str, db: Session = Depends(get_db)):
    """○ Todos os dados relacionados a um país informado (indicadores e descrição,
com exceção da coluna SpecialNotes). input: Nome ou código do país"""
    gdp = GDPAction.find_by_country_code_or_country_name(db, item)

    if not gdp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Country name not found"
        )
    if item.isnumeric() or item.isalnum():
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED, detail=f"""the parameter passed is not of the expected type...
                                                                                                            expected :str
                                                                                                            provided:{type(item)}"""
        )
    return GDPCountryNameSchema.from_orm(gdp)


@app.get("/gdp/country/{item}", response_model=GDPCountryNameSchema)
def get_growth_rate(item: str, db: Session = Depends(get_db)):
    """○ Taxa de crescimento do PIB por país. input: Nome ou código do país"""

    gdp = GDPAction.find_growth_rate(db, item)

    if not gdp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Country name not found"
        )

    if item.isnumeric() or item.isalnum():
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED, detail=f"""the parameter passed is not of the expected type...
                                                                                                            expected :str
                                                                                                            provided:{type(item)}"""
        )
    return GDPCountryNameSchema.from_orm(gdp)


@app.get("/gdp/pib/{item}", response_model=GDPFromRegion)
def find_gdp_by_region(item: str, db: Session = Depends(get_db)):
    """○ Consulta do PIB dos países por região (ordem alfabética). input: Região"""
    gdp = GDPAction.find_by_region_name(db, item)
    if not gdp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Region name not found"
        )
    return GDPFromRegion.from_orm(gdp)


@app.get("/gdp/pib/rank/{intial_period}&{final_period}", response_model=GDPFromPeriod)
def find_by_period(intial_period: int, final_period: int, db: Session = Depends(get_db)):
    """○ Ranking dos 10 países (Nome e código) com maior e menor média de
    crescimento do PIB (GDP growth annual ) com o período sendo fornecido
    como parâmetro na API."""
    gdp = GDPAction.find_average_gdp_by_country(db, intial_period, final_period)
    if not gdp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado"
        )
    return GDPFromPeriod.from_orm(gdp)
