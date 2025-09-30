# ScreenTime Tracker

A Python script for tracking how long a user spends on various application windows (tabs) and logging that data in CSV files.

---

## Features

- Continuously monitors the currently active window every second.
- Detects when the user switches windows/tabs, and records start & end times.
- Creates two CSV outputs:
  - `session_logs.csv` — detailed per-session entries with window title and duration.
  - `session_duration.csv` — aggregated total time per window/tab across the script’s runtime.
- Works with Windows (using `pywin32` / `win32gui.GetWindowText()`).

---

## Requirements

- Python 3.x  
- On Windows: `pywin32`  

## Usage

1. Clone the repository (or download the script files)  
   ```bash
   git clone https://github.com/adysfunc/screen-time-tracker.git
   cd your-repo
2. Install dependencies
   ```bash
   pip install pywin32
3. Run the script
   ```bash
   python tracker.py
4. Let it run in the background while you use your system.
5. Check the output CSV files:
- `session_logs.csv`— logs each session: timestamp, window title, and duration.
- `session_duration.csv` — aggregated runtime per window/tab. 