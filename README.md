# Keystroke Counter

## What is this?
A script that records how many keystrokes one has typed for each key.

This script does not record the order of each keystrokes, so this is more of a key-counter and rather than a keylogger. (No I'm not stealing your email password)

The script is for **Windows** only

---
## Usage
1. Import the following python packges.
`pip install win32api win32console win32gui pythoncom pyWinhook`
2. See the following ways to run this script:

### Combine with autohotkey (Suggested)
1. Install [autohotkey](https://www.autohotkey.com)
2. Double click to run `keystroke_toggle.ahk`
3. Press the F13 key to toggle the key counter script on/off. When toggling off the script will  
automatically save the key strokes to the text file. 

### Simple way
1. Run the script directly in the terminal.
`python keystroke_counter.py`
2. After a while you can then press (by default) the `Pause/Break` key to save the recorded keystrokes to the `keystroke_record.txt` file

Note that by doing this you would need to have the terminal window open to keep the script running. Once the terminal window is closed the script will also terminate.

### Run in background
1. Run the script with the following command
`pythonw keystroke_counter.py`
2. Occasionally press the `Pause/Break` key to save the keystrokes
3. To terminate the script you would need to use the following command
`taskkill /im pythonw.exe /f`