from tools.computer import program_ac, program_kapat


PROGRAMLAR = {
    "chrome": "chrome",
    "steam": "steam",
    "discord": "discord",
    "spotify": "spotify",
    "youtube": "chrome",

    # Not Defteri
    "notepad": "notepad",
    "not defteri": "notepad",
    "not defterini": "notepad",

    # Hesap Makinesi
    "calc": "calc",
    "hesap makinesi": "calc",
}


def calistir(komut):

    komut = komut.lower().strip()

    # KAPATMA
    if "kapat" in komut:

        for kelime, program in PROGRAMLAR.items():

            if kelime in komut:

                sonuc = program_kapat(program)

                if sonuc:
                    return f"{kelime} kapatılıyor."

                return f"{kelime} kapatılamadı."

    # AÇMA
    for kelime, program in PROGRAMLAR.items():

        if kelime in komut:

            sonuc = program_ac(program)

            if sonuc:
                return f"{kelime} açılıyor."

            return f"{kelime} bulunamadı."

    return "Hangi programı açacağımı anlayamadım."