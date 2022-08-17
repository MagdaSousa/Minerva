from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from src.database.database import DatabaseConnection, Base
from src.domains.repository.indicator_repository.cross_domestic_product_repository import GDPRepository
from src.domains.schemas.schemas import GDPCountryNameSchema, GDPFromRegion, GDPFromPeriod

obj_connection = DatabaseConnection()
engine = obj_connection.engine
get_db = obj_connection.get_db()

Base.metadata.create_all(bind=engine)

app = FastAPI()

"""A API deve possibilitar as seguintes consultas:
○ Todos os dados relacionados a um país informado (indicadores e descrição,
com exceção da coluna SpecialNotes). input: Nome ou código do país
○ Consulta do PIB dos países por região (ordem alfabética). input: Região
○ Taxa de crescimento do PIB por país. input: Nome ou código do país
○ Ranking dos 10 países (Nome e código) com maior e menor média de
crescimento do PIB (GDP growth annual ) com o período sendo fornecido
como parâmetro na API. input: Null
"""


@app.get("/gdp/pib/country/{value}", response_model=GDPCountryNameSchema)
def get_by_country_name(value: str or int, db: Session = Depends(get_db)):
    """○ Todos os dados relacionados a um país informado (indicadores e descrição,
com exceção da coluna SpecialNotes). input: Nome ou código do país"""
    if value.isnumeric():
        gdp = GDPRepository.find_by_id(db, value)
    else:
        gdp = GDPRepository.find_by_country_name(db, value)

    if not gdp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Country name not found"
        )
    return GDPCountryNameSchema.from_orm(gdp)


@app.get("/gdp/pib/{region}", response_model=GDPFromRegion)
def find_by_region(region: str, db: Session = Depends(get_db)):
    """○ Consulta do PIB dos países por região (ordem alfabética). input: Região"""
    gdp = GDPRepository.find_by_region_name(db, region)
    if not gdp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Region name not found"
        )
    return GDPFromRegion.from_orm(gdp)


@app.get("/gdp/pib/rank/{period}", response_model=GDPFromPeriod)
def find_by_region(period: int, db: Session = Depends(get_db)):
    """○ Ranking dos 10 países (Nome e código) com maior e menor média de
    crescimento do PIB (GDP growth annual ) com o período sendo fornecido
    como parâmetro na API. input: Null"""
    gdp = GDPRepository.find_by_period(db, period)
    if not gdp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado"
        )
    return GDPFromPeriod.from_orm(gdp)
