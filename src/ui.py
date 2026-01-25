from typing import List, Optional
import questionary

from .config import (
    CLI_STYLE, SEPARATOR, APP_TITLE, ITYSL_LOGO, PLAYER_CONTROLS,
    MENU_BROWSE_SEASONS, MENU_SEARCH_SKETCHES, MENU_RANDOM_SKETCH,
    MENU_LIST_ALL, MENU_VIDEO_CONTROLS, MENU_SETTINGS, MENU_EXIT, MENU_BACK
)
from .models import Season, Episode, SearchResult


class UI:
    
    @staticmethod
    def display_header() -> None:
        """Display colorful ASCII art logo"""
        print("\033[95m" + ITYSL_LOGO + "\033[0m")  # Magenta color
    
    @staticmethod
    def main_menu() -> Optional[str]:
        """Display main menu and get user choice"""
        choices = [
            MENU_BROWSE_SEASONS,
            MENU_SEARCH_SKETCHES,
            MENU_RANDOM_SKETCH,
            MENU_LIST_ALL,
            MENU_VIDEO_CONTROLS,
            MENU_SETTINGS,
            MENU_EXIT
        ]
        
        return questionary.select(
            "Hey shirt brother, what would you like to do?",
            choices=choices,
            style=CLI_STYLE,
            use_arrow_keys=True
        ).ask()
    
    @staticmethod
    def season_menu(seasons: List[Season]) -> Optional[str]:
        """Display season selection menu"""
        choices = [f"Season {s.season}" for s in seasons]
        choices.append(f"<- {MENU_BACK} to Main Menu")
        
        return questionary.select(
            "Select a season:",
            choices=choices,
            style=CLI_STYLE,
            use_arrow_keys=True
        ).ask()
    
    @staticmethod
    def episode_menu(season: Season) -> Optional[str]:
        """Display episode selection menu"""
        choices = [f"Episode {ep.episode}" for ep in season.episodes]
        choices.append(f"<- {MENU_BACK} to Seasons")
        
        return questionary.select(
            f"Season {season.season} - Select an episode:",
            choices=choices,
            style=CLI_STYLE,
            use_arrow_keys=True
        ).ask()
    
    @staticmethod
    def sketch_menu(season_num: int, episode: Episode) -> Optional[str]:
        """Display sketch selection menu with arrow key navigation"""
        choices = ["Play Full Episode"]
        choices.extend([s.name for s in episode.sketches])
        choices.append(f"<- {MENU_BACK} to Episodes")
        
        return questionary.select(
            f"Season {season_num} Episode {episode.episode}:",
            choices=choices,
            style=CLI_STYLE,
            use_arrow_keys=True,
            use_shortcuts=False
        ).ask()
    
    @staticmethod
    def search_input() -> Optional[str]:
        """Get search query from user"""
        return questionary.text(
            "Enter sketch name to search:",
            style=CLI_STYLE
        ).ask()
    
    @staticmethod
    def search_results_menu(results: List[SearchResult]) -> Optional[str]:
        """Display search results menu"""
        choices = [str(r) for r in results]
        choices.append(f"<- {MENU_BACK} to Main Menu")
        
        return questionary.select(
            f"Found {len(results)} sketch(es):",
            choices=choices,
            style=CLI_STYLE,
            use_arrow_keys=True
        ).ask()
    
    @staticmethod
    def display_all_sketches(seasons: List[Season]) -> None:
        """Display all sketches organized by season and episode"""
        print(f"\n{SEPARATOR}")
        print("ALL SKETCHES")
        print(f"{SEPARATOR}")
        
        for season in seasons:
            print(f"\n\033[96mSEASON {season.season}\033[0m")  # Cyan
            for episode in season.episodes:
                print(f"\n  \033[93mEpisode {episode.episode}\033[0m")  # Yellow
                for sketch in episode.sketches:
                    print(f"     • {sketch.name} \033[90m({sketch.formatted_time})\033[0m")
        
        input("\n\nPress Enter to continue...")
    
    @staticmethod
    def display_video_controls() -> None:
        """Display formatted video player controls"""
        print("\033[92m" + PLAYER_CONTROLS + "\033[0m")  # Green
        input("Press Enter to return to menu...")
    
    @staticmethod
    def display_settings(video_dir: str, config_path: str) -> None:
        """Display current settings"""
        print(f"\n{SEPARATOR}")
        print("SETTINGS")
        print(f"{SEPARATOR}")
        print(f"\nVideo directory: \033[94m{video_dir}\033[0m")
        print(f"Config file: \033[94m{config_path}\033[0m")
        input("\nPress Enter to continue...")
    
    @staticmethod
    def display_no_results(query: str) -> None:
        """Display message when no search results found"""
        print(f"\n\033[91mNo sketches found matching '{query}'\033[0m")
        input("\nPress Enter to continue...")
    
    @staticmethod
    def display_random_sketch(season: int, episode: int, sketch_name: str) -> None:
        """Display information about randomly selected sketch"""
        print(f"\n\033[93m🎲 RANDOM SKETCH:\033[0m \033[96m{sketch_name}\033[0m")
        print(f"\033[90mSeason {season}, Episode {episode}\033[0m\n")
    
    @staticmethod
    def display_exit_message() -> None:
        """Display exit message"""
        print("\n\033[95mI don't even want to be around anymore\033[0m\n")