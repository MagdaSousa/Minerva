from src.domains.models.income_groups.invome_groups import IncomeGroups


class TestIncomeGroups:

    def test_create_invome_groups(self):
        new_association = IncomeGroups(id=8,
                                       income_level=32,
                                       country_income_fk=90)
        assert isinstance(new_association, IncomeGroups)
