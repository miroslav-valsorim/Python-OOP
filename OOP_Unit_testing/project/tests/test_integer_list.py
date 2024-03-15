from unittest import TestCase, main
from project.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.integer_list = IntegerList("2", 1, "Gosho", 2, 3)

    def test_correct_initializing(self):
        self.assertEqual([1, 2, 3], self.integer_list._IntegerList__data)

    def test_get_data(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_with_none_integer_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add('100')
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_correct(self):
        result = self.integer_list.add(4)
        self.assertEqual(result, [1, 2, 3, 4])
        self.assertEqual(self.integer_list._IntegerList__data, [1, 2, 3, 4])

    def test_remove_index_index_value_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(5)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_correct(self):
        result = self.integer_list.remove_index(2)
        self.assertEqual([1, 2], self.integer_list._IntegerList__data)
        self.assertEqual(result, 3)

    def test_get_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(4)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_correct(self):
        result = self.integer_list.get(1)
        self.assertEqual(2, result)

    def test_insert_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(5, 4)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(2, "gosho")
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_correct_insert(self):
        self.integer_list.get_data().insert(3, 4)
        self.assertEqual([1, 2, 3, 4], self.integer_list._IntegerList__data)

    def test_biggest_number(self):
        result = self.integer_list.get_biggest()
        self.assertEqual(result, 3)

    def test_get_index(self):
        result = self.integer_list.get_index(2)
        self.assertEqual(1, result)

        
if __name__ == "__main__":
    main()