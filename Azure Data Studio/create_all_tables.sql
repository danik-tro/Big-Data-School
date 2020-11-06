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