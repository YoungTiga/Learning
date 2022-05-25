
class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'
import unittest
class WorkerTests(unittest.TestCase):

    def test_if_worker_initialized_correctly(self):
        worker = Worker("Test",100,10)
        self.assertEqual("Test",worker.name)
        self.assertEqual(100,worker.salary)
        self.assertEqual(10,worker.energy)
        self.assertEqual(0,worker.money)

    def test_if_worker_energy_is_incremented_after_rest_method(self):
        worker = Worker("Test",100,10)
        energy_expected = 10
        self.assertEqual(energy_expected,worker.energy)

        worker.rest()
        self.assertEqual(energy_expected+1,worker.energy)

    def test_if_error_is_raised_if_worker_tries_to_work_with_energy_less_than_zeto(self):
        worker = Worker("Test",100,0)
        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.',str(ex.exception))
    def test_if_worker_tries_working_with_negative_energy(self):
        worker = Worker("Test",100,-1)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.',str(ex.exception))
    def test_if_worker_money_is_increaset_correctly_after_work_method(self):
        worker = Worker("Test", 100, 10)
        expected_money= 0
        self.assertEqual(expected_money,worker.money)
        worker.work()
        self.assertEqual(expected_money+100,worker.money)
    def test_if_worker_energy_is_correctly_decreased_after_work_method(self):
        worker = Worker("Test", 100, 10)
        expected_energy = 10
        self.assertEqual(expected_energy,worker.energy)
        worker.work()
        self.assertEqual(expected_energy-1,worker.energy)

    def test_if_get_info_method_returns_correct_string_and_values(self):
        worker = Worker("Test", 100, 10)
        expected_output = 'Test has saved 100 money.'
        worker.work()
        self.assertEqual(expected_output,worker.get_info())


if __name__ == "__main__":
    unittest.main()
