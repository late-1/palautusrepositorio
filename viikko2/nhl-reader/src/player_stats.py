class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = filter(lambda p: p.nationality == nationality, self.players)
        return sorted(filtered_players, key=lambda p: p.points, reverse=True)
        
    def get_nationalities(self):
        nationalities = set(p.nationality for p in self.players)
        return sorted(list(nationalities))