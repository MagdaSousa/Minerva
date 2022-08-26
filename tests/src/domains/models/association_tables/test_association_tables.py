
from src.domains.models.association_tables.association_tables import Association

class TestAssociation:

    def test_create_association(self):
        new_association = Association(id=1,
                                      country_id=5,
                                      indicators_id=6,
                                      gdp_association_fk=54)
        assert isinstance(new_association,Association)