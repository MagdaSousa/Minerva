CREATE TABLE IncomeGroups (IncomeGroupID int GENERATED ALWAYS AS IDENTITY,
                            IncomeGroupName varchar(50),
                            PRIMARY KEY (IncomeGroupID));

CREATE TABLE Region (RegionID int GENERATED ALWAYS AS IDENTITY,
                            RegionName varchar(50),
                            IncomeGroupID int,
                            PRIMARY KEY (RegionID),
    FOREIGN KEY (IncomeGroupID) REFERENCES IncomeGroups(IncomeGroupID));

CREATE TABLE Country (CountryID int GENERATED ALWAYS AS IDENTITY,
                            CountryName varchar(50),
                            CountryCode varchar(3),
                            IncomeGroupID int,
                            PRIMARY KEY (CountryID),
      FOREIGN KEY (IncomeGroupID) REFERENCES IncomeGroups(IncomeGroupID));

CREATE TABLE CountryIndicators(
                            CountryID int,
                            IndicatorID int,
 FOREIGN KEY (IndicatorID) REFERENCES Indicators(IndicatorID),
 FOREIGN KEY (CountryID) REFERENCES Country(CountryID));


CREATE TABLE Indicators(IndicatorID int GENERATED ALWAYS AS IDENTITY,
                            IndicatorName varchar(50),
                            IndicatorCode varchar(50),
                            PRIMARY KEY (IndicatorID));

CREATE TABLE PeriodIndicators(
                            PeriodID int,
                            IndicatorID int);


CREATE TABLE Period (PeriodID int GENERATED ALWAYS AS IDENTITY,
                            ResearchYear DATE,
                            PRIMARY KEY (PeriodID));



CREATE TABLE GDPGrowthAnnual (GDPGrowthAnnualID int GENERATED ALWAYS AS IDENTITY,
                            GDPGrowthAnnualName varchar(50),
                            CountryID int,
                            IndicatorID int,
                            PeriodID int,
                            ValueperPeriod float,
                            PRIMARY KEY (GDPGrowthAnnualID),
    FOREIGN KEY (CountryID) REFERENCES Country(CountryID),
    FOREIGN KEY (IndicatorID) REFERENCES Indicators(IndicatorID),
    FOREIGN KEY (PeriodID) REFERENCES Period(PeriodID));

