from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

# Models
from src.domains.models.country.country import Country
from src.domains.models.indicators.Gross_domestic_product import GrossDomesticProduct
from src.domains.models.indicators.indicator_base import Indicator
from src.domains.models.country.region import Region

# Repositories
from src.domains.repository.country_repository.country_repopsitory import CountryRepository
from src.domains.repository.country_repository.region_repository import RegionRepository
from src.domains.repository.indicator_repository.cross_domestic_product_repository import GDPRepository
from src.domains.repository.indicator_repository.indicator_repository import IndicatorRepository

from database import engine, Base, get_db
from schemas import CursoRequest, CursoResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()
