import os

PROGRAMLAR = {
    "chrome": [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ],

    "steam": [
        r"C:\Program Files (x86)\Steam\Steam.exe",
        r"C:\Program Files\Steam\Steam.exe",
    ],

    "discord": [
        os.path.expandvars(r"%LOCALAPPDATA%\Discord\Update.exe"),
    ],

    "spotify": [
        os.path.expandvars(r"%APPDATA%\Spotify\Spotify.exe"),
        os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WindowsApps\Spotify.exe"),
    ],

    "notepad": [
        "notepad.exe",
    ],

    "calc": [
        "calc.exe",
    ],
}


def program_bul(program):

    program = program.lower()

    if program not in PROGRAMLAR:
        return None

    for yol in PROGRAMLAR[program]:

        if os.path.exists(yol) or yol.endswith(".exe"):
            return yol

    return None