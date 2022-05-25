# from project.train.train import Train
from project.train.train import Train
from unittest import TestCase,main

class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train = Train("T", 5)

    def test_init(self):
        name = "T"
        capacity = 10
        train = Train(name,capacity)
        self.assertEqual(name,train.name)
        self.assertEqual(capacity,train.capacity)
        self.assertEqual([],train.passengers)

    def test_add_method_throws_error_if_not_enough_capacity(self):
        self.train.passengers = ["Ivan","Petyr","Kolio","Stenli","Mariq"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("Petq")
        self.assertEqual("Train is full",str(ex.exception))
        self.assertEqual(["Ivan","Petyr","Kolio","Stenli","Mariq"],self.train.passengers)

    def test_add_method_if_passenger_already_in_passengers_list(self):
        self.train.passengers = ["Ivan","Petyr","Kolio","Stenli"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("Ivan")

        self.assertEqual("Passenger Ivan Exists",str(ex.exception))
        self.assertEqual(["Ivan","Petyr","Kolio","Stenli"],self.train.passengers)

    def test_add_method_works_correctly_with_correct_input(self):
        res = self.train.add("Ivan")

        self.assertEqual("Added passenger Ivan",res)
        self.assertEqual(["Ivan"],self.train.passengers)

    def test_remove_method_throws_error_with_non_existing_passenger(self):
        self.train.passengers = ["Ivan","Mariq"]
        with self.assertRaises(ValueError) as ex:
            self.train.remove("Gosho")
        self.assertEqual("Passenger Not Found",str(ex.exception))
        self.assertEqual(["Ivan","Mariq"],self.train.passengers)

    def test_remove_method_works_correctly_with_valid_input(self):
        self.train.passengers = ["Ivan", "Mariq"]
        res = self.train.remove("Ivan")
        self.assertEqual("Removed Ivan",res)
        self.assertEqual(["Mariq"],self.train.passengers)

if __name__=="__main__":
    main()