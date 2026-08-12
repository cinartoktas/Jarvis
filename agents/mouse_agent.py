from tools.mouse import (
    hareket_et,
    sol_tik,
    cift_tik
)

from agents.vision_agent import yazi_bul


def tikla(yazi):

    sonuc = yazi_bul(yazi)

    if not sonuc["success"]:
        return sonuc["error"]

    x = sonuc["x"]
    y = sonuc["y"]

    hareket_et(
        x,
        y
    )

    sol_tik()

    return f"{yazi} tıklandı"


def calistir(komut):

    komut = komut.lower()

    if "tıkla" in komut:

        kelime = komut.replace(
            "tıkla",
            ""
        ).strip()

        return tikla(kelime)

    return "Mouse komutu anlaşılamadı."