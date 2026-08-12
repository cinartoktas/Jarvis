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

            youtube_ara(hedef)

            aktif_site = "youtube"

            return f"YouTube'da {hedef} aranıyor."

        # Açıkça Google belirtilmişse Google'da ara.
        if target.startswith("google "):

            hedef = target.replace(
                "google",
                "",
                1
            ).strip()

            google_ara(hedef)

            aktif_site = "google"

            return f"Google'da {hedef} aranıyor."

        # Arama motoru belirtilmemişse,
        # en son açılan siteyi kullan.
        if aktif_site == "youtube":

            youtube_ara(target)

            return f"YouTube'da {target} aranıyor."

        if aktif_site == "google":

            google_ara(target)

            return f"Google'da {target} aranıyor."

        # Hiçbir site açılmamışsa varsayılan Google.
        google_ara(target)

        aktif_site = "google"

        return f"Google'da {target} aranıyor."

    if target in SITELER:

        siteye_git(SITELER[target])

        aktif_site = target

        return f"{target.capitalize()} açılıyor."

    return f"{target} tanınmıyor."