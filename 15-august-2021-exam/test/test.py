from unittest import TestCase

from project.pet_shop import PetShop


class PetShopTest(TestCase):
    NAME = "TEST_ZOO"

    def setUp(self) -> None:
        self.petshop = PetShop(self.NAME)

    def test_is_initialized_correct(self):
        self.assertEqual(self.NAME, self.petshop.name)
        self.assertEqual({}, self.petshop.food)
        self.assertEqual([], self.petshop.pets)

    def test_add_food_with_negative_or_zero_quantity_rises(self):
        with self.assertRaises(ValueError) as error:
            self.petshop.add_food("Test Food", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))
        with self.assertRaises(ValueError) as error:
            self.petshop.add_food("Test Food", -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

    def test_add_food_correct(self):
        # TO DO
        name = 'Test'
        quantity = 5
        result_as_str = self.petshop.add_food(name, quantity)
        self.assertEqual(f"Successfully added {quantity:.2f} grams of {name}.", result_as_str)
        expected = {'Test': 5}
        result = self.petshop.food
        self.assertEqual(expected, result)
        self.petshop.add_food(name, quantity)
        result = self.petshop.food
        expected = {'Test': 10}
        self.assertEqual(expected, result)

    def test_add_pet_raises(self):
        self.petshop.pets = ["Pony"]
        with self.assertRaises(Exception) as error:
            self.petshop.add_pet("Pony")
        self.assertEqual("Cannot add a pet with the same name", str(error.exception))

    def test_add_pet_correct(self):
        name = "Pony"
        result_as_str = self.petshop.add_pet(name)
        self.assertEqual(f"Successfully added {name}.", result_as_str)
        # Check it works only for 1 added animal.
        result = self.petshop.pets[0]
        self.assertEqual("Pony", result)
        # pet = self.petshop.pets.index("Pony")
        # self.assertEqual("Pony",self.petshop.pets[pet])

    def test_feed_non_existing_pet_raises(self):
        with self.assertRaises(Exception) as error:
            self.petshop.feed_pet("Rise", "Pony")
        self.assertEqual(f"Please insert a valid pet name", str(error.exception))

    def test_feed_existing_pet_without_food(self):
        self.petshop.pets = ["Pony"]
        food_name = "Rise"
        result = self.petshop.feed_pet(food_name, "Pony")
        self.assertEqual(f'You do not have {food_name}', result)

    def test_feed_pet_adding_food_working_correct(self):
        self.petshop.food["Rise"] = 5
        self.petshop.pets = ["Pony"]
        result = self.petshop.feed_pet("Rise", "Pony")
        self.assertEqual("Adding food...", result)
        self.assertEqual({"Rise": 1005}, self.petshop.food)

    def test_feed_pet_with_more_food(self):
        pet_name = "Pony"
        self.petshop.food["Rise"] = 300
        self.petshop.pets = ["Pony"]
        result = self.petshop.feed_pet("Rise", "Pony")
        self.assertEqual(f"{pet_name} was successfully fed", result)
        self.assertEqual(200, self.petshop.food["Rise"])

    def test_repr_method_work_correct(self):
        self.petshop.pets = ["Pony", "Dog", "Wolf"]
        result = repr(self.petshop)
        expected_result = f'Shop {self.NAME}:\n' \
                          f'Pets: {", ".join(self.petshop.pets)}'
        self.assertEqual(expected_result, result)
