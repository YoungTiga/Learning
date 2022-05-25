from project.hero import Hero
from unittest import TestCase,main

class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero  = Hero("Warrior",10,100,50)
        self.enemy = Hero("Defender", 10, 100, 50)

    def test_init(self):
        username = "Warrior"
        level = 10
        health = 100
        damage= 50

        test_hero = Hero(username,level,health,damage)

        self.assertEqual(username,test_hero.username)
        self.assertEqual(level,test_hero.level)
        self.assertEqual(health, test_hero.health)
        self.assertEqual(damage, test_hero.damage)

    def test_if_throws_error_if_enemy_name_equal_hero_name(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself",str(ex.exception))

    def test_if_battle_throws_error_if_hero_health_below_or_zero(self):
        for health in [0,-50]:
            self.hero.health = health
            with self.assertRaises(Exception) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual("Your health is lower than or equal to 0. You need to rest",str(ex.exception))

    def test_if_battle_throws_error_if_enemy_health_below_or_zero(self):
        for health in [0,-50]:
            self.enemy.health = health
            with self.assertRaises(Exception) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest",str(ex.exception))

    def test_if_return_draw_correctly(self):
        res = self.hero.battle(self.enemy)
        self.assertEqual("Draw",res)
        self.assertEqual(-400,self.hero.health)
        self.assertEqual(-400, self.enemy.health)

    def test_if_returns_correctly_if_hero_win(self):
        self.enemy.level=1
        res=self.hero.battle(self.enemy)
        self.assertEqual("You win",res)
        self.assertEqual(11,self.hero.level)
        self.assertEqual(55,self.hero.health)
        self.assertEqual(55,self.hero.damage)
        self.assertEqual(-400,self.enemy.health)

    def test_if_returns_correctly_if_enemy_win(self):
        self.hero.level=1
        res=self.hero.battle(self.enemy)
        self.assertEqual("You lose",res)
        self.assertEqual(11,self.enemy.level)
        self.assertEqual(55,self.enemy.health)
        self.assertEqual(55,self.enemy.damage)
        self.assertEqual(-400,self.hero.health)

    def test_if_str_method_works_correctly(self):
        expected = f"Hero Warrior: 10 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 50\n"
        res= str(self.hero)
        self.assertEqual(expected,res)

if __name__ == "__main__":
    main()