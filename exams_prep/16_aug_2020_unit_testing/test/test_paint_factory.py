from project.factory.paint_factory import PaintFactory

from unittest import TestCase,main

class TestPaintFactory(TestCase):

    def setUp(self) -> None:
        self.f = PaintFactory("F",10)

    def test_init(self):
        f = PaintFactory("F",10)
        self.assertEqual("F",f.name)
        self.assertEqual(10,f.capacity)

    def test_add_ingridient_error_invalid_ingredient(self):
        with self.assertRaises(TypeError) as ex:
            self.f.add_ingredient("yellowish",10)

        self.assertEqual("Ingredient of type yellowish not allowed in PaintFactory",str(ex.exception))

    def test_add_ingredient_error_not_enough_space(self):
        self.f.capacity = 0
        with self.assertRaises(ValueError) as ex:
            self.f.add_ingredient("yellow",5)
        self.assertEqual("Not enough space in factory",str(ex.exception))

    def test_add_ingredient_correct_ingredient_enough_space(self):
        self.f.add_ingredient("yellow",5)
        self.assertEqual({"yellow":5},self.f.ingredients)

    def test_remove_ingredient_error_if_ingredient_not_in_ingredients(self):
        self.f.ingredients = {"yellow":5}
        with self.assertRaises(KeyError) as ex:
            self.f.remove_ingredient("yellowish",5)
        self.assertEqual("'No such ingredient in the factory'",str(ex.exception))

    def test_remove_remove_ingredient_error_if_quantity_greater_than_the_ingredient(self):
        self.f.ingredients = {"yellow":5}
        with self.assertRaises(ValueError) as ex:
            self.f.remove_ingredient("yellow",6)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_correctly(self):
        self.f.ingredients = {"yellow": 5}
        self.f.remove_ingredient("yellow",4)
        self.assertEqual({"yellow": 1},self.f.ingredients)

    def test_remove_ingredient_correctly_edge(self):
        self.f.ingredients = {"yellow": 5}
        self.f.remove_ingredient("yellow",5)
        self.assertEqual({"yellow": 0},self.f.ingredients)

    def test_products(self):
        self.f.ingredients = {"yellow": 5}
        self.assertEqual({"yellow": 5},self.f.products)


if __name__ == "__main__":
    main()