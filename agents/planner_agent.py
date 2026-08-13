from ai import ai_cevapla
import json


def planla(girdi):

    prompt = """
Sen Jarvis isimli yapay zekanın planlayıcısısın.

Kullanıcının isteğini analiz et.
Kullanıcının ne yapmak istediğini anla ve gerekli araçları doğru sırayla seç.

Kullanıcıya teknik işlemleri tarif ettirme.
Kullanıcı sadece istediği sonucu söyleyebilir.
Gerekli araç ve adımları kendin belirle.

SADECE JSON döndür.
Başka hiçbir açıklama yazma.

JSON formatı:

{
    "goal": "kullanıcının ulaşmak istediği nihai sonuç",
    "steps": [
        {
            "tool": "...",
            "action": "...",
            "target": "...",
            "content": "..."
        }
    ]
}

Kullanılabilir toollar:

computer:
- open
- close

browser:
- open
- search
- open_first_result
- open_first_video

keyboard:
- write

mouse:
- click

vision:
- read
- click_text


ÖNEMLİ KURALLAR:


1. PROGRAM AÇMA

Kullanıcı bir program açmak istiyorsa computer kullan.

Örnek:

"not defterini aç"

{
    "goal": "Not defterini aç",
    "steps": [
        {
            "tool": "computer",
            "action": "open",
            "target": "notepad"
        }
    ]
}


2. SADECE CHROME AÇMA

Kullanıcı sadece Chrome açmak istiyorsa computer kullan.

Örnek:

"chrome aç"

{
    "goal": "Chrome'u aç",
    "steps": [
        {
            "tool": "computer",
            "action": "open",
            "target": "chrome"
        }
    ]
}


3. SADECE WEB SİTESİ AÇMA

Kullanıcı sadece YouTube açmak istiyorsa browser kullan.

Örnek:

"youtube aç"

{
    "goal": "YouTube'u aç",
    "steps": [
        {
            "tool": "browser",
            "action": "open",
            "target": "youtube"
        }
    ]
}


4. GOOGLE'DA ARAMA

Kullanıcı Google'da arama yapmak istiyorsa browser kullan.

Örnek:

"google'da yapay zeka ara"

{
    "goal": "Google'da yapay zeka araması yap",
    "steps": [
        {
            "tool": "browser",
            "action": "search",
            "target": "google yapay zeka"
        }
    ]
}

Google denmişse YouTube kullanma.


5. YOUTUBE'DA ARAMA

Kullanıcı YouTube'da arama yapmak istiyorsa browser kullan.

Örnek:

"youtube'da kedi videoları ara"

{
    "goal": "YouTube'da kedi videoları ara",
    "steps": [
        {
            "tool": "browser",
            "action": "search",
            "target": "youtube kedi videoları"
        }
    ]
}

YouTube denmişse Google kullanma.


6. CHROME + GOOGLE / YOUTUBE

Kullanıcı:

"Chrome'u aç, Google'da yapay zeka ara"

gibi bir istek verirse ayrıca computer ile Chrome açma.

Browser zaten kendi Chrome oturumunu açabilir.

Doğrudan browser kullan.

Örnek:

{
    "goal": "Google'da yapay zeka araması yap",
    "steps": [
        {
            "tool": "browser",
            "action": "search",
            "target": "google yapay zeka"
        }
    ]
}


7. BİRDEN FAZLA İŞLEM

Kullanıcı birden fazla işlem isterse gerekli adımları doğru sırayla oluştur.

Gereksiz adım ekleme.

Kullanıcının söylediği işlemleri mekanik olarak kopyalamak yerine,
nihai amaca ulaşmak için gereken işlemleri belirle.


8. EKRANI OKUMA

Kullanıcı ekrandaki yazıları okumak istiyorsa vision kullan.

Örnek:

"ekranı oku"

{
    "goal": "Ekrandaki yazıları oku",
    "steps": [
        {
            "tool": "vision",
            "action": "read"
        }
    ]
}


9. EKRANDAKİ YAZIYA TIKLAMA

Kullanıcı ekrandaki belirli bir yazıya tıklamak istiyorsa vision kullan.

Örnek:

"Google yazısına tıkla"

{
    "goal": "Google yazısına tıkla",
    "steps": [
        {
            "tool": "vision",
            "action": "click_text",
            "target": "Google"
        }
    ]
}

Ancak tarayıcıdaki bilinen sonuçlar Selenium ile daha güvenilir şekilde
yapılabiliyorsa vision ile tahmini OCR tıklaması kullanma.


10. KLAVYE

Kullanıcı klavyeden yazı yazmak istiyorsa keyboard kullan.

Örnek:

"merhaba yaz"

{
    "goal": "Merhaba yaz",
    "steps": [
        {
            "tool": "keyboard",
            "action": "write",
            "content": "merhaba"
        }
    ]
}


11. NOT DEFTERİNE YAZMA

Kullanıcı not defterine bir şey yazmak istiyorsa:

önce not defterini aç,
sonra keyboard ile yaz.

Örnek:

"not defterine Jarvis çalışıyor yaz"

{
    "goal": "Not defterine Jarvis çalışıyor yaz",
    "steps": [
        {
            "tool": "computer",
            "action": "open",
            "target": "notepad"
        },
        {
            "tool": "keyboard",
            "action": "write",
            "content": "Jarvis çalışıyor"
        }
    ]
}

Kullanıcı sadece not defterini açmak istiyorsa keyboard kullanma.


12. YOUTUBE'DA VİDEO BULUP AÇMA

Kullanıcı YouTube'da bir video bulup açmak istiyorsa,
arama yaptıktan sonra uygun ilk videoyu aç.

Kullanıcının ayrıca "ilk videoya tıkla" demesini bekleme.

Örnek:

"YouTube'da kedi videolarından birini aç"

{
    "goal": "YouTube'da kedi videolarından birini aç",
    "steps": [
        {
            "tool": "browser",
            "action": "search",
            "target": "youtube kedi videoları"
        },
        {
            "tool": "browser",
            "action": "open_first_video"
        }
    ]
}


13. GOOGLE'DA SONUÇ BULUP AÇMA

Kullanıcı Google'da bir şey arayıp sonuçlardan birini açmak istiyorsa,
arama yaptıktan sonra uygun ilk sonucu aç.

Örnek:

"Google'da Python hakkında bilgi bul ve ilk sonucu aç"

{
    "goal": "Google'da Python hakkında bilgi bul ve ilk sonucu aç",
    "steps": [
        {
            "tool": "browser",
            "action": "search",
            "target": "google Python"
        },
        {
            "tool": "browser",
            "action": "open_first_result"
        }
    ]
}


14. SONUÇ ODAKLI KOMUTLAR

Kullanıcı:

- bul
- ara
- aç
- getir
- göster
- bul ve aç
- ara ve aç

gibi ifadeler kullanabilir.

Kullanıcı gerekli teknik işlemleri söylemek zorunda değildir.

Örneğin:

"Bana YouTube'da güzel bir kedi videosu aç"

isteğinde:

arama yap
+
uygun ilk videoyu aç

adımlarını kendin oluştur.


15. GEREKSİZ COMPUTER KULLANMA

Browser'ın kendi Chrome oturumunu kullanabildiği görevlerde
sadece Chrome'u ayrıca açmak için computer kullanma.

Örneğin:

"Chrome'u aç, YouTube'da kedi videosu ara"

isteğinde:

computer open chrome

ekleme.

Browser kullan.


16. ARAMA MOTORUNU KORU

Kullanıcı Google diyorsa Google kullan.

Kullanıcı YouTube diyorsa YouTube kullan.

Arama motoru açıkça belirtilmişse değiştirme.


17. GOAL ZORUNLU

Her JSON çıktısında goal alanı bulunmalıdır.

goal kullanıcının nihai amacını kısa şekilde anlatmalıdır.


18. BOŞ VE GEREKSİZ STEP EKLEME

Kullanıcının isteği için gerekli olmayan tool veya step ekleme.

Aynı işlemi iki kere yapma.


19. DOĞAL DİLİ ANLA

Kullanıcı:

"bana kedilerle ilgili bir video bul"

derse bunu teknik komut olarak değil,
bir görev olarak değerlendir.

Gerekli araçları kendin seç.


20. VİZYON VE BROWSER ARASINDA TERCİH

Bir web sayfasındaki bilinen sonuç veya video Selenium ile bulunabiliyorsa
browser kullan.

Ekrandaki herhangi bir görsel yazıya doğrudan tıklamak gerekiyorsa
vision kullan.


Kullanıcı isteği:

""" + girdi


    cevap = ai_cevapla(prompt)

    try:

        temiz = cevap.replace("```json", "")
        temiz = temiz.replace("```", "")
        temiz = temiz.strip()

        plan = json.loads(temiz)

        if not isinstance(plan, dict):
            return {
                "goal": girdi,
                "steps": []
            }

        if "goal" not in plan:
            plan["goal"] = girdi

        steps = plan.get("steps", [])

        if not isinstance(steps, list):
            steps = []

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

            if not isinstance(step, dict):
                continue

            tool = step.get("tool")
            action = step.get("action")

            target = str(
                step.get("target", "")
            ).lower().strip()

            # Chrome açma adımını güvenceye al
            if (
                target == "chrome"
                and action == "open"
            ):
                step["tool"] = "computer"

            # Chrome + browser görevi varsa
            # gereksiz Chrome açma adımını kaldır.
            if (
                chrome_ile_browser
                and step.get("tool") == "computer"
                and step.get("action") == "open"
                and str(
                    step.get("target", "")
                ).lower().strip() == "chrome"
            ):
                continue

            yeni_steps.append(step)

        plan["steps"] = yeni_steps

        return plan

    except Exception as e:

        print("PLAN HATASI:", e)
        print("AI CEVABI:", cevap)

        return {
            "goal": girdi,
            "steps": []
        }