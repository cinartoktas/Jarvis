import json
import os

DOSYA = "data/history.json"


def gecmisi_oku():

    if not os.path.exists(DOSYA):
        return []

    with open(DOSYA, "r", encoding="utf-8") as f:
        return json.load(f)


def mesaj_ekle(role, content):

    gecmis = gecmisi_oku()

    gecmis.append({
        "role": role,
        "content": content
    })

    # Sadece son 20 mesajı tut
    gecmis = gecmis[-20:]

    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump(
            gecmis,
            f,
            ensure_ascii=False,
            indent=4
        )