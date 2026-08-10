from tools.computer import program_ac, program_kapat


PROGRAMLAR = {
    "chrome": "chrome",
    "steam": "steam",
    "discord": "discord",
    "spotify": "spotify",
    "youtube": "chrome",

    "notepad": "notepad",
    "not defteri": "notepad",
    "not defterini": "notepad",

    "calc": "calc",
    "hesap makinesi": "calc",
}


def calistir(komut):
    komut = komut.lower().strip()

    if "kapat" in komut:
        for kelime, program in PROGRAMLAR.items():
            if kelime in komut:
                sonuc = program_kapat(program)

                if "kapatıldı." in sonuc:
                    return f"{kelime} kapatılıyor."

                return f"{kelime} kapatılamadı."

    for kelime, program in PROGRAMLAR.items():
        if kelime in komut:
            sonuc = program_ac(program)

            if sonuc == f"{program} açıldı.":
                return f"{kelime} açılıyor."

            return sonuc

    return "Hangi programı açacağımı anlayamadım."