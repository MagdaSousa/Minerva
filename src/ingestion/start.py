from src.ingestion.extract_and_transform import ExtractAndTransformDataSet
from src.ingestion.ingestion import IngestionInPostgres
from loguru import logger


def execution_load_to_postgres(db):
    try:
        data = ExtractAndTransformDataSet().processamento_para_database()
        ingestion_postgres = IngestionInPostgres(data, db)
        ingestion_postgres.iterate_in_rows_to_ingestion()
        return True

    except Exception as error:
        raise logger.error(f"[IngestionInPostgres] ERROR- Verify function to ingestion data{error}")
