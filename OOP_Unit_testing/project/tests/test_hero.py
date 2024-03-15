from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.best_hero = Hero("Miro", 1, 100, 100)
        self.enemy_hero = Hero("Pesho", 1, 50, 50)

    def test_initialization(self):
        self.assertEqual("Miro", self.best_hero.username)
        self.assertEqual(19, self.best_hero.level)
        self.assertEqual(100, self.best_hero.health)
        self.assertEqual(50, self.best_hero.damage)

    def test_battle_yourself_expect_exception_error(self):
        with self.assertRaises(Exception) as ex:
            self.best_hero.battle(self.best_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_zero_health(self):
        self.best_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.best_hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_with_zero_health(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.best_hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight Pesho. He needs to rest", str(ve.exception))

    def test_battle_damage_if_taken(self):
        self.best_hero.health = 50
        result = self.best_hero.battle(self.enemy_hero)

        self.assertEqual(0, self.best_hero.health)
        self.assertEqual(-50, self.enemy_hero.health)
        self.assertEqual("Draw", result)

    def test_battle_enemy_and_win_expect_stats_upgrade(self):
        result = self.best_hero.battle(self.enemy_hero)

        self.assertEqual(2, self.best_hero.level)
        self.assertEqual(55, self.best_hero.health)
        self.assertEqual(105, self.best_hero.damage)
        self.assertEqual("You win", result)

    def test_battle_enemy_and_lose_expect_stats_upgrade(self):
        self.best_hero, self.enemy_hero = self.enemy_hero, self.best_hero

        result = self.best_hero.battle(self.enemy_hero)

        self.assertEqual(2, self.enemy_hero.level)
        self.assertEqual(55, self.enemy_hero.health)
        self.assertEqual(105, self.enemy_hero.damage)
        self.assertEqual("You lose", result)

    def test__str__(self):
        self.assertEqual(
            f"Hero Miro: 1 lvl\n"
            f"Health: 100\n"
            f"Damage: 100\n",
            str(self.best_hero)
        )


if __name__ == "__main__":
    main()