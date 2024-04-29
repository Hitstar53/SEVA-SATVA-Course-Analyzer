-- drop if exits
DROP TABLE IF EXISTS ENROLMENTS;
GO

-- create the table to contain enrolments data
CREATE TABLE ENROLMENTS
(
    ENROLMENT_ID INT IDENTITY(1,1) PRIMARY KEY,
    EMAIL VARCHAR(255) NOT NULL,
    NAME VARCHAR(300) NOT NULL,
    UID CHAR(10) NOT NULL,
    BRANCH VARCHAR(10) NOT NULL,
    SEM INT NOT NULL CHECK (SEM>=1 AND SEM<=8),
    COURSE VARCHAR(100) NOT NULL,
    CATEGORY VARCHAR(12) NOT NULL CHECK (CATEGORY IN('Intellectual', 'Social', 'Physical', 'Spiritual', 'Emotional')),
    PERIOD VARCHAR(20) NOT NULL
);
GO

-- create data source from the CSV blob file stored in Azure container
CREATE EXTERNAL DATA SOURCE MyAzureBlobStorage
WITH ( 
    TYPE = BLOB_STORAGE,
    LOCATION = 'https://devopiajkjsomaiyya.blob.core.windows.net/enrolments', 
);
GO

-- import the CSV file into this table
BULK INSERT ENROLMENTS 
FROM 'enrolments.csv' 
WITH (
    DATA_SOURCE = 'MyAzureBlobStorage',
    DATAFILETYPE = 'char',
    FIRSTROW=2,
    CODEPAGE = 65001,
    FIELDTERMINATOR=',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);