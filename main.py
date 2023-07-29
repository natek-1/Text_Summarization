from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"

try:
    """ logger.info(f"\n\n{'>'*10} {STAGE_NAME}  started {'<'*10}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{'>'*10} {STAGE_NAME} completed {'<'*10} \n\n x{'='*20}x \n\n")
    STAGE_NAME = 'Data Validation stage'
    logger.info(f"\n\n{'>'*10} {STAGE_NAME}  started {'<'*10}")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"{'>'*10} {STAGE_NAME} completed {'<'*10} \n\n x{'='*20}x \n\n")
    STAGE_NAME = 'Data Transformation  stage'
    logger.info(f"\n\n {'>'*10} {STAGE_NAME}  started {'<'*10}")
    data_transformation= DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"{'>'*10} {STAGE_NAME} completed {'<'*10} \n\n x{'='*20}x")
    STAGE_NAME = 'Model Training  stage'
    logger.info(f"\n\n {'>'*10} {STAGE_NAME}  started {'<'*10}")
    model_trainer= ModelTrainer()
    model_trainer.main()
    logger.info(f"{'>'*10} {STAGE_NAME} completed {'<'*10} \n\n x{'='*20}x") """
    STAGE_NAME = 'Model Evaluation  stage'
    logger.info(f"\n\n {'>'*10} {STAGE_NAME}  started {'<'*10}")
    model_eval= ModelEvaluationTrainingPipeline()
    model_eval.main()
    logger.info(f"{'>'*10} {STAGE_NAME} completed {'<'*10} \n\n x{'='*20}x")
except Exception as e:
    logger.exception(e)
    raise e