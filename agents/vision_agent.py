import pyautogui
import pytesseract


# Tesseract'ın bilgisayardaki tam yolu
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def ekran_oku():

    try:

        ekran = pyautogui.screenshot()

        metin = pytesseract.image_to_string(
            ekran,
            lang="eng"
        )

        if not metin.strip():

            return {
                "success": False,
                "text": "Ekranda yazı bulunamadı."
            }

        return {
            "success": True,
            "text": "Ekranda bulunan yazılar:\n" + metin
        }

    except Exception as e:

        return {
            "success": False,
            "text": f"Vision hata: {str(e)}"
        }


def yazi_bul(yazi):

    try:

        ekran = pyautogui.screenshot()

        veri = pytesseract.image_to_data(
            ekran,
            lang="eng",
            output_type=pytesseract.Output.DICT
        )

        aranan = yazi.lower().strip()

        for i, kelime in enumerate(veri["text"]):

            kelime = kelime.strip()

            if not kelime:
                continue

            if aranan in kelime.lower():

                x = veri["left"][i]
                y = veri["top"][i]
                w = veri["width"][i]
                h = veri["height"][i]

                return {
                    "success": True,
                    "x": x + w // 2,
                    "y": y + h // 2
                }

        return {
            "success": False,
            "error": f"'{yazi}' yazısı bulunamadı."
        }

    except Exception as e:

        return {
            "success": False,
            "error": f"Vision hata: {str(e)}"
        }


def tikla_yazi(yazi):

    sonuc = yazi_bul(yazi)

    if not sonuc["success"]:
        return sonuc

    x = sonuc["x"]
    y = sonuc["y"]

    pyautogui.moveTo(
        x,
        y,
        duration=0.2
    )

    pyautogui.click()

    return {
        "success": True,
        "message": f"'{yazi}' tıklandı.",
        "x": x,
        "y": y
    }