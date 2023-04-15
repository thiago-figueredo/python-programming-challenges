from main import splice
from unittest import main, TestCase


def remove_element(lst, i):
    return lst[:i] + lst[i+1:]


class TestSplice(TestCase):
    list = [1, 2, 3]

    def test_returns_an_empty_list_when_start_is_negative(self):
        self.assertEqual(splice(self.list, -1, 1), [])

    def test_returns_an_empty_list_when_start_is_equal_to_list_length(self):
        self.assertEqual(splice(self.list, len(self.list), 1), [])

    def test_returns_an_empty_list_when_start_is_greater_than_list_length(self):
        self.assertEqual(splice(self.list, 0, len(self.list) + 1), [])

    def test_returns_an_empty_list_when_count_is_negative(self):
        self.assertEqual(splice(self.list, 3, -1), [])

    def test_returns_an_empty_list_when_count_is_equal_to_list_length(self):
        self.assertEqual(splice(self.list, 3, len(self.list)), [])

    def test_returns_an_empty_list_when_count_is_greater_than_list_length(self):
        self.assertEqual(splice(self.list, 3, len(self.list) + 1), [])

    def test_slices_all_the_list(self):
        self.assertEqual(splice(self.list, 0, len(self.list)), self.list)

    def test_slices_one_element(self):
        for i in range(len(self.list)):
            self.assertEqual(splice(self.list, i, 1), [self.list[i]])

    def test_slices_any_valid_index(self):
        for i in range(len(self.list)):
            expected_list = self.list

            if i == 1:
                expected_list = [self.list[1], self.list[2]]
            elif i == len(self.list) - 1:
                expected_list = []

            count = len(self.list) - i
            self.assertEqual(
                splice(self.list, i, count),
                expected_list if count != 1 else [self.list[i]]
            )


if __name__ == '__main__':
    main()
