from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):

    def setUp(self) -> None:
        self.pet = PetShop("S")
        self.pet.pets = ["Ivan"]
        self.pet.food = {"Hrana": 100}

    def test_init(self):
        name = "Gosho"
        pet = PetShop(name)
        self.assertEqual(name, pet.name)
        self.assertEqual({}, pet.food)
        self.assertEqual([], pet.pets)

    def test_add_food_throw_error_if_quantity_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.pet.add_food("S", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_throw_error_if_quantity_les_than_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.pet.add_food("S", -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_successfully(self):
        name = "Whizkaz"
        quantity = 10
        self.pet.add_food(name,quantity)
        res = self.pet.add_food(name,5)
        self.assertEqual(15,self.pet.food[name])
        self.assertEqual("Successfully added 5.00 grams of Whizkaz.",res)

    def test_add_pet_throws_error_if_name_existing(self):
        with self.assertRaises(Exception) as ex:
            self.pet.add_pet("Ivan")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_adds_non_existing_pet(self):
        res = self.pet.add_pet("Gosho")
        self.assertEqual(["Ivan", "Gosho"], self.pet.pets)
        self.assertEqual("Successfully added Gosho.",res)

    def test_feed_pet_throws_error_invalid_pet_name(self):
        with self.assertRaises(Exception) as ex:
            self.pet.feed_pet("Wizkaz", "Gosho")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_food_if_food_is_non_existan(self):
        res = self.pet.feed_pet("Whizkaz", "Ivan")
        self.assertEqual('You do not have Whizkaz', res)

    def test_food_method_if_food_quantity_is_less_than_onehundred(self):
        self.pet.food["Hrana"] = 65
        res = self.pet.feed_pet("Hrana", "Ivan")
        self.assertEqual("Adding food...", res)
        self.assertEqual(1065, self.pet.food["Hrana"])

    def test_food_method_if_food_quantity_is_at_least_onehundred(self):
        res = self.pet.feed_pet("Hrana", "Ivan")
        self.assertEqual("Ivan was successfully fed", res)
        self.assertEqual(0, self.pet.food["Hrana"])

    def test_repr_method(self):
        self.pet.pets.append("Sasho")
        expected = 'Shop S:\n' \
                   'Pets: Ivan, Sasho'
        self.assertEqual(expected, repr(self.pet))


if __name__ == "__main__":
    main()
