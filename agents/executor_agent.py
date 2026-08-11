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

                    if isinstance(sonuc, dict):
                        mesaj = sonuc.get(
                            "message",
                            sonuc.get("response", str(sonuc))
                        )
                    else:
                        mesaj = str(sonuc)

                    cevaplar.append(mesaj)

                elif action == "close":

                    sonuc = calistir(
                        target + " kapat"
                    )

                    if isinstance(sonuc, dict):
                        mesaj = sonuc.get(
                            "message",
                            sonuc.get("response", str(sonuc))
                        )
                    else:
                        mesaj = str(sonuc)

                    cevaplar.append(mesaj)


            # =========================
            # KEYBOARD
            # =========================

            elif tool == "keyboard":

                from agents.keyboard_agent import yaz

                if action == "write":

                    metin = content

                    sonuc = yaz(metin)

                    if isinstance(sonuc, dict):
                        mesaj = sonuc.get(
                            "message",
                            sonuc.get("response", str(sonuc))
                        )
                    else:
                        mesaj = str(sonuc)

                    cevaplar.append(mesaj)


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

                    if isinstance(sonuc, dict):
                        mesaj = sonuc.get(
                            "text",
                            "Yazı bulunamadı"
                        )
                    else:
                        mesaj = str(sonuc)

                    cevaplar.append(mesaj)

                elif action == "click_text":

                    sonuc = tikla_yazi(target)

                    if isinstance(sonuc, dict):
                        mesaj = sonuc.get(
                            "message",
                            sonuc.get("response", str(sonuc))
                        )
                    else:
                        mesaj = str(sonuc)

                    cevaplar.append(mesaj)


            # =========================
            # BROWSER
            # =========================

            elif tool == "browser":

                from agents.browser_agent import calistir

                sonuc = calistir(
                    target,
                    action
                )

                if isinstance(sonuc, dict):
                    mesaj = sonuc.get(
                        "message",
                        sonuc.get("response", str(sonuc))
                    )
                else:
                    mesaj = str(sonuc)

                cevaplar.append(mesaj)


        return cevaplar


    except Exception as e:

        return [
            f"Executor hata: {str(e)}"
        ]