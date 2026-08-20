from openai import OpenAI


client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)


MODEL = "qwen3:4b-instruct"


def ai_cevapla(mesaj):

    cevap = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Sen Jarvis isimli gelişmiş yapay zeka asistanısın. "
                    "Her zaman Türkçe cevap ver. "
                    "Kısa, doğru ve yardımcı ol."
                )
            },
            {
                "role": "user",
                "content": mesaj
            }
        ],
        temperature=0,

        # Qwen3 düşünme modunu kapat.
        # Jarvis'in görevleri için hızlı cevap daha önemli.
        extra_body={
            "think": False
        }
    )

    return cevap.choices[0].message.content