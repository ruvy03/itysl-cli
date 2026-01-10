from typing import List, Optional
import questionary

from .config import (
    CLI_STYLE, SEPARATOR, APP_TITLE,
    MENU_BROWSE_SEASONS, MENU_SEARCH_SKETCHES, MENU_RANDOM_SKETCH,
    MENU_LIST_ALL, MENU_SETTINGS, MENU_EXIT, MENU_BACK
)
from .models import Season, Episode, SearchResult


class UI:
    
    @staticmethod
    def display_header() -> None:
        print(f"\n{SEPARATOR}")
        print(f"  {APP_TITLE}")
        print(f"{SEPARATOR}\n")
    
    @staticmethod
    def main_menu() -> Optional[str]:

        choices = [
            MENU_BROWSE_SEASONS,
            MENU_SEARCH_SKETCHES,
            MENU_RANDOM_SKETCH,
            MENU_LIST_ALL,
            MENU_SETTINGS,
            MENU_EXIT
        ]
        
        return questionary.select(
            "Hey shirt brother, what would you like to do?",
            choices=choices,
            style=CLI_STYLE
        ).ask()
    
    @staticmethod
    def season_menu(seasons: List[Season]) -> Optional[str]:

        choices = [f"Season {s.season}" for s in seasons]
        choices.append(f"<- {MENU_BACK} to Main Menu")
        
        return questionary.select(
            "Select a season:",
            choices=choices,
            style=CLI_STYLE
        ).ask()
    
    @staticmethod
    def episode_menu(season: Season) -> Optional[str]:

        choices = [f"Episode {ep.episode}" for ep in season.episodes]
        choices.append(f"<- {MENU_BACK} to Seasons")
        
        return questionary.select(
            f"Season {season.season} - Select an episode:",
            choices=choices,
            style=CLI_STYLE
        ).ask()
    
    @staticmethod
    def sketch_menu(season_num: int, episode: Episode) -> Optional[str]:

        choices = ["Play Full Episode"]
        choices.extend([s.name for s in episode.sketches])
        choices.append(f"<- {MENU_BACK} to Episodes")
        
        return questionary.select(
            f"Season {season_num} Episode {episode.episode}:",
            choices=choices,
            style=CLI_STYLE
        ).ask()
    
    @staticmethod
    def search_input() -> Optional[str]:

        return questionary.text(
            "Enter sketch name to search:",
            style=CLI_STYLE
        ).ask()
    
    @staticmethod
    def search_results_menu(results: List[SearchResult]) -> Optional[str]:

        choices = [str(r) for r in results]
        choices.append(f"<- {MENU_BACK} to Main Menu")
        
        return questionary.select(
            f"Found {len(results)} sketch(es):",
            choices=choices,
            style=CLI_STYLE
        ).ask()
    
    @staticmethod
    def display_all_sketches(seasons: List[Season]) -> None:

        print(f"\n{SEPARATOR}")
        print("ALL SKETCHES")
        print(f"{SEPARATOR}")
        
        for season in seasons:
            print(f"\nSEASON {season.season}")
            for episode in season.episodes:
                print(f"\n  Episode {episode.episode}")
                for sketch in episode.sketches:
                    print(f"     - {sketch.name} ({sketch.formatted_time})")
        
        input("\n\nPress Enter to continue...")
    
    @staticmethod
    def display_settings(video_dir: str, config_path: str) -> None:

        print(f"\nVideo directory: {video_dir}")
        print(f"Config file: {config_path}")
        input("\nPress Enter to continue...")
    
    @staticmethod
    def display_no_results(query: str) -> None:

        print(f"\nNo sketches found matching '{query}'")
        input("\nPress Enter to continue...")
    
    @staticmethod
    def display_random_sketch(season: int, episode: int, sketch_name: str) -> None:

        print(f"\nRANDOM: {sketch_name}")
        print(f"Season {season}, Episode {episode}\n")
    
    @staticmethod
    def display_exit_message() -> None:
        print("\nI don't even want to be around anymore!")