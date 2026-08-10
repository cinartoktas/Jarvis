from ai import ai_cevapla


def calistir(soru):

    cevap = ai_cevapla(
        soru
    )

    return True, cevap