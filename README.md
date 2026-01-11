# ITYSL CLI Browser

A command-line interface for browsing and playing "I Think You Should Leave" episodes and sketches using mpv.

## Features

- Browse episodes by season
- Search for specific sketches
- Play random sketches
- Jump directly to sketch timestamps
- Full keyboard navigation

## Requirements

- Python 3.7+
- [mpv](https://mpv.io/installation/) media player

## Installation

1. Clone this repository
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install mpv:
   - **Windows**: Download from [mpv.io](https://mpv.io/installation/)
   - **macOS**: `brew install mpv`
   - **Linux**: `sudo apt install mpv` or equivalent

## Setup

1. Create a `videos` directory in the project root
2. Name your video files to match the JSON config (e.g., `S01E01.mkv`, `S02E03.mkv`)
3. The default config expects files like:
   - `S01E01.mkv` - Season 1, Episode 1
   - `S02E06.mkv` - Season 2, Episode 6
   - etc.

**Note**: You can customize file names and sketch timestamps by editing `itysl_data.json`. Update the `file` field for each episode and adjust `start_time` values (in seconds) for each sketch.

## Usage

Run from the project directory:

```bash
python main.py
```

## Making it Accessible from Anywhere (Windows)

Create a batch file to run the program from any directory:

1. Create a file called `itysl.bat` with this content:

   ```batch
   @echo off
   python "C:\path\to\your\project\main.py"
   ```

2. Save it to a directory that's in your PATH (e.g., `C:\Windows\System32` or create a custom bin folder)

3. Add a custom directory to PATH:

   - Create a folder like `C:\bin`
   - Add it to PATH: System Properties → Environment Variables → Path → New → `C:\bin`
   - Save `itysl.bat` there

4. Now you can run `itysl` from any command prompt!
