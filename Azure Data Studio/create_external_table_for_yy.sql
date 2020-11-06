-- ====================================================================
-- Create External Table Template for Azure SQL Data Warehouse Database
-- ====================================================================

IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[d_trotsenko_schema].[trotsenko_external]') AND type in (N'U'))
DROP EXTERNAL TABLE [d_trotsenko_schema].[trotsenko_external]
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