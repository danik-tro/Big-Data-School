CREATE DATABASE SCOPED CREDENTIAL AzureStorageCredentialTrotsenko
    WITH
        IDENTITY = 'bds01tro',
        SECRET = 'jnbr6t4qlKDnIUTZVtJItkO9osoTZVsnCuPp+BEzB/1zYOu/VXwSr36L4ZaJGCFm+qkTGPn54nXpFE+M+0At8Q=='
		GO

CREATE EXTERNAL DATA SOURCE trotsenko_ext WITH (
    LOCATION = 'wasbs://trotsenkodaniil01@bds01tro.blob.core.windows.net',
    CREDENTIAL = AzureStorageCredentialTrotsenko,
	TYPE = HADOOP
)