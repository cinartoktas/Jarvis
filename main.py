from graphs.graph import graph


print("JARVIS v3")
print("Çıkmak için: çık")
print()


while True:

    komut = input("Sen: ")

    # Boş Enter'a basılırsa hiçbir şey yapma
    if not komut.strip():
        continue

    # Çıkış
    if komut.lower().strip() in ["çık", "exit", "quit"]:
        print("Jarvis kapatılıyor.")
        break

    try:

        sonuc = graph.invoke({
            "user_input": komut
        })

        cevap = sonuc.get(
            "response",
            sonuc.get(
                "result",
                sonuc.get(
                    "output",
                    sonuc.get(
                        "cevap",
                        ""
                    )
                )
            )
        )

        if cevap:
            print("Jarvis:", cevap)
        else:
            print("Jarvis:", sonuc)

    except Exception as e:

        print("Jarvis hata verdi:")
        print(e)