from project.team import Team
import unittest


class TestTeam(unittest.TestCase):
    # def test_if_team_is_initialized_correctly(self):
    #     team = Team("Test")
    #     self.assertEqual("Test",team.name)
    #     self.assertEqual({},team.members)

    def test_if_team_name_getter_throws_error(self):
        team = Team("Team")

        with self.assertRaises(ValueError) as ex:
            team.name = "12Team12"
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    # def test_if_add_member_method_works_correctly(self):
    #     team = Team("Test")
    #     self.assertEqual({},team.members)
    #     res = team.add_member(**{"Ivan":12})
    #     self.assertEqual("Successfully added: Ivan",res)
    #     self.assertEqual({"Ivan":12},team.members)

    # def test_if_add_member_method_works_correctly_with_multiple_members(self):
    #     team = Team("Test")
    #     self.assertEqual({},team.members)
    #     res = team.add_member(**{"Ivan":12,"Gosho":12})
    #     self.assertEqual("Successfully added: Ivan, Gosho",res)
    #     self.assertEqual({"Ivan":12, "Gosho":12},team.members)

    def test_if_remove_member_method_works_with_valid_input(self):
        team = Team("Test")
        self.assertEqual({}, team.members)
        team.add_member(**{"Ivan": 12, "Gosho": 12})
        res = team.remove_member("Ivan")
        self.assertEqual("Member Ivan removed", res)
        self.assertEqual({"Gosho": 12}, team.members)

    def test_if_remove_member_method_works_with_invalid_input(self):
        team = Team("Test")
        self.assertEqual({}, team.members)
        team.add_member(**{"Ivan": 12,"Milen":14})
        res = team.remove_member("Gosho")
        self.assertEqual("Member with name Gosho does not exist", res)
        self.assertEqual({"Ivan": 12,"Milen":14}, team.members)

    def test_if_greater_than_thunder_method_works(self):
        team1 = Team("Test")
        team1.add_member(**{"Ivan": 12,"Gari": 13})
        team2 = Team("Testt")
        team2.add_member(**{"Stenli": 12})
        self.assertEqual(team1 > team2,True)
        # self.assertGreater(len(team1),len(team2),True)
        # self.assertTrue(team1<team2)

    def test_if_greater_than_thunder_method_works_false_test(self):
        team1 = Team("Test")
        team1.add_member(**{"Stenli": 12, "Menli": 15})
        team2 = Team("Testt")
        team2.add_member(**{"Ivan": 12, "Gari": 13})
        self.assertFalse(team1 > team2)
        # self.assertEqual(team1 > team2,False)

    def test_if_len_thunder_method_works(self):
        team = Team("Test")
        team.add_member(**{"Stenli": 12})
        self.assertEqual(1, len(team))

    def test_if_add_thunder_method_works(self):
        team1 = Team("Test")
        team1.add_member(**{"Stenli": 12})
        team2 = Team("Testt")
        team2.add_member(**{"Ivan": 12, "Gari": 13})

        team3 = team1 + team2
        self.assertEqual("TestTestt", team3.name)
        self.assertEqual({"Stenli": 12, "Ivan": 12, "Gari": 13}, team3.members)

    def test_if_str_thunder_method_works(self):
        team = Team("Test")
        team.add_member(**{"Ani": 12, "Milen": 15})
        expected = "Team name: Test\nMember: Milen - 15-years old\nMember: Ani - 12-years old"
        self.assertEqual(expected, team.__str__())

    def test_if_str_thunder_method_works_with_equal_ages(self):
        team = Team("Test")
        team.add_member(**{"Ani": 15, "Milen": 15})
        expected = "Team name: Test\nMember: Ani - 15-years old\nMember: Milen - 15-years old"
        self.assertEqual(expected, team.__str__())


if __name__ == "__main__":
    unittest.main()
