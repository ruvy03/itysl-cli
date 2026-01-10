import json
import sys
import os
from pathlib import Path
from typing import List, Optional

from .models import Season, SearchResult
from .config import DEFAULT_CONFIG_PATH, DEFAULT_VIDEO_DIR


def get_project_root() -> Path:
   
    current_file = Path(__file__).resolve()
    return current_file.parent.parent


class DataManager:
    
    def __init__(self, config_path: str = DEFAULT_CONFIG_PATH):
        
        self.project_root = get_project_root()
        self.config_path = self.project_root / config_path
        self.data = self._load_data()
        self.seasons = self._parse_seasons()
    
    def _load_data(self) -> dict:
        
        if not self.config_path.exists():
            print(f"Error: Configuration file '{self.config_path}' not found.")
            print(f"Expected location: {self.config_path}")
            print("Please ensure itysl_data.json is in the project directory.")
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
        
        video_dir = self.data.get('video_directory', DEFAULT_VIDEO_DIR)
        
        video_path = Path(video_dir)
        if not video_path.is_absolute():
            video_path = self.project_root / video_path
        
        return video_path
    
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