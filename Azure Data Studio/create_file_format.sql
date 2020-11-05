-- ==========================================================================
-- Create external file format template for Azure SQL Data Warehouse Database
-- ==========================================================================



CREATE EXTERNAL FILE FORMAT trotsenko_format WITH
(

	FORMAT_TYPE = DELIMITEDTEXT,
	FORMAT_OPTIONS
	(
		FIELD_TERMINATOR = N',',
		STRING_DELIMITER = N'',
		DATE_FORMAT = N'yyyy-MM-dd',
		USE_TYPE_DEFAULT = False
	)
)
GO