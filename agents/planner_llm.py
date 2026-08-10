import json

from ai import ai_cevapla


SYSTEM_PROMPT = """
Sen Jarvis Planner'sın.

Görevin kullanıcı komutunu analiz edip SADECE JSON döndürmektir.

Format:

{
  "steps":[
    {
      "tool":"computer",
      "action":"open",
      "target":"chrome"
    }
  ]
}

Kurallar:

- Sadece JSON döndür.
- Açıklama yazma.
- Markdown kullanma.
- ```json yazma.
- tool değerleri:
  computer
  browser
  files
  keyboard
  internet

Örnek:

Kullanıcı:
Chrome'u aç

Cevap:

{
 "steps":[
   {
     "tool":"computer",
     "action":"open",
     "target":"chrome"
   }
 ]
}
"""


def planla(komut):

    cevap = ai_cevapla(
        komut,
        sistem_mesaji=SYSTEM_PROMPT
    )

    try:
        return json.loads(cevap)

    except Exception:

        return {
            "steps":[]
        }