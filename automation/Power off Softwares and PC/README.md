# Power Off Utilities

A collection of Python scripts to automatically shut down applications and your PC after a specified time.

## What These Tools Do

These utilities help you:
- Set timers to close specific applications
- Automate PC shutdown at specified times
- Target specific processes by name
- Create countdown timers with visual feedback

## Included Scripts

### 1. anyProcess.py
Shut down any application by process name after a timer.

**How it works:**
- Enter the exact process name to close
- Set a countdown timer in minutes
- The script provides countdown updates
- Uses sudo privileges to kill the process when time expires

**Usage:**
```
python anyProcess.py
```

When prompted:
- Enter process name (e.g., "firefox")
- Enter time in minutes (e.g., "30")

### 2. chromeOff.py
Specifically targets Chrome browser for shutdown.

**How it works:**
- Pre-configured to target Chrome's process name
- Set a timer in minutes
- The script will close Chrome when time expires

**Usage:**
```
python chromeOff.py
```

### 3. firefoxOff.py
Specifically targets Firefox browser for shutdown.

**How it works:**
- Pre-configured to target Firefox's process name
- Set a timer in minutes
- The script will close Firefox when time expires

**Usage:**
```
python firefoxOff.py
```

### 4. teamsOff.py
Specifically targets Microsoft Teams for shutdown.

**How it works:**
- Pre-configured to target Teams' process name
- Set a timer in minutes
- The script will close Teams when time expires

**Usage:**
```
python teamsOff.py
```

### 5. pcOff.py
Shut down your entire PC after a specified time.

**How it works:**
- Set a timer in minutes
- The script provides countdown updates
- Uses system commands to initiate a proper shutdown

**Usage:**
```
python pcOff.py
```

## Requirements

- Python 3.x
- Linux-based operating system (uses pkill command)
- sudo privileges for killing processes

## Setup

1. Make sure Python is installed on your system
2. For security reasons, you should edit the scripts to add your sudo password
3. Make the scripts executable: `chmod +x scriptname.py`

## Use Cases

- Set a timer to close distracting apps after a work session (or skip a boring lecture from college)
- Schedule your PC to shut down after a long download
- Enforce break times by closing work applications
- Save energy by ensuring your PC shuts down after you've left
