# testes- coletar os países e fazer a média
from src.database.database import DBConnection
from src.domains.models.association_tables.association_tables import Association
from src.domains.models.indicators.Gross_domestic_product import GrossDomesticProduct
from src.domains.models.period.period import Period

obj_connection = DBConnection()
engine = obj_connection.engine
get_db = obj_connection.get_db()


class TestRoutes:
    def __init__(self):
        pass

    def test_coletar_periodo(self):
        final_period = 1989
        initial_period = 1995

        # coletando o período
        result = get_db.query(Period).filter(initial_period <= Period.research_year <= final_period).first()

        print(result)

    # associations = get_db().query(GrossDomesticProduct).filter(Association.id == 1).first()

    # print(associations.gdp_association_fk)


TestRoutes().test_coletar_período()
