import subprocess
import shutil
from pathlib import Path

from .config import SEPARATOR, PLAYER_CONTROLS


class VideoPlayer:
    
    @staticmethod
    def play(filepath: Path, start_time: int = 0) -> None:
   
        if not filepath.exists():
            print(f"\nError: Video file not found: {filepath}")
            input("\nPress Enter to continue...")
            return
        
        if not shutil.which('mpv'):
            print("\nError: mpv not found on your system.")
            print("Please install mpv: https://mpv.io/installation/")
            input("\nPress Enter to continue...")
            return
        
        VideoPlayer._display_playback_info(filepath, start_time)
        VideoPlayer._display_controls()
        VideoPlayer._play_with_mpv(filepath, start_time)
    
    @staticmethod
    def _play_with_mpv(filepath: Path, start_time: int) -> None:

        try:
            cmd = ['mpv', str(filepath)]
            if start_time > 0:
                cmd.append(f'--start={start_time}')
            
            subprocess.run(cmd)
            
        except Exception as e:
            print(f"\nError launching mpv: {e}")
            input("\nPress Enter to continue...")
    
    @staticmethod
    def _display_playback_info(filepath: Path, start_time: int) -> None:

        print(f"\nPlaying: {filepath.name}")
        if start_time > 0:
            minutes, seconds = divmod(start_time, 60)
            print(f"Starting at: {start_time}s ({minutes}m {seconds}s)")
    
    @staticmethod
    def _display_controls() -> None:
        print(f"\n{SEPARATOR}")
        print(PLAYER_CONTROLS)
        print(f"{SEPARATOR}\n")