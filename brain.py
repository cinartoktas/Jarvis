from graphs.graph import graph
from tools.memory import bilgi_getir


def dusun(komut):

    if komut.lower() == "çık":
        return "EXIT"


    sonuc = graph.invoke({
        "user_input": komut
    })


    cevap = sonuc["response"]


    isim = bilgi_getir("isim")


    if isim:

        selamlama_kelimeleri = [
            "merhaba",
            "selam",
            "hey",
            "nasılsın"
        ]


        if any(
            kelime in komut.lower()
            for kelime in selamlama_kelimeleri
        ):

            cevap = f"{isim}, {cevap}"


    return cevap