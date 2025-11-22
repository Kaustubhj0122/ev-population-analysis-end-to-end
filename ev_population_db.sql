CREATE DATABASE ev_population_db;
USE ev_population_db;
CREATE TABLE ev_population (
    VIN_10 VARCHAR(15),
    County VARCHAR(50),
    City VARCHAR(50),
    State VARCHAR(50),
    Postal_Code VARCHAR(10),
    Model_Year INT,
    Make VARCHAR(50),
    Model VARCHAR(100),
    Electric_Vehicle_Type VARCHAR(50),
    CAFV_Eligibility VARCHAR(100),
    Electric_Range INT,
    Base_MSRP FLOAT,
    Legislative_District INT,
    DOL_Vehicle_ID BIGINT,
    Vehicle_Location VARCHAR(100),
    Electric_Utility VARCHAR(100),
    Census_Tract VARCHAR(50),
    Vehicle_Age INT,
    Battery_Capacity VARCHAR(50)
);
-- Count EVs by Make
SELECT Make, COUNT(*) AS Total_EVs
FROM ev_population
GROUP BY Make
ORDER BY Total_EVs DESC
LIMIT 15;

--  Average Range by Make
SELECT Make, AVG(`Electric Range`) AS Avg_Range
FROM ev_population
GROUP BY Make
ORDER BY Avg_Range DESC;

--  EV Adoption by County
SELECT County, COUNT(*) AS EV_Count
FROM ev_population
GROUP BY County
ORDER BY EV_Count DESC;

--  CAFV Eligibility Impact
SELECT CAFV_Eligibility, COUNT(*) AS Count
FROM ev_population
GROUP BY CAFV_Eligibility;

-- Find count of veicles age as  per the brand
SELECT Make,
       CASE
           WHEN `Vehicle_Age (years)` <= 3 THEN 'New (0-3)'
           WHEN `Vehicle_Age (years)` BETWEEN 4 AND 10 THEN 'Moderate (4-10)'
           ELSE 'Old (11+)'
       END AS Age_Group,
       COUNT(*) AS Vehicle_Count
FROM ev_population
GROUP BY Make, Age_Group
ORDER BY Make, Age_Group;

-- Idetify Maximum and Minimum value of each make
SELECT Make,
       MIN(`Base MSRP`) AS Min_MSRP,
       MAX(`Base MSRP`) AS Max_MSRP
      
FROM ev_population
GROUP BY Make
ORDER BY Make;




