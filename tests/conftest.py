import pytest

response = [
    200,
    {
        "country_name": "Ukraine",
        "country_code": "UKR",
        "region_name": "Europe & Central Asia",
        "indicator_name": "GDP growth (annual %)",
        "list_values_indicators": [
            {
                "1991": -8.7,
                "1992": -9.9,
                "1993": -14.2,
                "1994": -22.9,
                "1995": -12.2,
                "1996": -10.0,
                "1997": -3.0,
                "1998": -1.9,
                "1999": -0.2,
                "2000": 5.9,
                "2001": 8.8,
                "2002": 5.34,
                "2003": 9.52,
                "2004": 11.8,
                "2005": 3.07,
                "2006": 7.57,
                "2007": 8.22,
                "2008": 2.24,
                "2009": -15.14,
                "2010": 4.09,
                "2011": 5.45,
                "2012": 0.15,
                "2013": 0.05,
                "2014": -10.08,
                "2015": -9.77,
                "2016": 2.44,
                "2017": 2.36,
                "2018": 3.49,
                "2019": 3.2,
                "2020": -3.75,
                "2021": 3.4,
                "1960": 0,
                "1961": 0,
                "1962": 0,
                "1963": 0,
                "1964": 0,
                "1965": 0,
                "1966": 0,
                "1967": 0,
                "1968": 0,
                "1969": 0,
                "1970": 0,
                "1971": 0,
                "1972": 0,
                "1973": 0,
                "1974": 0,
                "1975": 0,
                "1976": 0,
                "1977": 0,
                "1978": 0,
                "1979": 0,
                "1980": 0,
                "1981": 0,
                "1982": 0,
                "1983": 0,
                "1984": 0,
                "1985": 0,
                "1986": 0,
                "1987": 0,
                "1988": 2.57,
                "1989": 3.87,
                "1990": -6.35
            }
        ]
    }
]


@pytest.fixture
def response_api():
    return response
