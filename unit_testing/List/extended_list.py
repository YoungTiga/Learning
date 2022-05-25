class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)

import unittest

class TestIntegerList(unittest.TestCase):
    def test_if_initialized_correctly_without_arguments(self):
        integer = IntegerList()
        self.assertEqual([],integer._IntegerList__data)
    def test_if_initialized_correctly_with_arguments(self):
        integer = IntegerList(2,3,6)
        self.assertEqual([2,3,6], integer._IntegerList__data)

    def test_if_initialized_correctly_with_false_arguments(self):
        integer = IntegerList(2.4, "3", 5.2)
        self.assertEqual([],integer._IntegerList__data)

    def test_if_get_method_returns_correct_element(self):
        integer = IntegerList(2, 3, 6)
        self.assertEqual(2,integer.get(0))

    def test_if_get_method_raises_error_with_invalid_index(self):
        integer = IntegerList(2, 3, 6)
        with self.assertRaises(IndexError) as ex:
            integer.get(4)
        self.assertEqual("Index is out of range",str(ex.exception))

    def test_if_insert_method_works_correctly(self):
        integer = IntegerList(2, 3, 6)
        integer.insert(0,1)
        self.assertEqual([1,2,3,6],integer._IntegerList__data)

    def test_if_insert_method_will_throw_value_error_with_false_argument(self):
        integer = IntegerList(2, 3, 6)
        with self.assertRaises(ValueError) as ex:
            integer.insert(0, "1")
        self.assertEqual("Element is not Integer",str(ex.exception))
    def test_if_insert_method_will_throw_index_error_with_invalid_index(self):
        integer = IntegerList(2, 3, 6)
        with self.assertRaises(IndexError) as ex:
            integer.insert(3, 1)
        self.assertEqual("Index is out of range",str(ex.exception))
    def test_if_get_biggest_method_works_correctly(self):
        integer = IntegerList(2, 3, 6,-1,100,23)
        expected = 100
        res = integer.get_biggest()
        self.assertEqual(expected,res)

    def test_if_get_index_method_works_correctly(self):
        integer = IntegerList(2, 3, 6)
        self.assertEqual(1,integer.get_index(3))

    def test_if_add_method_works_correctly(self):
        integer = IntegerList(2, 3, 6)
        integer.add(7)
        self.assertEqual([2,3,6,7],integer._IntegerList__data)
    def test_if_add_method_throws_error_if_false_argument_given(self):
        integer = IntegerList(2, 3, 6)
        with self.assertRaises(ValueError) as ex:
            integer.add("7")
        self.assertEqual("Element is not Integer",str(ex.exception))

    def test_if_remove_index_method_works_correctly(self):
        integer = IntegerList(2, 3, 6)
        self.assertEqual(2,integer.remove_index(0))
        self.assertEqual([3,6],integer._IntegerList__data)

    def test_if_remove_index_method_throws_exception_with_invalid_index(self):
        integer = IntegerList(2, 3, 6)
        with self.assertRaises(IndexError) as ex:
            integer.remove_index(3)
        self.assertEqual("Index is out of range",str(ex.exception))


if __name__ == "__main__":
    unittest.main()