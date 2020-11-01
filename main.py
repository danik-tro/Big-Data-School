import os

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


class BDS:
    blob_service_client: BlobServiceClient
    container_client: ContainerClient
    blob_client: BlobClient

    def __init__(self, connection_string, container_name_="trotsenkodaniil", file_name_='IndianFoodDatasetCSV.csv'):
        self.connection_str = connection_string
        self.container_name = container_name_
        self.file_name = file_name_

    def upload_file(self):
        self.blob_client = self.blob_service_client.get_blob_client(container=self.container_name,
                                                                    blob=self.file_name)

    def create_container(self):
        print("Being creating container")
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_str)
        self.container_client = blob_service_client.create_container(container_name)
        print("Has been created container")

    def upload_blob(self):
        with open(self.file_name, 'rb') as data:
            self.blob_client.upload_blob(data)


#connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
#connect_str_bds = os.getenv('AZURE_STORAGE_CONNECTION_BDS')
connect_str = os.getenv(('AZURE_STORAGE_CONNECT_STRING'))
print(connect_str)

try:
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_name = "trotsenkodaniil02"
    container_client = blob_service_client.create_container(container_name)
except Exception as ex:
    print("Container had been created already.")
    print(ex)

try:
    file_name = "hashed_feature.csv"
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

    with open(file_name, 'rb') as data:
        blob_client.upload_blob(data)
except Exception as ex:
    print("File had been uploaded already.")
    print(ex)

