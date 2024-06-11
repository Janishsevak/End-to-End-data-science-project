import os
from src.logger.logging import logging
from src.exception.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_ingestion import DataIngestionConfig
from src.components.data_transformation import DataTransformation, DataTransformationConfig
import sys
from src.components.model_trainer import ModelTrainer,ModelTrainerConfig

if __name__ == "__main__":
    logging.info("The execution started")

    try:
          data_ingestion= DataIngestion()
          train_data_path,test_data_path = data_ingestion.initiate_data_ingestion()

          data_transformation=DataTransformation()
          train_arr,test_arr,_= data_transformation.initiate_data_transormation(train_data_path,test_data_path)

          model_trainer=ModelTrainer()
          print(model_trainer.initiate_model_trainer(train_arr,test_arr))

    except Exception as e:

        logging.info("Custome Exception")
        raise CustomException(e,sys)