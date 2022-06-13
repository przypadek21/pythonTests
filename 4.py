import pytest

def sort_by(names, first_letter=False, last_letter=False, lenght=False):
    if first_letter:
        names.sort()

    if last_letter:
        names.sort(key=lambda name: name[::-1])

    if lenght:
        names.sort(key=len)

    return names

class TestSort:
    @pytest.fixture
    def names(self):
        return ['Alina', 'Ewa', 'Paulina', 'Maciej']

    def test_sort(self, names):
        # when
        sorted_names = sort_by(names, first_letter=True)

        # then
        assert sorted_names == ['Alina', 'Ewa', 'Maciej', 'Paulina']

    def test_revers_sort(self, names):

        # when
        sorted_names = sort_by(names, last_letter=True)

        # then
        assert sorted_names == ['Alina', 'Paulina', 'Ewa', 'Maciej']

    def test_lenght_sort(self, names):

        # when
        sorted_names = sort_by(names, lenght=True)

        # then
        assert sorted_names == ['Ewa', 'Alina', 'Maciej', 'Paulina']