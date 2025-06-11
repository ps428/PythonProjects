# Pygame Progress Bar

A simple yet effective progress bar implementation using tqdm, a fast and extensible progress bar for Python.

## What It Does

This tool creates a visual progress bar in your console that:
- Shows loading percentage
- Displays an animated progress indicator
- Provides estimated time remaining for long operations

## How It Works

The implementation uses tqdm, a popular Python library for creating progress bars:

1. The code creates a progress bar with 100 steps
2. It displays "Loading..." as the description
3. The bar updates as the process completes each step
4. When finished, it shows 100% completion

While this example simply loops through a range, you can use this same pattern for:
- File downloads
- Data processing tasks
- Long computational operations
- Any task where you want to show progress to users

## Usage

Simply run the program:

```
python main.py
```

To implement this in your own projects:

```python
from tqdm import tqdm

# Replace this range with your actual task
for i in tqdm(range(your_total_steps), desc="Your Task Description"):
    # Your actual task code here
    your_task_function(i)
```

## Requirements

- Python 3.x
- tqdm library (`pip install tqdm`)

## Examples

### Basic Progress Bar
```python
from tqdm import tqdm
import time

for i in tqdm(range(100)):
    time.sleep(0.1)  # Simulate work
```

### Progress Bar with Custom Formatting
```python
from tqdm import tqdm
import time

for i in tqdm(range(100), desc="Processing", unit="items", colour="green"):
    time.sleep(0.1)  # Simulate work
```
