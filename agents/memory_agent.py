from tools.memory import bilgi_kaydet, bilgi_getir


def calistir(komut):

    k = komut.lower().strip()


    # =====================
    # İSİM SORMA
    # =====================

    if k in [
        "benim adım ne",
        "adım ne",
        "ismim ne",
        "ben kimim"
    ]:

        isim = bilgi_getir("isim")

        if isim:
            return True, f"Adın {isim}."

        return True, "Henüz adını bilmiyorum."


    # =====================
    # İSİM KAYDETME
    # =====================

    if k.startswith("benim adım "):

        isim = komut[len("benim adım "):].strip()

        bilgi_kaydet("isim", isim)

        return True, f"Tamam. Adını {isim} olarak kaydettim."


    if k.startswith("adım "):

        isim = komut[len("adım "):].strip()

        bilgi_kaydet("isim", isim)

        return True, f"Tamam. Adını {isim} olarak kaydettim."



    # =====================
    # FAVORİ OYUN SORMA
    # =====================

    if k in [
        "en sevdiğim oyun ne",
        "favori oyunum ne",
        "hangi oyunu seviyorum"
    ]:

        oyun = bilgi_getir("favori_oyun")

        if oyun:
            return True, f"Favori oyunun {oyun}."

        return True, "Favori oyununu bilmiyorum."



    # =====================
    # FAVORİ OYUN KAYDETME
    # =====================

    if k.startswith("en sevdiğim oyun "):

        oyun = komut[len("en sevdiğim oyun "):].strip()

        bilgi_kaydet(
            "favori_oyun",
            oyun
        )

        return True, f"Tamam. Favori oyununu {oyun} olarak kaydettim."



    # =====================
    # YAŞ SORMA
    # =====================

    if k in [
        "yaşım kaç",
        "kaç yaşındayım",
        "ben kaç yaşındayım"
    ]:

        yas = bilgi_getir("yas")

        if yas:
            return True, f"Yaşın {yas}."

        return True, "Yaşını bilmiyorum."



    # =====================
    # YAŞ KAYDETME
    # =====================

    if "yaşındayım" in k:

        yas = k.replace("ben", "")
        yas = yas.replace("yaşındayım", "")
        yas = yas.strip()

        bilgi_kaydet(
            "yas",
            yas
        )

        return True, f"Yaşını {yas} olarak kaydettim."



    # =====================
    # ŞEHİR SORMA
    # =====================

    if k in [
        "hangi şehirde yaşıyorum",
        "yaşadığım şehir ne",
        "şehirim ne",
        "nerede yaşıyorum",
        "hangi şehirdeyim",
        "ben nereliyim"
    ]:

        sehir = bilgi_getir("sehir")

        if sehir:
            return True, f"{sehir} şehrinde yaşıyorsun."

        return True, "Yaşadığın şehri bilmiyorum."



    # =====================
    # ŞEHİR KAYDETME
    # =====================

    if "şehrinde yaşıyorum" in k:

        sehir = komut.lower()

        sehir = sehir.replace(
            "ben",
            ""
        )

        sehir = sehir.replace(
            "şehrinde yaşıyorum",
            ""
        )

        sehir = sehir.strip()


        bilgi_kaydet(
            "sehir",
            sehir
        )

        return True, f"Tamam. Yaşadığın şehri {sehir} olarak kaydettim."


    # İstanbul gibi "İstanbul'da yaşıyorum" formatı

    if "da yaşıyorum" in k or "de yaşıyorum" in k:

        sehir = k

        sehir = sehir.replace(
            "yaşıyorum",
            ""
        )

        sehir = sehir.replace(
            "da",
            ""
        )

        sehir = sehir.replace(
            "de",
            ""
        )

        sehir = sehir.strip()


        bilgi_kaydet(
            "sehir",
            sehir
        )

        return True, f"Tamam. Yaşadığın şehri {sehir} olarak kaydettim."


    return False, None