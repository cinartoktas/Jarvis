from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
import time



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


def robot_dogrulamasi_var_mi(browser):

    try:

        url = browser.current_url.lower()
        baslik = browser.title.lower()

        # Google bizi /sorry/ sayfasına yönlendirdiyse
        if "google.com/sorry" in url:
            return True

        if "/sorry/" in url:
            return True

        # Gerçek doğrulama sayfası başlıkları
        baslik_anahtarlari = [
            "unusual traffic",
            "verify you are human",
            "are you a robot"
        ]

        for anahtar in baslik_anahtarlari:

            if anahtar in baslik:
                return True

        # Görünen sayfa metnini kontrol et
        try:

            gorunen_metin = browser.find_element(
                "tag name",
                "body"
            ).text.lower()

        except Exception:

            gorunen_metin = ""

        metin_anahtarlari = [
            "unusual traffic",
            "verify you are human",
            "i'm not a robot",
            "are you a robot",
            "captcha verification"
        ]

        for anahtar in metin_anahtarlari:

            if anahtar in gorunen_metin:
                return True

        return False

    except Exception:

        return False


def siteye_git(url):

    global driver

    try:

        browser = browser_ac()

        browser.get(url)

        return True

    except Exception as e:

        print("Browser Hatası:", e)

        driver = None

        return False


def google_ara(aranacak):

    global driver

    try:

        browser = browser_ac()

        time.sleep(2)

        kelime = quote(aranacak)

        url = f"https://www.google.com/search?q={kelime}"

        browser.get(url)

        if robot_dogrulamasi_var_mi(browser):

            return {
                "success": False,
                "error": "Google robot doğrulaması istiyor.",
                "robot_verification": True
            }

        return {
            "success": True,
            "robot_verification": False
        }

    except Exception as e:

        print("Arama Hatası:", e)

        driver = None

        return {
            "success": False,
            "error": f"Google araması başarısız oldu: {str(e)}",
            "robot_verification": False
        }


def duckduckgo_ara(aranacak):

    global driver

    try:

        browser = browser_ac()

        kelime = quote(aranacak)

        url = (
            "https://duckduckgo.com/?q="
            + kelime
        )

        browser.get(url)

        time.sleep(2)

        return {
            "success": True,
            "message": f"Alternatif aramada {aranacak} aranıyor."
        }

    except Exception as e:

        print("DuckDuckGo Arama Hatası:", e)

        driver = None

        return {
            "success": False,
            "error": f"Alternatif arama başarısız: {str(e)}"
        }


def duckduckgo_ilk_sonuc_ac():

    global driver

    try:

        browser = browser_ac()

        time.sleep(2)

        sonuclar = browser.find_elements(
            "css selector",
            "a[data-testid='result-title-a']"
        )

        for sonuc in sonuclar:

            try:

                if not sonuc.is_displayed():
                    continue

                href = sonuc.get_attribute("href")

                if not href:
                    continue

                baslik = sonuc.text.strip()

                browser.execute_script(
                    "arguments[0].click();",
                    sonuc
                )

                return {
                    "success": True,
                    "message": (
                        f"'{baslik}' sonucu açıldı."
                    )
                }

            except Exception:
                continue

        return {
            "success": False,
            "error": "Alternatif aramada sonuç bulunamadı."
        }

    except Exception as e:

        return {
            "success": False,
            "error": (
                f"Alternatif sonuç açma hatası: {str(e)}"
            )
        }


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

        time.sleep(2)

        return {
            "success": True
        }

    except Exception as e:

        print("YouTube Arama Hatası:", e)

        driver = None

        return {
            "success": False,
            "error": f"YouTube araması başarısız oldu: {str(e)}"
        }


def youtube_ilk_video_ac():

    global driver

    try:

        browser = browser_ac()

        time.sleep(2)

        videolar = browser.find_elements(
            "css selector",
            "a#video-title"
        )

        for video in videolar:

            try:

                if not video.is_displayed():
                    continue

                href = video.get_attribute("href")

                if not href:
                    continue

                baslik = video.text.strip()

                if not baslik:
                    continue

                browser.execute_script(
                    "arguments[0].click();",
                    video
                )

                return {
                    "success": True,
                    "message": f"'{baslik}' videosu açıldı.",
                    "title": baslik
                }

            except Exception:
                continue

        return {
            "success": False,
            "error": "YouTube'da uygun video bulunamadı."
        }

    except Exception as e:

        return {
            "success": False,
            "error": f"YouTube video açma hatası: {str(e)}"
        }


def google_ilk_sonuc_ac():

    global driver

    try:

        browser = browser_ac()

        time.sleep(2)

        # Google sonuç sayfasındaki gerçek sonuç linklerini bul
        sonuclar = browser.find_elements(
            "css selector",
            "a"
        )

        for sonuc in sonuclar:

            try:

                if not sonuc.is_displayed():
                    continue

                href = sonuc.get_attribute("href")

                if not href:
                    continue

                href = href.strip()

                # Google'ın kendi navigasyon linklerini atla
                if (
                    href.startswith("https://www.google.com/")
                    or
                    href.startswith("https://www.google.com.tr/")
                ):
                    continue

                # Google servis linklerini atla
                if (
                    "/search?" in href
                    or
                    "/preferences" in href
                    or
                    "/advanced_search" in href
                ):
                    continue

                # Gerçek dış site linki bulduk
                browser.execute_script(
                    "arguments[0].click();",
                    sonuc
                )

                return {
                    "success": True,
                    "message": "Google'daki ilk sonuç açıldı."
                }

            except Exception:
                continue

        return {
            "success": False,
            "error": "Google'da uygun sonuç bulunamadı."
        }

    except Exception as e:

        return {
            "success": False,
            "error": f"Google sonuç açma hatası: {str(e)}"
        }

