class TestPerson:
    def test_new_person(self, person):
        assert person.inn
        assert person.name

    def test_inn_person(self, person, another_person):
        assert person.inn != another_person.inn
