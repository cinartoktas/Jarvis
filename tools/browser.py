from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote


driver = None


def browser_ac():

    global driver

    # Eski Selenium oturumu kapanmışsa yeniden oluştur
    if driver is not None:

        try:
            driver.current_url

        except Exception:

            try:
                driver.quit()
            except:
                pass

            driver = None


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

    global driver

    try:

        browser = browser_ac()

        browser.get(url)

        return True

    except Exception as e:

        print("Browser Hatası:", e)

        # Eski session'ı temizle
        driver = None

        return False


def google_ara(aranacak):

    global driver

    try:

        browser = browser_ac()

        kelime = quote(aranacak)

        url = f"https://www.google.com/search?q={kelime}"

        browser.get(url)

        return True

    except Exception as e:

        print("Arama Hatası:", e)

        driver = None

        return False


def youtube_ara(aranacak):

    global driver

    try:

        browser = browser_ac()

        kelime = quote(aranacak)

        url = (
            "https://www.youtube.com/results?search_query="
            + kelime
        )

        browser.get(url)

        return True

    except Exception as e:

        print("YouTube Arama Hatası:", e)

        driver = None

        return False