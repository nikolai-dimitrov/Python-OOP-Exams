from unittest import TestCase

from project.plantation import Plantation


class PlantationTest(TestCase):
    SIZE = 5

    def setUp(self) -> None:
        self.plantation = Plantation(self.SIZE)

    def test_init_work_correct(self):
        self.plantation.plants = {"Test": "Test"}
        self.plantation.workers = ["Test"]
        self.assertEqual(5, self.plantation.size)
        self.assertEqual({"Test": "Test"}, self.plantation.plants)
        self.assertEqual(["Test"], self.plantation.workers)

    def test_getter_work_correct(self):
        result = self.plantation.size
        self.assertEqual(self.SIZE, result)

    def test_setter_with_incorrect_value_raises(self):
        with self.assertRaises(ValueError) as error:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(error.exception))

    def test_hire_worker_raises(self):
        self.plantation.workers = ["Test"]
        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker("Test")
        self.assertEqual("Worker already hired!", str(error.exception))

    def test_hire_worker_with_correct_value(self):
        worker = "Test"
        result = self.plantation.hire_worker(worker)
        self.assertEqual(f"{worker} successfully hired.", result)
        self.assertEqual(["Test"], self.plantation.workers)

    def test_len_work_proper(self):
        self.plantation.plants = {"Worker1": ["Test1", "Test2"], "Worker2": ["Test3"]}
        result = len(self.plantation)
        self.assertEqual(3, result)

    def test_planting_with_non_existing_worker_raises(self):
        worker = "Gosho"
        self.plantation.workers = ["Pesho"]
        with self.assertRaises(ValueError) as error:
            self.plantation.planting(worker, "test_plant")
        self.assertEqual(f"Worker with name {worker} is not hired!", str(error.exception))

    # to do with equal or more raises
    def test_is_planting_when_no_size_avaible_raises(self):
        self.plantation.workers = ["Worker1", "Worker2"]
        self.plantation.size = 3
        self.plantation.plants = {"Worker1": ["Test1", "Test2"], "Worker2": ["Test3"]}
        with self.assertRaises(ValueError) as error:
            self.plantation.planting("Worker1", "Test_plant")
        self.assertEqual("The plantation is full!", str(error.exception))

    def test_is_worker_in_plant_keys_work_correct(self):
        self.plantation.workers = ["Worker1"]
        self.plantation.plants = {"Worker1": ["Test1", "Test2"]}
        result = self.plantation.planting("Worker1", "Test3")
        self.assertEqual("Worker1 planted Test3.", result)
        self.assertEqual({"Worker1": ["Test1", "Test2", "Test3"]}, self.plantation.plants)

    def test_is_worker_planting_his_first_plant_correct(self):
        self.plantation.workers = ["Worker1"]
        result = self.plantation.planting("Worker1", "Test_plant")
        self.assertEqual("Worker1 planted it's first Test_plant.", result)
        self.assertEqual({"Worker1": ["Test_plant"]}, self.plantation.plants)

    def test_is_repr_work_correct(self):
        self.plantation.plants = {"Worker1": ["Test1", "Test2"]}
        expected_result = f"Size: {self.SIZE}\n"
        expected_result += f"Workers: Worker1"
        result = repr(self.plantation)

    # def __str__(self):
    #     result = [f"Plantation size: {self.size}"]
    #     result.append(f'{", ".join(self.workers)}')
    #     for worker, plants in self.plants.items():
    #         result.append(f"{worker} planted: {', '.join(plants)}")
    #     return '\n'.join(result)
    def test_str_work_correct(self):
        self.plantation.workers = ['Worker1', 'Worker2']
        self.plantation.plants = {'Worker1': ['Potatoe'], 'Worker2': ['Tulip', "Roze"]}
        expected_result = "Plantation size: 5\nWorker1, Worker2\nWorker1 planted: Potatoe\nWorker2 planted: Tulip, Roze"
        self.assertEqual(expected_result,str(self.plantation))
