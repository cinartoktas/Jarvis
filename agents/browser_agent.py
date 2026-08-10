from tools.browser import siteye_git, google_ara, youtube_ara


SITELER = {
    "google": "https://google.com",
    "youtube": "https://youtube.com",
    "github": "https://github.com",
    "steam": "https://store.steampowered.com"
}


def calistir(target, action="open"):

    if action == "search":

        if "youtube" in target:

            hedef = target.replace("youtube", "").strip()

            youtube_ara(hedef)

            return f"YouTube'da {hedef} aranıyor."


        google_ara(target)

        return f"Google'da {target} aranıyor."


    target = target.lower().strip()

    if target in SITELER:

        siteye_git(SITELER[target])

        return f"{target.capitalize()} açılıyor."


    return f"{target} tanınmıyor."