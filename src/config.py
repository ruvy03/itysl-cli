from questionary import Style


# File paths
DEFAULT_CONFIG_PATH = "./itysl_data.json"
DEFAULT_VIDEO_DIR = "./videos"

# UI Styling
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

# Display constants
SEPARATOR = "=" * 60
APP_TITLE = "I THINK YOU SHOULD LEAVE - Episode Browser"

# Menu choices
MENU_BROWSE_SEASONS = "Browse by Season"
MENU_SEARCH_SKETCHES = "Search for a Sketch"
MENU_RANDOM_SKETCH = "Random Sketch"
MENU_LIST_ALL = "List All Sketches"
MENU_SETTINGS = "Settings"
MENU_EXIT = "Exit"
MENU_BACK = "Back"

PLAYER_CONTROLS = """
CONTROLS:
  SPACE    - Play/Pause
  Left/Right Arrow - Seek backward/forward 5 seconds
  Up/Down Arrow - Volume up/down
  f        - Toggle fullscreen
  q / ESC  - Quit player
"""