import json

from ai import ai_cevapla
from tools.memory import bilgi_kaydet


def calistir(kullanici_mesaji):

    prompt = f"""
Sen Jarvis'in hafıza yöneticisisin.

Kullanıcının mesajını incele.

Eğer hafızaya kaydedilecek önemli bilgi varsa:

{{
    "save": true,
    "key": "...",
    "value": "..."
}}

Eğer gerekmiyorsa:

{{
    "save": false
}}

SADECE JSON döndür.

Kullanıcı:

{kullanici_mesaji}
"""

    cevap = ai_cevapla(prompt)

    print("\n=== MEMORY AI ===")
    print(cevap)
    print("=================\n")

    try:

        veri = json.loads(cevap)

    except Exception as e:

        print("JSON HATASI:", e)

        return False

    if veri.get("save"):

        bilgi_kaydet(
            veri["key"],
            veri["value"]
        )

        print("Hafızaya kaydedildi.")

        return True

    print("Kaydedilecek bilgi yok.")

    return False