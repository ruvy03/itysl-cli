import subprocess
import shutil
from pathlib import Path


class VideoPlayer:
    
    @staticmethod
    def play(filepath: Path, start_time: int = 0) -> None:
        if not filepath.exists():
            print(f"\n\033[91mError: Video file not found:\033[0m {filepath}")
            input("\nPress Enter to continue...")
            return
        
        if not shutil.which('mpv'):
            print("\n\033[91mError: mpv not found on your system.\033[0m")
            print("Please install mpv: https://mpv.io/installation/")
            input("\nPress Enter to continue...")
            return
        
        VideoPlayer._display_playback_info(filepath, start_time)
        VideoPlayer._play_with_mpv(filepath, start_time)
    
    @staticmethod
    def _play_with_mpv(filepath: Path, start_time: int) -> None:
        try:
            cmd = ['mpv', str(filepath)]
            if start_time > 0:
                cmd.append(f'--start={start_time}')
            
            subprocess.run(cmd)
            
        except Exception as e:
            print(f"\n\033[91mError launching mpv:\033[0m {e}")
            input("\nPress Enter to continue...")
    
    @staticmethod
    def _display_playback_info(filepath: Path, start_time: int) -> None:
        print(f"\n\033[92m▶ Playing:\033[0m {filepath.name}")
        if start_time > 0:
            minutes, seconds = divmod(start_time, 60)
            print(f"\033[90mStarting at: {start_time}s ({minutes}m {seconds}s)\033[0m")
        print()