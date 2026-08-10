import pyautogui
import time


def yaz(metin):

    # Türkçe karakterleri yazabilmek için
    # karakterleri tek tek kontrol ediyoruz.

    turkce = {
        "ç": "ç",
        "Ç": "Ç",
        "ğ": "ğ",
        "Ğ": "Ğ",
        "ı": "ı",
        "İ": "İ",
        "ö": "ö",
        "Ö": "Ö",
        "ş": "ş",
        "Ş": "Ş",
        "ü": "ü",
        "Ü": "Ü",
    }

    for karakter in metin:

        if karakter in turkce:

            # Türkçe karakteri clipboard üzerinden yaz
            import pyperclip

            pyperclip.copy(karakter)

            pyautogui.hotkey(
                "ctrl",
                "v"
            )

        else:

            pyautogui.write(
                karakter
            )

        time.sleep(0.03)

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