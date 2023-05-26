from unittest import TestCase

from project.team import Team


class TeamTests(TestCase):
    def setUp(self) -> None:
        self.team = Team("TestTeam")

    def test_is_init_work_correct(self):
        self.team.members = {}
        self.assertEqual("TestTeam", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_is_name_getter_work_correct(self):
        name = self.team.name
        self.assertEqual("TestTeam", name)

    def test_is_setter_with_non_alpha_name_raises(self):
        with self.assertRaises(ValueError) as error:
            self.team.name = "asd123@"
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

    def test_setter_work_correct(self):
        self.team.name = "NewTeamName"
        self.assertEqual("NewTeamName", self.team.name)

    def test_add_member_work_correct(self):
        self.team.members = {}
        self.assertEqual({}, self.team.members)
        result = self.team.add_member(Member1=20)
        self.assertEqual(f"Successfully added: Member1", result)
        self.assertEqual(20, self.team.members["Member1"])
        result = self.team.add_member(Member2=21, Member3=23)
        self.assertEqual(f"Successfully added: Member2, Member3", result)
        self.assertEqual({"Member1": 20, "Member2": 21, "Member3": 23}, self.team.members)

    def test_remove_member_with_non_existing_member(self):
        self.team.members = {"Pesho": 20}
        result = self.team.remove_member("Gosho")
        self.assertEqual(f"Member with name Gosho does not exist", result)
        self.assertEqual(1, len(self.team.members))

    def test_remove_existing_member(self):
        self.team.members = {"Pesho": 20, "Josh": 23}
        result = self.team.remove_member("Pesho")
        self.assertEqual(f"Member Pesho removed", result)
        self.assertEqual(1, len(self.team.members))

    def test_gt_dunder(self):
        self.team.members = {"Pesho": 20, "Josh": 23}
        team2 = Team("AnotherTeam")
        team2.members = {"Member": 20}
        self.assertEqual(False, self.team < team2)
        self.assertEqual(True, team2 < self.team)

    def test_len_dunder(self):
        self.team.members = {"Pesho": 20, "Josh": 23}
        self.assertEqual(2, len(self.team))

    def test_dunder_add(self):
        # new_team_name = f"{self.name}{other.name}"
        # new_team = Team(new_team_name)
        # new_team.add_member(**self.members)
        # new_team.add_member(**other.members)
        # return new_team
        self.team.members = {"Pesho": 20, "Josh": 23}
        team2 = Team("AnotherTeam")
        team2.members = {"Member": 20}
        new_team = self.team.__add__(team2)
        self.assertEqual("TestTeamAnotherTeam", new_team.name)
        self.assertEqual({"Pesho": 20, "Josh": 23, "Member": 20}, new_team.members)

    def test_str_dunder(self):
        self.team.members = {"Pesho": 20, "Josh": 23}
        expected_result = f"Team name: {self.team.name}\nMember: Josh - 23-years old\nMember: Pesho - 20-years old"
        self.assertEqual(expected_result, str(self.team))

    def test_str_with_same_years(self):
        self.team.members = {"Pesho": 20, "Josh": 20}
        expected_result = f"Team name: {self.team.name}\nMember: Josh - 20-years old\nMember: Pesho - 20-years old"
        self.assertEqual(expected_result, str(self.team))
