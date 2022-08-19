
CREATE database db_minerva;

CREATE TABLE Country (CountryID int identity,
                            CountryName varchar(50),
                            CountryCode varchar(3),
                            IncomeGroupID int,
                            PRIMARY KEY (CountryID),
      FOREIGN KEY (IncomeGroupID) REFERENCES IncomeGroups(IncomeGroupID));


CREATE TABLE Region (RegionID int identity,
                            RegionName varchar(50),
                            CountryID int,
                            PRIMARY KEY (RegionID),
    FOREIGN KEY (CountryID) REFERENCES Country(CountryID));



CREATE TABLE IncomeGroups (IncomeGroupID int identity,
                            IncomeGroupName varchar(50),
                            PRIMARY KEY (IncomeGroupID),
   );

CREATE TABLE Indicators (IndicatorID int identity,
                            IndicatorName varchar(50),
                            PRIMARY KEY (IndicatorID));


CREATE TABLE GDPGrowthAnnual (GDPGrowthAnnualID int identity,
                            GDPGrowthAnnualName varchar(50),
                            CountryID int,
                            IndicatorID int,
                            PRIMARY KEY (GDPGrowthAnnualID),
    FOREIGN KEY (CountryID) REFERENCES Country(CountryID),
    FOREIGN KEY (IndicatorID) REFERENCES Indicators(IndicatorID),
    FOREIGN KEY (PeriodID) REFERENCES Period(PeriodID));

CREATE TABLE Period (PeriodID int identity,
                            ResearchYear YEAR,
                            PRIMARY KEY (PeriodID));