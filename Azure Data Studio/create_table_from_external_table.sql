CREATE TABLE d_trotsenko_schema.fact_tripdata WITH (
        CLUSTERED COLUMNSTORE INDEX,
        DISTRIBUTION = HASH(trep_dropoff_datetime)
)  AS SELECT * FROM d_trotsenko_schema.trotsenko_external;