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

Örnek kullanıcı:
not defteri aç

JSON:
{
    "steps": [
        {
            "tool": "computer",
            "action": "open",
            "target": "notepad"
        }
    ]
}


2. Kullanıcı Chrome açmak istiyorsa computer kullan.

Örnek:
google aç

JSON:
{
    "steps": [
        {
            "tool": "computer",
            "action": "open",
            "target": "chrome"
        }
    ]
}


3. Kullanıcı YouTube açmak istiyorsa browser kullan.

Örnek:
youtube aç

JSON:
{
    "steps": [
        {
            "tool": "browser",
            "action": "open",
            "target": "youtube"
        }
    ]
}

YouTube sadece kullanıcı açıkça YouTube'dan bahsediyorsa kullanılabilir.


4. Kullanıcı bir şey aramak istiyorsa:

- Kullanıcı "youtube'da", "youtube üzerinde" veya açıkça YouTube'dan bahsediyorsa browser kullan.

Örnek:
youtube'da kedi videoları ara

JSON:
{
    "steps": [
        {
            "tool": "browser",
            "action": "search",
            "target": "youtube kedi videoları"
        }
    ]
}

- Kullanıcı "google'da", "google üzerinde" veya açıkça Google'dan bahsediyorsa browser kullan.

Örnek:
google'da yapay zeka ara

JSON:
{
    "steps": [
        {
            "tool": "browser",
            "action": "search",
            "target": "google yapay zeka"
        }
    ]
}

ÇOK ÖNEMLİ:

Kullanıcı Google diyorsa ASLA youtube yazma.

Kullanıcı YouTube diyorsa ASLA google yazma.

Arama motoru belirtilmişse kullanıcının belirttiği motoru koru.


5. Kullanıcı Chrome'u açıp ardından Google veya YouTube'da bir işlem yapmak istiyorsa:

Eğer aynı kullanıcı isteğinde:
- Chrome'u aç
- Google'da ara
- YouTube'da ara
- Google'a git
- YouTube'a git
- Google/YouTube üzerinde işlem yap

gibi birden fazla işlem varsa, computer ile ayrıca Chrome açma.

Browser tool'u Chrome'u kendisi açabileceği için doğrudan browser kullan.

Örneğin:

Kullanıcı:
Chrome'u aç, Google'da yapay zeka ara

JSON:
{
    "steps": [
        {
            "tool": "browser",
            "action": "search",
            "target": "google yapay zeka"
        }
    ]
}

Kullanıcı:
Chrome'u aç, Google'da yapay zeka ara, sonra Google yazısına tıkla

JSON:
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

Kullanıcı:
Chrome'u aç, YouTube'da kedi videoları ara

JSON:
{
    "steps": [
        {
            "tool": "browser",
            "action": "search",
            "target": "youtube kedi videoları"
        }
    ]
}

Bu tür görevlerde computer ile Chrome açma adımı EKLEME.


6. Kullanıcı ekrandaki yazıları okumak istiyorsa vision kullan.

Örnek:
ekranı oku

JSON:
{
    "steps": [
        {
            "tool": "vision",
            "action": "read"
        }
    ]
}


7. Kullanıcı ekrandaki belirli bir yazıya tıklamak istiyorsa vision kullan.

Örnek:
google yazısına tıkla

JSON:
{
    "steps": [
        {
            "tool": "vision",
            "action": "click_text",
            "target": "Google"
        }
    ]
}


8. Kullanıcı klavyeden yazı yazmak istiyorsa keyboard kullan.

Örnek:
merhaba yaz

JSON:
{
    "steps": [
        {
            "tool": "keyboard",
            "action": "write",
            "content": "merhaba"
        }
    ]
}


9. Kullanıcı NOT DEFTERİNE bir şey yazmak istiyorsa önce not defterini aç, sonra yaz.

Örnek kullanıcı:
not defterine merhaba yaz

JSON:
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


ÇOK ÖNEMLİ:

Kullanıcı sadece:

"not defteri aç"
"not defterini aç"
"notepad aç"

derse keyboard KULLANMA.

Sadece:

{
    "steps": [
        {
            "tool": "computer",
            "action": "open",
            "target": "notepad"
        }
    ]
}

döndür.


Kullanıcı isteği:

""" + girdi

    cevap = ai_cevapla(prompt)

    try:

        temiz = cevap.replace("```json", "")
        temiz = temiz.replace("```", "")
        temiz = temiz.strip()

        return json.loads(temiz)

    except Exception as e:

        print("PLAN HATASI:", e)
        print("AI CEVABI:", cevap)

        return {
            "steps": []
        }