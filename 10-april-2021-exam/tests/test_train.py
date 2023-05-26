from unittest import TestCase

from project.train.train import Train


class TrainTest(TestCase):
    NAME = "Test Train"
    CAPACITY = 5

    def setUp(self) -> None:
        self.train = Train(self.NAME, self.CAPACITY)

    def test_is_initialized_correct(self):
        self.assertEqual(self.NAME, self.train.name)
        self.assertEqual(self.CAPACITY, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_pasager_when_train_is_full_raises(self):
        self.train.capacity = 1
        self.train.passengers = ["Passager1"]
        with self.assertRaises(ValueError) as error:
            self.train.add("Passager Test")
        self.assertEqual("Train is full", str(error.exception))

    def test_add_existing_passager_raises(self):
        passager = "Passager1"
        self.train.passengers = ["Passager1"]
        with self.assertRaises(ValueError) as error:
            self.train.add(passager)
        self.assertEqual(f"Passenger {passager} Exists", str(error.exception))

    def test_add_passager_correct(self):
        passager = "Passager1"
        result = self.train.add(passager)
        self.assertEqual(f"Added passenger {passager}", result)
        result = self.train.passengers[0]
        self.assertEqual(passager, result)

    def test_remove_non_existing_passager(self):
        passager = "Passager1"
        with self.assertRaises(ValueError) as error:
            self.train.remove(passager)
        self.assertEqual("Passenger Not Found", str(error.exception))

    def test_remove_existing_passager(self):
        passager = "Passager1"
        self.train.passengers = ["Passager1"]
        result = self.train.remove(passager)
        self.assertEqual(f"Removed {passager}", result)
        self.assertEqual(0,len(self.train.passengers))
