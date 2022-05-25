from project.mammal import Mammal
from unittest import TestCase,main

class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("name","mammal_type","sound")
    def test_if_initiated_correctly(self):
        name = "Ivan"
        type = "Mammal"
        sound = "Sound"
        test_mammal = Mammal(name,type,sound)

        self.assertEqual(name,test_mammal.name)
        self.assertEqual(type,test_mammal.type)
        self.assertEqual(sound,test_mammal.sound)

    def test_if_make_sound_method_works_correctly(self):

        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}",self.mammal.make_sound())

    def test_if_get_kingdom_method_works_correctly(self):
        self.assertEqual(self.mammal._Mammal__kingdom, self.mammal.get_kingdom())

    def test_if_get_info_method_works_correctly(self):
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}",self.mammal.info())
if __name__=="__main__":
    main()