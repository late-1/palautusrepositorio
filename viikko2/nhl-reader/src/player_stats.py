class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = filter(lambda p: p.nationality == nationality, self.players)
        return sorted(filtered_players, key=lambda p: p.points, reverse=True)

    def top_scorers_by_team(self, team):
        filtered_players = filter(lambda p: p.team == team, self.players)
        return sorted(filtered_players, key=lambda p: p.points, reverse=True)

    def get_nationalities(self):
        nationalities = set(p.nationality for p in self.players)
        return sorted(list(nationalities))

    def get_teams(self):
        teams = set(p.team for p in self.players)
        return sorted(list(teams))

    def top_goal_scorers(self, how_many):
        """Palauttaa eniten maaleja tehneet pelaajat laskevassa järjestyksessä."""
        return sorted(self.players, key=lambda p: p.goals, reverse=True)[:how_many]
