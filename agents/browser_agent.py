from tools.browser import siteye_git, google_ara, youtube_ara


SITELER = {
    "google": "https://google.com",
    "youtube": "https://youtube.com",
    "github": "https://github.com",
    "steam": "https://store.steampowered.com"
}


def calistir(target, action="open"):

    target = target.lower().strip()

    if action == "search":

        # YouTube araması
        if target.startswith("youtube "):

            hedef = target.replace(
                "youtube",
                "",
                1
            ).strip()

            youtube_ara(hedef)

            return f"YouTube'da {hedef} aranıyor."

        # Google araması
        if target.startswith("google "):

            hedef = target.replace(
                "google",
                "",
                1
            ).strip()

            google_ara(hedef)

            return f"Google'da {hedef} aranıyor."

        # Arama motoru belirtilmemişse Google kullan
        google_ara(target)

        return f"Google'da {target} aranıyor."

    if target in SITELER:

        siteye_git(SITELER[target])

        return f"{target.capitalize()} açılıyor."

    return f"{target} tanınmıyor."