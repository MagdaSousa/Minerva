from src.ingestion.extract_and_transform import ExtractAndTransformDataSet
from src.ingestion.ingestion_old import IngestionInPostgres
from fastapi import status
from loguru import logger


def execution_load_to_postgres():
    try:
        data = ExtractAndTransformDataSet().processamento_para_database()
        ingestion_postgres = IngestionInPostgres(data)
        ingestion_postgres.iterate_in_rows_to_ingestion()
        return status.HTTP_200_OK

    except Exception as error:
        raise logger.error(f"[IngestionInPostgres] ERROR- Verify function to ingestion data{error}")


if __name__ == "__main__":
    # run to tests
    execution_load_to_postgres()
