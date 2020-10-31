import os
import uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    print("Azure Blob strorage v" + __version__ )
except Exception as ex:
    print("Exception:")
    print(ex)
