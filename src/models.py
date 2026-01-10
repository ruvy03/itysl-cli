from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class Sketch:
    name: str
    start_time: int  # in seconds
    
    @property
    def formatted_time(self) -> str:
        minutes, seconds = divmod(self.start_time, 60)
        return f"{minutes}:{seconds:02d}"
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Sketch':
        return cls(
            name=data['name'],
            start_time=data['start_time']
        )


@dataclass
class Episode:
    episode: int
    file: str
    sketches: List[Sketch]
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Episode':
        return cls(
            episode=data['episode'],
            file=data['file'],
            sketches=[Sketch.from_dict(s) for s in data['sketches']]
        )
    
    def get_sketch_by_name(self, name: str) -> Optional[Sketch]:
        return next((s for s in self.sketches if s.name == name), None)


@dataclass
class Season:
    season: int
    episodes: List[Episode]
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Season':
        return cls(
            season=data['season'],
            episodes=[Episode.from_dict(e) for e in data['episodes']]
        )
    
    def get_episode(self, episode_num: int) -> Optional[Episode]:
        return next((e for e in self.episodes if e.episode == episode_num), None)


@dataclass
class SearchResult:
    season: int
    episode: int
    sketch: Sketch
    file: str
    
    def __str__(self) -> str:
        return f"S{self.season:02d}E{self.episode:02d} - {self.sketch.name}"