import re
import json

from ai import ai_cevapla


# =========================================================
# HIZLI PLANLAYICI
# =========================================================
# Basit ve sık kullanılan komutları LLM'e göndermeden çözer.
# Böylece 20-30 saniyelik planner beklemesi ortadan kalkar.
# =========================================================

def hizli_planla(girdi):

    metin = girdi.strip()
    kucuk = metin.lower()

    # =====================================================
    # YOUTUBE - VİDEO AÇ
    # =====================================================

    if (
        "youtube" in kucuk
        and "video" in kucuk
        and ("aç" in kucuk or "ac" in kucuk)
    ):

        arama = metin

        # YouTube ifadesini kaldır
        arama = re.sub(
            r"youtube(?:'da|’da| da|da)?",
            "",
            arama,
            flags=re.IGNORECASE
        )

        # "da / de" kalıntılarını kaldır
        arama = re.sub(
            r"\bda\b|\bde\b",
            "",
            arama,
            flags=re.IGNORECASE
        )

        # Açma ifadelerini kaldır
        arama = re.sub(
            r"videolarından birini aç",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"videolarindan birini ac",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"ilk videoyu aç",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"ilk videoyu ac",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"videoyu aç",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"videoyu ac",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"videosu aç",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"videosu ac",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"video aç",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"video ac",
            "",
            arama,
            flags=re.IGNORECASE
        )

        # Gereksiz kelimeler
        arama = re.sub(
            r"\bbirini\b",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"\bilk\b",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"\s+",
            " ",
            arama
        ).strip()

        if arama:

            return {
                "goal": metin,
                "steps": [
                    {
                        "tool": "browser",
                        "action": "search",
                        "target": f"youtube {arama}"
                    },
                    {
                        "tool": "browser",
                        "action": "open_first_video"
                    }
                ]
            }


    # =====================================================
    # GOOGLE - İLK SONUÇ
    # =====================================================

    if (
        "google" in kucuk
        and (
            "ilk sonucu" in kucuk
            or "ilk sonuca" in kucuk
        )
    ):

        arama = metin

        # Google ifadesini kaldır
        arama = re.sub(
            r"google(?:'da|’da| da|da)?",
            "",
            arama,
            flags=re.IGNORECASE
        )

        # "da / de" kalıntıları
        arama = re.sub(
            r"\bda\b|\bde\b",
            "",
            arama,
            flags=re.IGNORECASE
        )

        # İstek sonundaki işlemleri temizle
        arama = re.sub(
            r"bilgi bul",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"bilgi ara",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"ilk sonucu aç",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"ilk sonucu ac",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"ilk sonuca git",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"\s+",
            " ",
            arama
        ).strip()

        # "ve" gibi bağlaçları sadece başta/sonda temizle
        arama = re.sub(
            r"^\s*ve\s+",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"\s+ve\s*$",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = arama.strip()

        if arama:

            return {
                "goal": metin,
                "steps": [
                    {
                        "tool": "browser",
                        "action": "search",
                        "target": f"google {arama}"
                    },
                    {
                        "tool": "browser",
                        "action": "open_first_result"
                    }
                ]
            }


    # =====================================================
    # GOOGLE - SADECE ARAMA
    # =====================================================

    if (
        "google" in kucuk
        and (
            "ara" in kucuk
            or "arama yap" in kucuk
        )
    ):

        arama = metin

        arama = re.sub(
            r"google(?:'da|’da| da|da)?",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"\bda\b|\bde\b",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"arama yap",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"\bara\b",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"\s+",
            " ",
            arama
        ).strip()

        if arama:

            return {
                "goal": metin,
                "steps": [
                    {
                        "tool": "browser",
                        "action": "search",
                        "target": f"google {arama}"
                    }
                ]
            }


    # =====================================================
    # YOUTUBE - SADECE ARAMA
    # =====================================================

    if (
        "youtube" in kucuk
        and (
            "ara" in kucuk
            or "arama yap" in kucuk
        )
    ):

        arama = metin

        arama = re.sub(
            r"youtube(?:'da|’da| da|da)?",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"\bda\b|\bde\b",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"arama yap",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"\bara\b",
            "",
            arama,
            flags=re.IGNORECASE
        )

        arama = re.sub(
            r"\s+",
            " ",
            arama
        ).strip()

        if arama:

            return {
                "goal": metin,
                "steps": [
                    {
                        "tool": "browser",
                        "action": "search",
                        "target": f"youtube {arama}"
                    }
                ]
            }


    # =====================================================
    # NOT DEFTERİNE YAZ
    # =====================================================

    if (
        "not defteri" in kucuk
        and (
            kucuk.endswith(" yaz")
            or kucuk.endswith(" yaz.")
        )
    ):

        icerik = re.sub(
            r"^not defterine\s*",
            "",
            metin,
            flags=re.IGNORECASE
        )

        icerik = re.sub(
            r"\s+yaz\.?$",
            "",
            icerik,
            flags=re.IGNORECASE
        )

        icerik = icerik.strip()

        if icerik:

            return {
                "goal": metin,
                "steps": [
                    {
                        "tool": "computer",
                        "action": "open",
                        "target": "notepad"
                    },
                    {
                        "tool": "keyboard",
                        "action": "write",
                        "content": icerik
                    }
                ]
            }


    # =====================================================
    # CHROME AÇ
    # =====================================================

    if kucuk in (
        "chrome aç",
        "chrome ac",
        "google chrome aç",
        "google chrome ac"
    ):

        return {
            "goal": metin,
            "steps": [
                {
                    "tool": "computer",
                    "action": "open",
                    "target": "chrome"
                }
            ]
        }


    # =====================================================
    # HIZLI PLAN YOK
    # =====================================================

    return None


# =========================================================
# LLM PLANNER
# =========================================================

def llm_planla(girdi):

    prompt = f"""
Sen Jarvis'in görev planlayıcısısın.

Kullanıcı isteğini analiz et ve yapılması gereken işlemleri JSON olarak oluştur.

SADECE JSON DÖNDÜR.
Markdown kullanma.
Açıklama yazma.

Kullanılabilir araçlar:

computer:
- open
- close

browser:
- open
- search
- open_first_video
- open_first_result

keyboard:
- write

mouse:
- click

vision:
- read
- click_text

Kurallar:

- Program açma/kapatma için computer kullan.
- Chrome açmak için computer kullan.
- Web sitesi açmak için browser kullan.
- Google araması için browser search kullan.
- YouTube araması için browser search kullan.
- YouTube'da ilk video istenirse search ardından open_first_video kullan.
- Google'da ilk sonuç istenirse search ardından open_first_result kullan.
- Ekrandaki yazıya tıklamak için vision click_text kullan.
- Ekranı okumak için vision read kullan.
- Klavyeden yazmak için keyboard write kullan.
- Not defterine yazmak için önce notepad aç, sonra keyboard write kullan.
- Birden fazla işlem varsa doğru sırayla steps oluştur.
- Kullanıcı Chrome'u açıp aynı anda Google/YouTube işlemi istiyorsa ayrıca Chrome açma.

ÖRNEK:

Kullanıcı:
YouTube'da kedi videosu aç

JSON:
{{
    "goal": "YouTube'da kedi videosu aç",
    "steps": [
        {{
            "tool": "browser",
            "action": "search",
            "target": "youtube kedi videosu"
        }},
        {{
            "tool": "browser",
            "action": "open_first_video"
        }}
    ]
}}

Kullanıcı:
Google'da Python hakkında bilgi bul ve ilk sonucu aç

JSON:
{{
    "goal": "Google'da Python hakkında bilgi bul ve ilk sonucu aç",
    "steps": [
        {{
            "tool": "browser",
            "action": "search",
            "target": "google Python hakkında"
        }},
        {{
            "tool": "browser",
            "action": "open_first_result"
        }}
    ]
}}

Kullanıcı:
Not defterine Jarvis çalışıyor yaz

JSON:
{{
    "goal": "Not defterine Jarvis çalışıyor yaz",
    "steps": [
        {{
            "tool": "computer",
            "action": "open",
            "target": "notepad"
        }},
        {{
            "tool": "keyboard",
            "action": "write",
            "content": "Jarvis çalışıyor"
        }}
    ]
}}

Kullanıcı isteği:
{girdi}
"""

    cevap = ai_cevapla(prompt)

    try:

        temiz = cevap.replace("```json", "")
        temiz = temiz.replace("```", "")
        temiz = temiz.strip()

        plan = json.loads(temiz)

        if "goal" not in plan:
            plan["goal"] = girdi

        if "steps" not in plan:
            plan["steps"] = []

        return plan

    except Exception as e:

        print("PLAN HATASI:", e)
        print("AI CEVABI:", cevap)

        return {
            "goal": girdi,
            "steps": []
        }


# =========================================================
# ANA PLANNER
# =========================================================

def planla(girdi):

    # Önce hızlı planner.
    # Basit komutlarda LLM hiç çalışmaz.
    hizli = hizli_planla(girdi)

    if hizli is not None:
        return hizli

    # Hızlı planner çözemiyorsa LLM'e gönder.
    return llm_planla(girdi)