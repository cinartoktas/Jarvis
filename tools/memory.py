import json
import os

DOSYA = "data/memory.json"


def hafizayi_oku():

    if not os.path.exists(DOSYA):
        return {}

    with open(DOSYA, "r", encoding="utf-8") as f:
        return json.load(f)


def hafizayi_kaydet(veri):

    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)


def bilgi_kaydet(anahtar, deger):

    veri = hafizayi_oku()

    veri[anahtar] = deger

    hafizayi_kaydet(veri)


def bilgi_getir(anahtar):

    veri = hafizayi_oku()

    return veri.get(anahtar)