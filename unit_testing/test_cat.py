class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False
import unittest
class TestCat(unittest.TestCase):

  def test_if_cat_size_increments_after_eat_method(self):
    cat = Cat("Tom")
    self.assertEqual(0,cat.size)
    cat.eat()
    self.assertEqual(1,cat.size)

  def test_if_cat_is_fed_after_eating(self):
    cat = Cat("Tom")
    cat.eat()
    self.assertTrue(cat.fed)

  def test_if_cat_will_raise_error_if_eat_method_called_after_its_fed(self):
    cat = Cat("Tom")
    cat.eat()

    with self.assertRaises(Exception) as ex:
      cat.eat()
    self.assertEqual('Already fed.',str(ex.exception))

  def test_if_cat_tries_to_sleep_but_not_fed(self):
    cat = Cat("Tom")
    with self.assertRaises(Exception) as ex:
      cat.sleep()
    self.assertEqual('Cannot sleep while hungry',str(ex.exception))

  def test_if_cat_is_not_sleepy_after_sleeping(self):
    cat = Cat("Tom")
    cat.eat()
    cat.sleep()
    self.assertFalse(cat.sleepy)
if __name__ == "__main__":
  unittest.main()