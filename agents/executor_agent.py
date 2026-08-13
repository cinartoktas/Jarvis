def execute(plan):

    cevaplar = []

    try:

        steps = plan.get("steps", [])
        goal = plan.get("goal", "")

        for index, step in enumerate(steps):

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
                            sonuc.get(
                                "response",
                                str(sonuc)
                            )
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
                            sonuc.get(
                                "response",
                                str(sonuc)
                            )
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

                    sonuc = yaz(content)

                    if isinstance(sonuc, dict):
                        mesaj = sonuc.get(
                            "message",
                            sonuc.get(
                                "response",
                                str(sonuc)
                            )
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
                            sonuc.get(
                                "error",
                                sonuc.get(
                                    "response",
                                    str(sonuc)
                                )
                            )
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

                # Google robot doğrulaması
                if isinstance(sonuc, dict):

                    if sonuc.get("robot_verification"):

                        mesaj = sonuc.get(
                            "error",
                            "Google robot doğrulaması gerekiyor."
                        )

                        cevaplar.append(mesaj)

                        # Kalan adımları sakla
                        kalan_adimlar = steps[index:]

                        pending_plan = {
                            "goal": goal,
                            "steps": kalan_adimlar
                        }

                        return {
                            "responses": cevaplar,
                            "pending_plan": pending_plan
                        }

                if isinstance(sonuc, dict):

                    if sonuc.get("success") is False:

                        mesaj = sonuc.get(
                            "error",
                            sonuc.get(
                                "message",
                                str(sonuc)
                            )
                        )

                    else:

                        mesaj = sonuc.get(
                            "message",
                            sonuc.get(
                                "response",
                                str(sonuc)
                            )
                        )

                else:

                    mesaj = str(sonuc)

                cevaplar.append(mesaj)


            # =========================
            # MOUSE
            # =========================

            elif tool == "mouse":

                from agents.mouse_agent import tikla

                if action == "click":

                    sonuc = tikla(target)

                    if isinstance(sonuc, dict):

                        mesaj = sonuc.get(
                            "message",
                            sonuc.get(
                                "error",
                                sonuc.get(
                                    "response",
                                    str(sonuc)
                                )
                            )
                        )

                    else:

                        mesaj = str(sonuc)

                    cevaplar.append(mesaj)


            # =========================
            # BİLİNMEYEN TOOL
            # =========================

            else:

                cevaplar.append(
                    f"Bilinmeyen tool: {tool}"
                )


        # Her şey tamamlandı
        return {
            "responses": cevaplar,
            "pending_plan": None
        }


    except Exception as e:

        return {
            "responses": [
                f"Executor hata: {str(e)}"
            ],
            "pending_plan": None
        }