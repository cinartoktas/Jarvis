from tools.mouse import (
    hareket_et,
    sol_tik,
    cift_tik
)

from agents.vision_agent import bul



def tikla(yazi):

    sonuc = bul(yazi)


    if sonuc["bulundu"] == False:

        return sonuc["mesaj"]


    obje = sonuc["obje"]


    hareket_et(
        obje["x"],
        obje["y"]
    )


    sol_tik()


    return f"{yazi} tıklandı"



def calistir(komut):

    komut = komut.lower()


    if "tıkla" in komut:

        kelime = komut.replace("tıkla", "").strip()

        return tikla(kelime)


    return "Mouse komutu anlaşılamadı."