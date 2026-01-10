import json
import sys
from pathlib import Path
from typing import List, Optional

from .models import Season, SearchResult
from .config import DEFAULT_CONFIG_PATH, DEFAULT_VIDEO_DIR


class DataManager:
    
    def __init__(self, config_path: str = DEFAULT_CONFIG_PATH):

        self.config_path = config_path
        self.data = self._load_data()
        self.seasons = self._parse_seasons()
    
    def _load_data(self) -> dict:

        if not Path(self.config_path).exists():
            print(f"Error: Configuration file '{self.config_path}' not found.")
            print("Please ensure itysl_data.json is in the same directory.")
            sys.exit(1)
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in configuration file: {e}")
            sys.exit(1)
    
    def _parse_seasons(self) -> List[Season]:

        return [Season.from_dict(s) for s in self.data.get('seasons', [])]
    
    def get_video_directory(self) -> Path:

        return Path(self.data.get('video_directory', DEFAULT_VIDEO_DIR))
    
    def get_all_seasons(self) -> List[Season]:

        return self.seasons
    
    def get_season(self, season_num: int) -> Optional[Season]:
    
        return next((s for s in self.seasons if s.season == season_num), None)
    
    def get_all_search_results(self) -> List[SearchResult]:
 
        results = []
        for season in self.seasons:
            for episode in season.episodes:
                for sketch in episode.sketches:
                    results.append(SearchResult(
                        season=season.season,
                        episode=episode.episode,
                        sketch=sketch,
                        file=episode.file
                    ))
        return results
    
    def search_sketches(self, query: str) -> List[SearchResult]:

        query_lower = query.lower()
        all_results = self.get_all_search_results()
        return [r for r in all_results if query_lower in r.sketch.name.lower()]