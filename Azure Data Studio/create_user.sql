-- ========================================================================================
-- Create User as DBO template for Azure SQL Database and Azure SQL Data Warehouse Database
-- ========================================================================================
-- For login <login_name, sysname, login_name>, create a user in the database


CREATE USER d_trotsenko
	FOR LOGIN [d_trotsenko]
	WITH DEFAULT_SCHEMA = d_trotsenko_schema
GO