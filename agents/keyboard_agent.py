import pyautogui
import time


def yaz(metin):
    pyautogui.write(metin, interval=0.03)
    return {
        "success": True,
        "message": f"'{metin}' yazıldı."
    }


def tus_basma(tus):
    pyautogui.press(tus)
    return {
        "success": True,
        "message": f"'{tus}' tuşuna basıldı."
    }


def enter():
    pyautogui.press("enter")
    return {
        "success": True,
        "message": "Enter tuşuna basıldı."
    }