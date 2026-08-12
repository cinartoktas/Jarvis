from ai import ai_cevapla
import json


def planla(girdi):

    prompt = """
Sen Jarvis isimli yapay zekanın planlayıcısısın.

Kullanıcının isteğini analiz et ve doğru tool'u seç.

SADECE JSON döndür.
Başka hiçbir açıklama yazma.

Kullanılabilir toollar:

computer:
- open
- close

browser:
- open
- search

keyboard:
- write

mouse:
- click

vision:
- read
- click_text

ÖNEMLİ KURALLAR:

1. Kullanıcı bir PROGRAM açmak istiyorsa computer kullan.

2. Kullanıcı sadece Chrome açmak istiyorsa computer kullan.

Örnek:
chrome aç

{
    "steps": [
        {
            "tool": "computer",
            "action": "open",
            "target": "chrome"
        }
    ]
}

3. Kullanıcı sadece YouTube açmak istiyorsa browser kullan.

Örnek:
youtube aç

{
    "steps": [
        {
            "tool": "browser",
            "action": "open",
            "target": "youtube"
        }
    ]
}

4. Kullanıcı Google'da arama yapmak istiyorsa browser kullan.

Örnek:
google'da yapay zeka ara

{
    "steps": [
        {
            "tool": "browser",
            "action": "search",
            "target": "google yapay zeka"
        }
    ]
}

5. Kullanıcı YouTube'da arama yapmak istiyorsa browser kullan.

Örnek:
youtube'da kedi videoları ara

{
    "steps": [
        {
            "tool": "browser",
            "action": "search",
            "target": "youtube kedi videoları"
        }
    ]
}

Google denmişse ASLA youtube kullanma.

YouTube denmişse ASLA google kullanma.

6. Kullanıcı aynı istekte Chrome'u açıp Google veya YouTube üzerinde işlem yapmak istiyorsa computer ile ayrıca Chrome açma.

Browser zaten Chrome'u açabilir.

Örnek:

Chrome'u aç, Google'da yapay zeka ara

{
    "steps": [
        {
            "tool": "browser",
            "action": "search",
            "target": "google yapay zeka"
        }
    ]
}

7. Kullanıcı birden fazla işlem isterse doğru sırayla steps oluştur.

Örnek:

Chrome'u aç, Google'da yapay zeka ara, sonra Google yazısına tıkla

{
    "steps": [
        {
            "tool": "browser",
            "action": "search",
            "target": "google yapay zeka"
        },
        {
            "tool": "vision",
            "action": "click_text",
            "target": "Google"
        }
    ]
}

8. Kullanıcı ekranı okumak istiyorsa vision kullan.

{
    "steps": [
        {
            "tool": "vision",
            "action": "read"
        }
    ]
}

9. Kullanıcı ekrandaki yazıya tıklamak istiyorsa vision kullan.

{
    "steps": [
        {
            "tool": "vision",
            "action": "click_text",
            "target": "Google"
        }
    ]
}

10. Kullanıcı klavyeden yazmak istiyorsa keyboard kullan.

{
    "steps": [
        {
            "tool": "keyboard",
            "action": "write",
            "content": "merhaba"
        }
    ]
}

11. Kullanıcı not defterine yazmak istiyorsa önce not defterini aç, sonra yaz.

Örnek:

not defterine merhaba yaz

{
    "steps": [
        {
            "tool": "computer",
            "action": "open",
            "target": "notepad"
        },
        {
            "tool": "keyboard",
            "action": "write",
            "content": "merhaba"
        }
    ]
}

Kullanıcı sadece not defteri aç derse keyboard kullanma.

Kullanıcı isteği:

""" + girdi

    cevap = ai_cevapla(prompt)

    try:

        temiz = cevap.replace("```json", "")
        temiz = temiz.replace("```", "")
        temiz = temiz.strip()

        plan = json.loads(temiz)

        steps = plan.get("steps", [])

        kullanici_metni = girdi.lower()

        chrome_ile_browser = (
            "chrome" in kullanici_metni
            and (
                "google" in kullanici_metni
                or "youtube" in kullanici_metni
            )
        )

        yeni_steps = []

        for step in steps:

            tool = step.get("tool")
            action = step.get("action")
            target = str(step.get("target", "")).lower()

            if target == "chrome" and action == "open":
                step["tool"] = "computer"

            if (
                chrome_ile_browser
                and step.get("tool") == "computer"
                and step.get("action") == "open"
                and str(step.get("target", "")).lower() == "chrome"
            ):
                continue

            yeni_steps.append(step)

        plan["steps"] = yeni_steps

        return plan

    except Exception as e:

        print("PLAN HATASI:", e)
        print("AI CEVABI:", cevap)

        return {
            "steps": []
        }