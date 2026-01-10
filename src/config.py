from questionary import Style


DEFAULT_CONFIG_PATH = "./itysl_data.json"
DEFAULT_VIDEO_DIR = "./videos"

CLI_STYLE = Style([
    ('qmark', 'fg:#673ab7 bold'),
    ('question', 'bold'),
    ('answer', 'fg:#f44336 bold'),
    ('pointer', 'fg:#673ab7 bold'),
    ('highlighted', 'fg:#673ab7 bold'),
    ('selected', 'fg:#cc5454'),
    ('separator', 'fg:#cc5454'),
    ('instruction', ''),
    ('text', ''),
])

SEPARATOR = "=" * 60
APP_TITLE = "I THINK YOU SHOULD LEAVE - CLI"

ITYSL_LOGO = """
╔════════════════════════════════════════════════╗
║                                                ║                           
║   ██╗  ████████╗ ██╗   ██╗ ███████╗ ██╗        ║                         
║   ██║     ██╔══╝ ╚██╗ ██╔╝ ██╔════╝ ██║        ║                         
║   ██║     ██║     ╚████╔╝  ███████╗ ██║        ║                         
║   ██║     ██║      ╚██╔╝   ╚════██║ ██║        ║                         
║   ██║     ██║       ██║    ███████║ ███████╗   ║                         
║   ╚═╝     ╚═╝       ╚═╝    ╚══════╝ ╚══════╝   ║                                  
║                                                ║                           
╚════════════════════════════════════════════════╝
"""

MENU_BROWSE_SEASONS = "Browse by Season"
MENU_SEARCH_SKETCHES = "Search for a Sketch"
MENU_RANDOM_SKETCH = "Random Sketch"
MENU_LIST_ALL = "List All Sketches"
MENU_VIDEO_CONTROLS = "Show Video Controls"
MENU_SETTINGS = "Settings"
MENU_EXIT = "Exit"
MENU_BACK = "Back"

PLAYER_CONTROLS = """
╔════════════════════════════════════════════════════════════════╗
║                      VIDEO PLAYER CONTROLS                     ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  PLAYBACK:                                                     ║
║    SPACE           Play / Pause                                ║
║    q / ESC         Quit player and return to menu              ║
║                                                                ║
║  SEEKING:                                                      ║
║    ← / →           Seek backward / forward 5 seconds           ║
║    Shift + ← / →   Seek backward / forward 1 minute            ║
║    [ / ]           Decrease / increase playback speed          ║
║                                                                ║
║  AUDIO & VIDEO:                                                ║
║    ↑ / ↓           Volume up / down                            ║
║    m               Mute / unmute audio                         ║
║    f               Toggle fullscreen                           ║
║                                                                ║
║  SUBTITLES:                                                    ║
║    v               Toggle subtitle visibility                  ║
║    j / J           Cycle through available subtitles           ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
"""