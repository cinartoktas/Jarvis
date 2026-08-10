import pyautogui



def hareket_et(x,y):

    pyautogui.moveTo(
        x,
        y,
        duration=0.5
    )

    return "Fare hareket etti."




def sol_tik():
    import time
    
    time.sleep(0.5)

    pyautogui.click()

    return "Sol tık yapıldı."



def sag_tik():

    pyautogui.rightClick()

    return "Sağ tık yapıldı."



def cift_tik():

    pyautogui.doubleClick()

    return "Çift tık yapıldı."



def scroll_yukari(miktar=500):

    pyautogui.scroll(miktar)

    return "Yukarı kaydırıldı."



def scroll_asagi(miktar=500):

    pyautogui.scroll(-miktar)

    return "Aşağı kaydırıldı."