from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats

def display_player_table(console, players, season, category, value):
    console.print(f"\n[italic]Season {season} players from {category} {value}[/italic]\n")
    table = Table(show_header=True, header_style="bold")

    table.add_column("name", style="cyan", no_wrap=True)
    table.add_column("team", style="magenta")
    table.add_column("goals", style="green", justify="right")
    table.add_column("assists", style="green", justify="right")
    table.add_column("points", style="green", justify="right")

    for p in players:
        table.add_row(p.name, p.team, str(p.goals), str(p.assists), str(p.points))

    console.print(table)

def display_players_by_category(console, season, category, values, get_players):
    while True:
        value = Prompt.ask(f"\n{category}", choices=values, default="")
        if not value:
            break

        display_player_table(
            console,
            get_players(value),
            season,
            category.lower(),
            value
        )

def main():
    console = Console()
    season = Prompt.ask(
        "Season",
        choices=[
            "2018-19", "2019-20", "2020-21", "2021-22",
            "2022-23", "2023-24", "2024-25", "2025-26"
        ],
        default="2024-25"
    )
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))

    display_players_by_category(
        console,
        season,
        "Nationality",
        stats.get_nationalities(),
        stats.top_scorers_by_nationality
    )
    display_players_by_category(
        console,
        season,
        "Team",
        stats.get_teams(),
        stats.top_scorers_by_team
    )

if __name__ == "__main__":
    main()
