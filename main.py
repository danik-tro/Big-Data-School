import os
import logging

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


def logging_name_function(func):
    def wrap(*args, **kwargs):
        logging.info(f"{func.__name__} has been started")
        func(*args)
        logging.info(f"{func.__name__} has been finished")
    return wrap


class BdsBlob:
    logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO,
                        filename='BDS.log',
                        filemode='w')
    blob_service_client: BlobServiceClient
    container_client: ContainerClient
    blob_client: BlobClient

    def __init__(self, connection_string, container_name_="trotsenkodaniil", file_name_='IndianFoodDatasetCSV.csv'):
        logging.info("Init started")

        self.connection_str = connection_string
        self.container_name = container_name_
        self.file_name = file_name_

        logging.info("Init finished")

    def upload_file(self):
        logging.info("upload_file has been started")

        self.blob_client = self.blob_service_client.get_blob_client(container=self.container_name,
                                                                    blob=self.file_name)
        logging.info("upload_file has been finished")

    def create_container(self):
        logging.info("create_container has been started")

        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_str)
        self.container_client = self.blob_service_client.create_container(self.container_name)

        logging.info("create_container has been finished")

    def upload_blob(self):
        logging.info("upload_blob has been finished")

        with open(self.file_name, 'rb') as data:
            self.blob_client.upload_blob(data)

        logging.info("upload_blob has been finished")

    def task(self):
        logging.info("task has been started")

        try:
            self.create_container()
        except Exception as ex:
            logging.error("Exception occurred in create_container", exc_info=True)

        try:
            self.upload_file()
        except Exception as ex:
            logging.error("Exception occurred in upload_file", exc_info=True)

        try:
            self.upload_blob()
        except Exception as ex:
            logging.error("Exception occurred in upload_blob", exc_info=True)

        logging.info("task has been finished")

    @logging_name_function
    def get_containers(self):
        try:
            all_containers = self.blob_service_client.list_containers(include_metadata=True)
            for container in all_containers:
                print(container['name'], container['metadata'])
        except Exception as ex:
            logging.error("Exception occurred in get_containers", exc_info=True)


'''AZURE_STORAGE_CONNECTION_STRING'''
'''AZURE_STORAGE_CONNECTION_BDS'''
'''AZURE_STORAGE_CONNECT_STRING'''


def main():
    connect_str = os.getenv('AZURE_STORAGE_CONNECT_STRING')
    bds = BdsBlob(connect_str, container_name_="trotsenkodaniil")
    bds.task()
    bds.get_containers()


if __name__ == "__main__":
    main()
