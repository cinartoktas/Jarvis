from graphs.graph import graph


print("JARVIS v3")
print("Çıkmak için: çık")
print()


# Bekleyen görev
pending_plan = None


while True:

    komut = input("Sen: ")

    # Boş Enter
    if not komut.strip():
        continue


    # Çıkış
    if komut.lower().strip() in [
        "çık",
        "exit",
        "quit"
    ]:

        print("Jarvis kapatılıyor.")
        break


    try:

        # =========================
        # DEVAM ET
        # =========================

        if komut.lower().strip() in [
            "devam et",
            "devam",
            "sürdür"
        ]:

            if pending_plan is None:

                print(
                    "Jarvis: Devam edilecek bekleyen "
                    "bir görev yok."
                )

                continue


            sonuc = graph.invoke({

                "user_input": komut,

                "pending_plan": pending_plan

            })


        # =========================
        # NORMAL KOMUT
        # =========================

        else:

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


        # =========================
        # PENDING PLAN
        # =========================

        pending_plan = sonuc.get(
            "pending_plan"
        )


        # =========================
        # CEVAP
        # =========================

        if isinstance(cevap, list):

            for mesaj in cevap:

                print(
                    "Jarvis:",
                    mesaj
                )

        elif cevap:

            print(
                "Jarvis:",
                cevap
            )

        else:

            print(
                "Jarvis:",
                sonuc
            )


    except Exception as e:

        print("Jarvis hata verdi:")
        print(e)