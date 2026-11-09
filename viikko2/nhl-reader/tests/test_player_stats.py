import unittest

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def get_players(self):
        return [
            Player({
                "name": "Semenko",
                "nationality": "CAN",
                "team": "EDM",
                "goals": 4,
                "assists": 12,
            }),
            Player({
                "name": "Lemieux",
                "nationality": "CAN",
                "team": "PIT",
                "goals": 45,
                "assists": 54,
            }),
            Player({
                "name": "Kurri",
                "nationality": "FIN",
                "team": "EDM",
                "goals": 37,
                "assists": 53,
            }),
            Player({
                "name": "Yzerman",
                "nationality": "CAN",
                "team": "DET",
                "goals": 42,
                "assists": 56,
            }),
            Player({
                "name": "Gretzky",
                "nationality": "CAN",
                "team": "EDM",
                "goals": 35,
                "assists": 89,
            }),
        ]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(PlayerReaderStub())

    def test_top_scorers_by_team_returns_players_sorted_by_points(self):
        players = self.stats.top_scorers_by_team("EDM")

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Kurri", "Semenko"],
        )
        self.assertEqual([player.points for player in players], [124, 90, 16])

    def test_top_scorers_by_nationality_returns_players_sorted_by_points(self):
        players = self.stats.top_scorers_by_nationality("CAN")

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman", "Semenko"],
        )

    def test_get_teams_returns_sorted_unique_teams(self):
        self.assertEqual(self.stats.get_teams(), ["DET", "EDM", "PIT"])

    def test_get_nationalities_returns_sorted_unique_nationalities(self):
        self.assertEqual(self.stats.get_nationalities(), ["CAN", "FIN"])

    def test_top_goal_scorers_returns_requested_number(self):
        players = self.stats.top_goal_scorers(2)

        self.assertEqual([player.name for player in players], ["Lemieux", "Yzerman"])


if __name__ == "__main__":
    unittest.main()
