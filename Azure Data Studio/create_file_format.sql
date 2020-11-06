-- ==========================================================================
-- Create external file format template for Azure SQL Data Warehouse Database
-- ==========================================================================
DROP EXTERNAL FILE FORMAT [trotsenko_format]
GO


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