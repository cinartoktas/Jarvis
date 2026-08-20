from graphs.graph import graph


print("JARVIS v3")
print("Çıkmak için: çık")
print()


# =========================================================
# BEKLEYEN GÖREV
# =========================================================

pending_plan = None


while True:

    komut = input("Sen: ")

    # =====================================================
    # BOŞ ENTER
    # =====================================================

    if not komut.strip():
        continue


    # =====================================================
    # ÇIKIŞ
    # =====================================================

    if komut.lower().strip() in [
        "çık",
        "exit",
        "quit"
    ]:

        print("Jarvis kapatılıyor.")
        break


    try:

        komut_temiz = komut.lower().strip()


        # =================================================
        # DEVAM ET
        # =================================================

        if komut_temiz in [
            "devam et",
            "devam",
            "sürdür",
            "surdur"
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


        # =================================================
        # NORMAL KOMUT
        # =================================================

        else:

            sonuc = graph.invoke({

                "user_input": komut

            })


        # =================================================
        # CEVABI AL
        # =================================================

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


        # =================================================
        # PENDING PLAN
        # =================================================

        # Graph gerçekten pending_plan döndürdüyse
        # mevcut değeri güncelle.
        if "pending_plan" in sonuc:

            pending_plan = sonuc["pending_plan"]


        # =================================================
        # CEVABI YAZDIR
        # =================================================

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