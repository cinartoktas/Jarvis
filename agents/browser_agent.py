from tools.browser import (
    siteye_git,
    google_ara,
    youtube_ara,
    youtube_ilk_video_ac,
    google_ilk_sonuc_ac,
    duckduckgo_ara,
    duckduckgo_ilk_sonuc_ac
)


SITELER = {
    "google": "https://google.com",
    "youtube": "https://youtube.com",
    "github": "https://github.com",
    "steam": "https://store.steampowered.com"
}


# En son açılan siteyi takip eder.
aktif_site = None


def calistir(target, action="open"):

    global aktif_site

    target = target.lower().strip()


    # =========================
    # GOOGLE İLK SONUÇ
    # =========================

    if action == "open_first_result":

        if aktif_site == "duckduckgo":

            sonuc = duckduckgo_ilk_sonuc_ac()

            if isinstance(sonuc, dict):
                return sonuc

            return {
                "success": False,
                "error": "Alternatif arama sonucu açılamadı."
            }

        sonuc = google_ilk_sonuc_ac()

        if isinstance(sonuc, dict):

            if sonuc.get("robot_verification"):

                # Google engellediyse alternatif arama sonucunu aç.
                sonuc = duckduckgo_ilk_sonuc_ac()

                if isinstance(sonuc, dict):
                    return sonuc

                return {
                    "success": False,
                    "error": "Alternatif arama sonucu açılamadı."
                }

            return sonuc

        return {
            "success": False,
            "error": "Google sonucu açılamadı."
        }


    # =========================
    # YOUTUBE İLK VİDEO
    # =========================

    if action == "open_first_video":

        sonuc = youtube_ilk_video_ac()

        if isinstance(sonuc, dict):
            return sonuc

        return {
            "success": False,
            "error": "YouTube videosu açılamadı."
        }


    # =========================
    # ARAMA
    # =========================

    if action == "search":


        # -------------------------
        # YOUTUBE
        # -------------------------

        if target.startswith("youtube "):

            hedef = target.replace(
                "youtube",
                "",
                1
            ).strip()

            sonuc = youtube_ara(hedef)

            if not sonuc.get("success", False):
                return sonuc

            aktif_site = "youtube"

            return {
                "success": True,
                "message": f"YouTube'da {hedef} aranıyor."
            }


        # -------------------------
        # GOOGLE
        # -------------------------

        if target.startswith("google "):

            hedef = target.replace(
                "google",
                "",
                1
            ).strip()

            sonuc = google_ara(hedef)

            if not sonuc.get("success", False):

                if sonuc.get("robot_verification"):

                    # Google engellediyse DuckDuckGo'ya geç.
                    alternatif = duckduckgo_ara(hedef)

                    if not alternatif.get("success", False):
                        return alternatif

                    aktif_site = "duckduckgo"

                    return {
                        "success": True,
                        "message": (
                            f"Google doğrulama istedi. "
                            f"Alternatif aramada {hedef} aranıyor."
                        ),
                        "fallback": True
                    }

                return sonuc

            aktif_site = "google"

            return {
                "success": True,
                "message": f"Google'da {hedef} aranıyor."
            }


        # -------------------------
        # AKTİF SITE YOUTUBE
        # -------------------------

        if aktif_site == "youtube":

            sonuc = youtube_ara(target)

            if not sonuc.get("success", False):
                return sonuc

            return {
                "success": True,
                "message": f"YouTube'da {target} aranıyor."
            }


        # -------------------------
        # AKTİF SITE GOOGLE
        # -------------------------

        if aktif_site == "google":

            sonuc = google_ara(target)

            if not sonuc.get("success", False):

                if sonuc.get("robot_verification"):

                    alternatif = duckduckgo_ara(target)

                    if not alternatif.get("success", False):
                        return alternatif

                    aktif_site = "duckduckgo"

                    return {
                        "success": True,
                        "message": (
                            f"Google doğrulama istedi. "
                            f"Alternatif aramada {target} aranıyor."
                        ),
                        "fallback": True
                    }

                return sonuc

            return {
                "success": True,
                "message": f"Google'da {target} aranıyor."
            }


        # -------------------------
        # AKTİF SITE DUCKDUCKGO
        # -------------------------

        if aktif_site == "duckduckgo":

            sonuc = duckduckgo_ara(target)

            if not sonuc.get("success", False):
                return sonuc

            return {
                "success": True,
                "message": f"Alternatif aramada {target} aranıyor."
            }


        # -------------------------
        # VARSAYILAN GOOGLE
        # -------------------------

        sonuc = google_ara(target)

        if not sonuc.get("success", False):

            if sonuc.get("robot_verification"):

                alternatif = duckduckgo_ara(target)

                if not alternatif.get("success", False):
                    return alternatif

                aktif_site = "duckduckgo"

                return {
                    "success": True,
                    "message": (
                        f"Google doğrulama istedi. "
                        f"Alternatif aramada {target} aranıyor."
                    ),
                    "fallback": True
                }

            return sonuc

        aktif_site = "google"

        return {
            "success": True,
            "message": f"Google'da {target} aranıyor."
        }


    # =========================
    # SITE AÇ
    # =========================

    if target in SITELER:

        sonuc = siteye_git(
            SITELER[target]
        )

        if not sonuc:

            return {
                "success": False,
                "error": f"{target} açılamadı."
            }

        aktif_site = target

        return {
            "success": True,
            "message": f"{target.capitalize()} açılıyor."
        }


    return {
        "success": False,
        "error": f"{target} tanınmıyor."
    }