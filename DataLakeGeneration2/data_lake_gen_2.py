from azure.storage.filedatalake import DataLakeServiceClient
import logging
import os

def logging_name_function(func):
    def wrap(*args, **kwargs):
        logging.info(f"{func.__name__} has been started")
        func(*args)
        logging.info(f"{func.__name__} has been finished")
    return wrap


class DataLakeG2:
    logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO,
                        filename='BDS.log',
                        filemode='w')

    def __init__(self, connection_string=os.getenv("AZURE_DT_2"),
                 container_name_="container01",
                 file_name_='IndianFoodDatasetCSV.csv'):
        self.dt_service = DataLakeServiceClient.from_connection_string(connection_string)
        self.file_system_name = container_name_
        self.file_name = file_name_

    def create_file_system(self):
        """
            Create file system(Container)
        """

        self.file_system_client = self.dt_service.create_file_system(file_system=self.file_system_name)
