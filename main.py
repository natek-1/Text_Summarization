from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"{'>'*10} {STAGE_NAME}  started {'<'*10}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{'>'*10} {STAGE_NAME} completed {'<'*10} \n\n x{'='*20}x")
except Exception as e:
    logger.exception(e)
    raise e