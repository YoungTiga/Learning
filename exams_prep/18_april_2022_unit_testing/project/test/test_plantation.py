from project.plantation import Plantation
from unittest import TestCase,main

class TestPlantation(TestCase):

    def setUp(self) -> None:
        self.plant = Plantation(1)

    def test_init(self):
        p = Plantation(1)
        self.assertEqual(1,p.size)
        self.assertEqual({},p.plants)
        self.assertEqual([],p.workers)

    def test_size_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.plant.size = -1
        self.assertEqual("Size must be positive number!",str(ex.exception))

    def test_size_setter_edge_case(self):
        self.plant.size=0
        self.assertEqual(0,self.plant.size)

    def test_hire_worker_error(self):
        self.plant.workers = ["Ivan"]
        with self.assertRaises(ValueError) as ex:
            self.plant.hire_worker("Ivan")
        self.assertEqual("Worker already hired!",str(ex.exception))

    def test_hire_worker_with_non_existing_worker(self):
        self.assertEqual([],self.plant.workers)
        res = self.plant.hire_worker("Ivan")
        self.assertEqual(["Ivan"],self.plant.workers)
        self.assertEqual("Ivan successfully hired.",res)

    def test_planting_error_non_existing_worker(self):
        with self.assertRaises(ValueError) as ex:
            self.plant.planting("Ivan","Flower")
        self.assertEqual("Worker with name Ivan is not hired!",str(ex.exception))

    def test_len_not_addition(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Martin')
        self.pl.hire_worker('Alexandra')
        self.pl.plants['Martin'] = ['Tomatoes']
        self.pl.plants['Alexandra'] = ['plant']
        self.assertEqual(self.pl.__len__(), 2)

    def test_planting_error_plantation_is_full(self):
        self.plant.workers = ["Ivan"]
        self.plant.plants = {"Ivan":["Flower1"]}
        with self.assertRaises(ValueError) as ex:
            self.plant.planting("Ivan","Flower2")
        self.assertEqual("The plantation is full!",str(ex.exception))

    def test_planting_worker_first_plant(self):
        self.plant.workers = ["Ivan"]
        res = self.plant.planting("Ivan","Flower1")
        self.assertEqual({"Ivan":["Flower1"]},self.plant.plants)
        self.assertEqual("Ivan planted it's first Flower1.",res)

    def test_planting_worker_next_plant(self):
        self.plant.size = 2
        self.plant.workers = ["Ivan"]
        self.plant.plants = {"Ivan": ["Flower1"]}
        res = res = self.plant.planting("Ivan","Flower2")
        self.assertEqual({"Ivan": ["Flower1","Flower2"]}, self.plant.plants)
        self.assertEqual("Ivan planted Flower2.", res)

    def test_len_dunder_method(self):
        self.plant.workers = ["Ivan"]
        self.plant.plants = {"Ivan": ["Flower1"]}
        self.assertEqual(1,len(self.plant))

    def test_repr_dunder_method(self):
        self.plant.workers = ["Ivan"]
        expected = 'Size: 1\n'
        expected += 'Workers: Ivan'
        self.assertEqual(expected,repr(self.plant))

    def test_str_dunder_method(self):
        self.plant.workers = ["Ivan"]
        self.plant.plants = {"Ivan":["Flower1"]}
        expected = "Plantation size: 1\n"
        expected += "Ivan\n"
        expected += "Ivan planted: Flower1"
        self.assertEqual(expected,str(self.plant))

if __name__ == "__main__":
    main()