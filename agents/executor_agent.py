def execute(plan):

    cevaplar = []

    try:

        steps = plan.get("steps", [])

        # Daha önce yarım kalmış step bilgisi varsa
        start_index = plan.get("_start_index", 0)

        steps = plan.get("steps", [])

        # Daha önce yarım kalmış görev varsa
        # kaldığımız step'ten devam et.
        start_index = plan.get("_start_index", 0)

        for index in range(start_index, len(steps)):

            step = steps[index]

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

                        if sonuc.get("success") is False:

                            cevaplar.append(
                                sonuc.get(
                                    "error",
                                    "Bilgisayar işlemi başarısız oldu."
                                )
                            )

                            return {
                                "response": cevaplar,
                                "pending_plan": {
                                    "steps": steps,
                                    "_start_index": index
                                }
                            }

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

                        if sonuc.get("success") is False:

                            cevaplar.append(
                                sonuc.get(
                                    "error",
                                    "Bilgisayar işlemi başarısız oldu."
                                )
                            )

                            return {
                                "response": cevaplar,
                                "pending_plan": {
                                    "steps": steps,
                                    "_start_index": index
                                }
                            }

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

                        if sonuc.get("success") is False:

                            cevaplar.append(
                                sonuc.get(
                                    "error",
                                    "Klavye işlemi başarısız oldu."
                                )
                            )

                            return {
                                "response": cevaplar,
                                "pending_plan": {
                                    "steps": steps,
                                    "_start_index": index
                                }
                            }

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

                        if sonuc.get("success") is False:

                            cevaplar.append(
                                sonuc.get(
                                    "error",
                                    "Ekrandaki yazıya tıklanamadı."
                                )
                            )

                            return {
                                "response": cevaplar,
                                "pending_plan": {
                                    "steps": steps,
                                    "_start_index": index
                                }
                            }

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
            # BROWSER
            # =========================

            elif tool == "browser":

                from agents.browser_agent import calistir

                sonuc = calistir(
                    target,
                    action
                )

                if isinstance(sonuc, dict):

                    # Google robot doğrulaması
                    if sonuc.get("robot_verification"):

                        cevaplar.append(
                            sonuc.get(
                                "error",
                                "Google robot doğrulaması gerekiyor."
                            )
                        )

                        return {
                            "response": cevaplar,
                            "pending_plan": {
                                "steps": steps,
                                "_start_index": index
                            }
                        }


                    # Browser işlemi başarısız oldu
                    if sonuc.get("success") is False:

                        cevaplar.append(
                            sonuc.get(
                                "error",
                                sonuc.get(
                                    "message",
                                    str(sonuc)
                                )
                            )
                        )

                        return {
                            "response": cevaplar,
                            "pending_plan": {
                                "steps": steps,
                                "_start_index": index
                            }
                        }


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

                        if sonuc.get("success") is False:

                            cevaplar.append(
                                sonuc.get(
                                    "error",
                                    "Mouse işlemi başarısız oldu."
                                )
                            )

                            return {
                                "response": cevaplar,
                                "pending_plan": {
                                    "steps": steps,
                                    "_start_index": index
                                }
                            }

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

                return {
                    "response": cevaplar,
                    "pending_plan": {
                        "steps": steps,
                        "_start_index": index
                    }
                }


        # =========================
        # TÜM STEPLER TAMAMLANDI
        # =========================

        return {
            "response": cevaplar,
            "pending_plan": None
        }


    # =========================
    # GENEL HATA
    # =========================

    except Exception as e:

        return {
            "response": [
                f"Executor hata: {str(e)}"
            ],
            "pending_plan": {
                "steps": steps,
                "_start_index": start_index
            }
        }