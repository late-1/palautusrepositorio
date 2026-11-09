from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

def main():
    console = Console()
    
    seasons = [
        "2018-19", "2019-20", "2020-21", "2021-22", 
        "2022-23", "2023-24", "2024-25", "2025-26"
    ]
    
    season = Prompt.ask("Season", choices=seasons, default="2024-25")
    
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    
    nationalities = stats.get_nationalities()
    
    while True:
        nationality = Prompt.ask("\nNationality", choices=nationalities, default="")
        
        if not nationality:
            break
            
        players = stats.top_scorers_by_nationality(nationality)
        
        console.print(f"\n[italic]Season {season} players from {nationality}[/italic]\n")
        
        table = Table(show_header=True, header_style="bold")
        
        table.add_column("name", style="cyan", no_wrap=True)
        table.add_column("team", style="magenta")
        table.add_column("goals", style="green", justify="right")
        table.add_column("assists", style="green", justify="right")
        table.add_column("points", style="green", justify="right")
        
        for p in players:
            table.add_row(
                p.name, 
                p.team, 
                str(p.goals), 
                str(p.assists), 
                str(p.points)
            )
            
        console.print(table)

if __name__ == "__main__":
    main()