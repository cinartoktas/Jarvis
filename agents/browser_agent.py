from tools.browser import siteye_git, google_ara, youtube_ara


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

    if action == "search":

        # Açıkça YouTube belirtilmişse YouTube'da ara.
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

        # Açıkça Google belirtilmişse Google'da ara.
        if target.startswith("google "):

            hedef = target.replace(
                "google",
                "",
                1
            ).strip()

            sonuc = google_ara(hedef)

            if not sonuc.get("success", False):

                if sonuc.get("robot_verification"):

                    return {
                        "success": False,
                        "error": (
                            "Google robot doğrulaması istiyor. "
                            "Lütfen Chrome'daki doğrulamayı tamamla."
                        ),
                        "robot_verification": True
                    }

                return sonuc

            aktif_site = "google"

            return {
                "success": True,
                "message": f"Google'da {hedef} aranıyor."
            }

        # Arama motoru belirtilmemişse
        # en son açılan siteyi kullan.
        if aktif_site == "youtube":

            sonuc = youtube_ara(target)

            if not sonuc.get("success", False):
                return sonuc

            return {
                "success": True,
                "message": f"YouTube'da {target} aranıyor."
            }

        if aktif_site == "google":

            sonuc = google_ara(target)

            if not sonuc.get("success", False):

                if sonuc.get("robot_verification"):

                    return {
                        "success": False,
                        "error": (
                            "Google robot doğrulaması istiyor. "
                            "Lütfen Chrome'daki doğrulamayı tamamla."
                        ),
                        "robot_verification": True
                    }

                return sonuc

            return {
                "success": True,
                "message": f"Google'da {target} aranıyor."
            }

        # Hiçbir site açılmamışsa varsayılan Google.
        sonuc = google_ara(target)

        if not sonuc.get("success", False):

            if sonuc.get("robot_verification"):

                return {
                    "success": False,
                    "error": (
                        "Google robot doğrulaması istiyor. "
                        "Lütfen Chrome'daki doğrulamayı tamamla."
                    ),
                    "robot_verification": True
                }

            return sonuc

        aktif_site = "google"

        return {
            "success": True,
            "message": f"Google'da {target} aranıyor."
        }

    if target in SITELER:

        sonuc = siteye_git(SITELER[target])

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