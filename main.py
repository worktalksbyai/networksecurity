from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import (TrainingPipelineConfig,
                                                  DataIngestionConfig,
                                                  DataValidationConfig,
                                                  DataTransformationConfig)

import sys
from datetime import datetime

if __name__=="__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig(datetime.now())
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
        datavalidataionconfig = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, datavalidataionconfig)
        logging.info("Initiate data validation")
        datavalidationartifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(datavalidationartifact)
        datatransformationconfig = DataTransformationConfig(trainingpipelineconfig)
        logging.info("Initiate data Transformation")
        datatransformation = DataTransformation(datavalidationartifact, datatransformationconfig)
        datatransformationartifact = datatransformation.initiate_data_transformation()
        logging.info("Data Transformation Completed")
        print(datatransformationartifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)