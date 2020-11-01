import os

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


class BDS_Blob_Upload:
    def __init__(self, conection_string):
        pass


connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
print(connect_str)

try:
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_name = "trotsenkodaniil01"
    container_client = blob_service_client.create_container(container_name)
except Exception:
    print("Container had been created already.")

try:
    file_name = "hashed_feature.csv"
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

    with open(file_name, 'rb') as data:
        blob_client.upload_blob(data)
except Exception:
    print("File had been uploaded already.")

