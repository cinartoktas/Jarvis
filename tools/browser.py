from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote


driver = None


def browser_ac():

    global driver

    if driver is None:

        options = webdriver.ChromeOptions()

        options.add_experimental_option(
            "detach",
            True
        )

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=options
        )

    return driver


def siteye_git(url):

    try:

        browser = browser_ac()

        browser.get(url)

        return True

    except Exception as e:

        print("Browser Hatası:", e)

        return False


def google_ara(aranacak):

    try:

        browser = browser_ac()

        kelime = quote(aranacak)

        url = f"https://www.google.com/search?q={kelime}"

        browser.get(url)

        return True

    except Exception as e:

        print("Arama Hatası:", e)

        return False
    

def youtube_ara(aranacak):

    try:

        browser = browser_ac()

        from urllib.parse import quote

        kelime = quote(aranacak)

        url = f"https://www.youtube.com/results?search_query={kelime}"

        browser.get(url)

        return True

    except Exception as e:

        print("YouTube Arama Hatası:", e)

        return False