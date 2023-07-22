from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.logging import logger


class DataTransformationTrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_tranformation_config = config.get_data_transformation_config()
            data_tranformation = DataTransformation(config=data_tranformation_config)
            data_tranformation.convert()
        except Exception as e:
            raise e


