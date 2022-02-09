; Run keystroke counter command / Kill the background script
; This command is activated by pressing the F13 key
<!Pause::
F13::
    Send {Pause}
    Process, Exist, pythonw.exe
    if !ErrorLevel = 0 {
        sleep, 200
        Runwait, taskkill /im pythonw.exe /f, , Hide
        Progress, b fs17 WS550 zh0 X2259 Y1335 CW314051 CT66FCF1, Key Counter Script Terminated.., , , consolas
        Sleep, 1500
        Progress, Off
    } else {
        SetWorkingDir %A_ScriptDir%
        Run, pythonw "keystroke_counter_v2.0.py", , Hide
        Progress, b fs17 WS550 zh0 X2259 Y1335 CW314051 CT66FCF1, Key Counter Script Activated.., , , consolas
        Sleep, 1500
        Progress, Off    
    }
return