import pygetwindow as gw
import time

def pencereyi_one_getir(isim):
    for pencere in gw.getAllWindows():
        if isim.lower() in pencere.title.lower():
            if pencere.isMinimized:
                pencere.restore()

            pencere.activate()
            time.sleep(1)
            return True

    return False