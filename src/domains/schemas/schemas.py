import pandas as pd


# Actions
class GDPResponseSchema:
    def __init__(self, data):
        self.data = data

    def assemble_the_schematic_for_the_indicator(self):
        dict_values_indicators = {}

        gdp = self.data[0]
        country = self.data[1]
        indicators = self.data[2]
        for fields in gdp:

            if str(fields.value_per_period) == 'nan':
                values_per_period = 0
            else:
                values_per_period = round(fields.value_per_period, 2)
            dict_values_indicators[fields.gdp_period_fk.research_year] = values_per_period

        return {"country_name": country.country_name,
                "country_code": country.country_code,
                "region_name": country.region_country_fk.region_name,
                "indicator_name": indicators[0].indicator_name,
                "list_values_indicators": [dict_values_indicators]}


class GrossRateResponseSchema:
    def __init__(self, data):
        self.data = data

    def formatting_growth_rate_data_by_country(self):
        dict_values_indicators = {}

        gdp = self.data[0]
        country = self.data[1]
        for fields in gdp:

            if str(fields.value_per_period) == 'nan':
                values_per_period = 0
            else:
                values_per_period = round(fields.value_per_period, 2)
            dict_values_indicators[fields.gdp_period_fk.research_year] = f"{round(values_per_period)} %"

        return {"country_name": country.country_name,
                "country_code": country.country_code,
                "GDP growth annual %": [dict_values_indicators]}


class GrossRateByRegionSchema:
    def __init__(self, data):
        self.data = data

    def formatting_growth_rate_data_by_country(self):
        dict_values_indicators = {}
        dict_region = {}
        list_grouth_by_region = []
        regions_infos = self.data[0]
        gdp_by_country = self.data[1]
        country_infos = self.data[2]

        dict_region["Region"] = regions_infos.region_name

        for country, gpd in zip(country_infos, gdp_by_country):
            for fields in gpd:

                if str(fields.value_per_period) == 'nan':
                    values_per_period = 0
                else:
                    values_per_period = round(fields.value_per_period, 2)
                dict_values_indicators[fields.gdp_period_fk.research_year] = f"{round(values_per_period)} %"
            list_grouth_by_region.append(dict_values_indicators)

            dict_region[country.country_name] = {"GDP growth annual %": list_grouth_by_region}
            list_grouth_by_region = []
            dict_values_indicators = {}

        return dict_region


class PeriodRangeMeanSchema:
    def __init__(self, data):
        self.data = data

    def calculate_the_average_GDP_rate_by_country(self):
        df = pd.DataFrame(self.data, columns=['Country_name', 'avarage', 'country_id', 'association_id'])
        return {"highest average": df.nlargest(10, 'avarage')[['Country_name', 'avarage']].to_dict()}
