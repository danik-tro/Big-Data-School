# Homework
> ****Full script in full_script.sql****

## 3. Create User and Schema
````
CREATE LOGIN d_trotsenko
	WITH PASSWORD = '****'
GO

CREATE SCHEMA d_trotsenko_schema
GO

CREATE USER d_trotsenko
	FOR LOGIN [d_trotsenko]
	WITH DEFAULT_SCHEMA = d_trotsenko_schema
GO

EXEC sp_addrolemember N'db_owner', N'd_trotsenko'
GO
````
## 5-6. Create External Data Source and External Data Table
````
CREATE DATABASE SCOPED CREDENTIAL AzureStorageCredentialTrotsenko
    WITH
        IDENTITY = 'AzureStorageAccount',
        SECRET = 'AccountKeys'
		GO

CREATE EXTERNAL DATA SOURCE trotsenko_ext WITH (
    LOCATION = 'wasbs://trotsenkodaniil01@bds01tro.blob.core.windows.net',
    CREDENTIAL = AzureStorageCredentialTrotsenko,
	TYPE = HADOOP
)

CREATE EXTERNAL FILE FORMAT trotsenko_format WITH
(

	FORMAT_TYPE = DE    LIMITEDTEXT,
	FORMAT_OPTIONS
	(
		FIELD_TERMINATOR = N',',
		FIRST_ROW = 2,
		STRING_DELIMITER = N'',
		DATE_FORMAT = N'yyyy-MM-dd HH:mm:ss',
		USE_TYPE_DEFAULT = False
	)
)
GO

CREATE EXTERNAL TABLE d_trotsenko_schema.trotsenko_external (
    VendorID INT,
    trep_pickup_datetime DATETIME2(0),
    trep_dropoff_datetime DATETIME2(0),
    passenger_count INT,
    trip_distance REAL,
    RatecodeID INT ,
    store_and_fwd_flag VARCHAR(2),
    PULocationID INT,
    DOLocationID INT,
    payment_type INT,
    fare_amount REAL,
    extra REAL,
    mta_tax REAL,
    tip_amount REAL,
    tolls_amount REAL,
    improvement_surcharge REAL,
    total_amount REAL,
    congestion_surcharge REAL
) WITH (
    LOCATION='yellow_tripdata_2020-01.csv',
    DATA_SOURCE=trotsenko_ext,
    FILE_FORMAT=trotsenko_format
);
````

# 7. Upload the data from external table
````
CREATE TABLE d_trotsenko_schema.fact_tripdata WITH (
        CLUSTERED COLUMNSTORE INDEX,
        DISTRIBUTION = HASH(trep_dropoff_datetime)
)  AS SELECT * FROM d_trotsenko_schema.trotsenko_external;
````

# 8. Create table Vendor, RateCode, PaymentType and script for filling
````
CREATE TABLE [d_trotsenko_schema].[Vendor] WITH (
    DISTRIBUTION = ROUND_ROBIN
) AS
SELECT [VendorID] AS ID
FROM [d_trotsenko_schema].[trotsenko_external]
WHERE [VendorID] IS NOT NULL
GROUP BY [VendorID];


ALTER TABLE [d_trotsenko_schema].[Vendor] ADD Name VARCHAR(255);

UPDATE [d_trotsenko_schema].[Vendor]
SET [Name] = N'Creative Mobile Technologies, LLC'
WHERE [ID] = 1;
GO

UPDATE [d_trotsenko_schema].[Vendor]
SET [Name] = N'VeriFone Inc'
WHERE [ID] = 2;



CREATE TABLE [d_trotsenko_schema].[RateCode] WITH (
    DISTRIBUTION = ROUND_ROBIN
) AS
SELECT [RatecodeID] AS ID
FROM [d_trotsenko_schema].[trotsenko_external]
WHERE [RatecodeID] IS NOT NULL
GROUP BY [RatecodeID];


ALTER TABLE [d_trotsenko_schema].[RateCode] ADD Name VARCHAR(255);

UPDATE [d_trotsenko_schema].[RateCode]
SET [Name] = N'Standard rate'
WHERE [ID] = 1;
GO

UPDATE [d_trotsenko_schema].[RateCode]
SET [Name] = N'JFK'
WHERE [ID] = 2;
GO

UPDATE [d_trotsenko_schema].[RateCode]
SET [Name] = N'Newark'
WHERE [ID] = 3;
GO

UPDATE [d_trotsenko_schema].[RateCode]
SET [Name] = N'Nassau or Westchester'
WHERE [ID] = 4;
GO

UPDATE [d_trotsenko_schema].[RateCode]
SET [Name] = N'Negotiated fare'
WHERE [ID] = 5;
GO

UPDATE [d_trotsenko_schema].[RateCode]
SET [Name] = N'Group ride'
WHERE [ID] = 6;
GO



CREATE TABLE [d_trotsenko_schema].[Payment_type] WITH (
    DISTRIBUTION = ROUND_ROBIN
) AS
SELECT [payment_type] AS ID
FROM [d_trotsenko_schema].[trotsenko_external]
WHERE [payment_type] IS NOT NULL
GROUP BY [payment_type];


ALTER TABLE [d_trotsenko_schema].[Payment_type] ADD Name VARCHAR(255);

UPDATE [d_trotsenko_schema].[Payment_type]
SET [Name] = N'Credit card'
WHERE [ID] = 1;
GO

UPDATE [d_trotsenko_schema].[Payment_type]
SET [Name] = N'Cash'
WHERE [ID] = 2;
GO

UPDATE [d_trotsenko_schema].[Payment_type]
SET [Name] = N'No charge'
WHERE [ID] = 3;
GO

UPDATE [d_trotsenko_schema].[Payment_type]
SET [Name] = N'Dispute'
WHERE [ID] = 4;
GO

UPDATE [d_trotsenko_schema].[Payment_type]
SET [Name] = N'Unknown'
WHERE [ID] = 5;
GO

UPDATE [d_trotsenko_schema].[Payment_type]
SET [Name] = N'Voided trip'
WHERE [ID] = 6;
GO

INSERT INTO d_trotsenko_schema.Payment_type VALUES (6, N'Voided trip');
````