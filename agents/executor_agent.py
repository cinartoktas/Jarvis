def execute(plan):

    cevaplar = []

    try:

        steps = plan.get("steps", [])

        for step in steps:

            tool = step.get("tool")
            action = step.get("action")
            target = step.get("target", "")
            content = step.get("content", "")

            # =========================
            # COMPUTER
            # =========================

            if tool == "computer":

                from agents.computer_agent import calistir

                if action == "open":

                    sonuc = calistir(target)

                    cevaplar.append(
                        str(sonuc)
                    )

                elif action == "close":

                    sonuc = calistir(
                        target + " kapat"
                    )

                    cevaplar.append(
                        str(sonuc)
                    )


            # =========================
            # KEYBOARD
            # =========================

            elif tool == "keyboard":

                from agents.keyboard_agent import yaz

                if action == "write":

                    # Planner'dan gelen gerçek yazıyı kullan
                    metin = content

                    sonuc = yaz(metin)

                    cevaplar.append(
                        str(sonuc)
                    )


            # =========================
            # VISION
            # =========================

            elif tool == "vision":

                from agents.vision_agent import (
                    ekran_oku,
                    tikla_yazi
                )

                if action == "read":

                    sonuc = ekran_oku()

                    cevaplar.append(
                        sonuc.get(
                            "text",
                            "Yazı bulunamadı"
                        )
                    )

                elif action == "click_text":

                    sonuc = tikla_yazi(target)

                    cevaplar.append(
                        str(sonuc)
                    )


            # =========================
            # BROWSER
            # =========================

            elif tool == "browser":

                from agents.browser_agent import calistir

                sonuc = calistir(
                    target,
                    action
                )

                cevaplar.append(
                    str(sonuc)
                )


        return cevaplar


    except Exception as e:

        return [
            f"Executor hata: {str(e)}"
        ]