import random
from typing import Optional

from .config import (
    DEFAULT_CONFIG_PATH,
    MENU_BROWSE_SEASONS, MENU_SEARCH_SKETCHES, MENU_RANDOM_SKETCH,
    MENU_LIST_ALL, MENU_VIDEO_CONTROLS, MENU_SETTINGS, MENU_EXIT, MENU_BACK
)
from .data_manager import DataManager
from .player import VideoPlayer
from .ui import UI
from .models import Season, Episode


class ITYSLBrowser:
    """Main application class for browsing and playing ITYSL episodes"""
    
    def __init__(self, config_path: str = DEFAULT_CONFIG_PATH):
        """Initialize the browser with data manager, player, and UI"""
        self.data_manager = DataManager(config_path)
        self.player = VideoPlayer()
        self.ui = UI()
    
    def run(self) -> None:
        """Start the application"""
        self.ui.display_header()
        self._main_menu_loop()
    
    def _main_menu_loop(self) -> None:
        """Main menu loop"""
        while True:
            choice = self.ui.main_menu()
            
            if choice is None or choice == MENU_EXIT:
                self.ui.display_exit_message()
                break
            
            self._handle_main_menu_choice(choice)
    
    def _handle_main_menu_choice(self, choice: str) -> None:
        """Route main menu choice to appropriate handler"""
        handlers = {
            MENU_BROWSE_SEASONS: self._browse_by_season,
            MENU_SEARCH_SKETCHES: self._search_sketches,
            MENU_RANDOM_SKETCH: self._play_random_sketch,
            MENU_LIST_ALL: self._list_all_sketches,
            MENU_VIDEO_CONTROLS: self._show_video_controls,
            MENU_SETTINGS: self._show_settings,
        }
        
        handler = handlers.get(choice)
        if handler:
            handler()
    
    def _browse_by_season(self) -> None:
        """Browse episodes by season"""
        while True:
            seasons = self.data_manager.get_all_seasons()
            choice = self.ui.season_menu(seasons)
            
            if choice is None or MENU_BACK in choice:
                break
            
            season_num = int(choice.split()[1])
            season = self.data_manager.get_season(season_num)
            if season:
                self._browse_episodes(season)
    
    def _browse_episodes(self, season: Season) -> None:
        """Browse sketches within a season"""
        while True:
            choice = self.ui.episode_menu(season)
            
            if choice is None or MENU_BACK in choice:
                break
            
            ep_num = int(choice.split()[1])
            episode = season.get_episode(ep_num)
            if episode:
                self._show_episode_menu(season.season, episode)
    
    def _show_episode_menu(self, season_num: int, episode: Episode) -> None:
        """Show menu for selecting sketches within an episode"""
        while True:
            choice = self.ui.sketch_menu(season_num, episode)
            
            if choice is None or MENU_BACK in choice:
                break
            
            self._play_selection(episode, choice)
    
    def _play_selection(self, episode: Episode, choice: str) -> None:
        """Play the selected sketch or full episode"""
        video_dir = self.data_manager.get_video_directory()
        filepath = video_dir / episode.file
        
        if choice == "Play Full Episode":
            self.player.play(filepath, 0)
        else:
            sketch = episode.get_sketch_by_name(choice)
            if sketch:
                self.player.play(filepath, sketch.start_time)
    
    def _search_sketches(self) -> None:
        """Search for sketches by name"""
        search_term = self.ui.search_input()
        
        if not search_term:
            return
        
        results = self.data_manager.search_sketches(search_term)
        
        if not results:
            self.ui.display_no_results(search_term)
            return
        
        self._display_search_results(results)
    
    def _display_search_results(self, results: list) -> None:
        """Display and handle selection from search results"""
        while True:
            choice = self.ui.search_results_menu(results)
            
            if choice is None or MENU_BACK in choice:
                break
            
            idx = next(i for i, r in enumerate(results) if str(r) == choice)
            result = results[idx]
            
            video_dir = self.data_manager.get_video_directory()
            filepath = video_dir / result.file
            self.player.play(filepath, result.sketch.start_time)
    
    def _play_random_sketch(self) -> None:
        """Play a random sketch from the database"""
        all_results = self.data_manager.get_all_search_results()
        
        if not all_results:
            print("\n\033[91mNo sketches found in database\033[0m")
            input("\nPress Enter to continue...")
            return
        
        random_pick = random.choice(all_results)
        self.ui.display_random_sketch(
            random_pick.season,
            random_pick.episode,
            random_pick.sketch.name
        )
        
        video_dir = self.data_manager.get_video_directory()
        filepath = video_dir / random_pick.file
        self.player.play(filepath, random_pick.sketch.start_time)
    
    def _list_all_sketches(self) -> None:
        """List all sketches organized by season and episode"""
        seasons = self.data_manager.get_all_seasons()
        self.ui.display_all_sketches(seasons)
    
    def _show_video_controls(self) -> None:
        """Display video player controls reference"""
        self.ui.display_video_controls()
    
    def _show_settings(self) -> None:
        """Display current settings"""
        video_dir = str(self.data_manager.get_video_directory())
        config_path = self.data_manager.config_path
        self.ui.display_settings(video_dir, config_path)