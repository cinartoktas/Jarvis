import ctypes
import subprocess
import time

import psutil

from tools.appfinder import program_bul


user32 = ctypes.windll.user32

SW_RESTORE = 9
SW_SHOW = 5


def _pencereyi_one_getir(pid, timeout=5):

    bulunan_pencere = []

    ENUM_WINDOWS_PROC = ctypes.WINFUNCTYPE(
        ctypes.c_bool,
        ctypes.c_void_p,
        ctypes.c_void_p,
    )

    def pencere_bul(hwnd, lparam):

        pencere_pid = ctypes.c_ulong()

        user32.GetWindowThreadProcessId(
            hwnd,
            ctypes.byref(pencere_pid)
        )

        gorunur = user32.IsWindowVisible(hwnd)
        baslik_uzunlugu = user32.GetWindowTextLengthW(hwnd)

        if (
            pencere_pid.value == pid
            and gorunur
            and baslik_uzunlugu > 0
        ):
            bulunan_pencere.append(hwnd)
            return False

        return True

    callback = ENUM_WINDOWS_PROC(pencere_bul)

    bitis = time.time() + timeout

    while time.time() < bitis:

        bulunan_pencere.clear()

        user32.EnumWindows(
            callback,
            0
        )

        if bulunan_pencere:

            hwnd = bulunan_pencere[0]

            # Pencereyi görünür ve normal hale getir
            user32.ShowWindow(
                hwnd,
                SW_RESTORE
            )

            user32.ShowWindow(
                hwnd,
                SW_SHOW
            )

            # Mevcut ve hedef pencerenin thread'lerini al
            aktif_pencere = user32.GetForegroundWindow()

            aktif_thread = user32.GetWindowThreadProcessId(
                aktif_pencere,
                None
            )

            hedef_thread = user32.GetWindowThreadProcessId(
                hwnd,
                None
            )

            # Farklı thread ise geçici olarak bağla
            if aktif_thread != hedef_thread:

                user32.AttachThreadInput(
                    aktif_thread,
                    hedef_thread,
                    True
                )

            # Pencereyi öne getir
            user32.BringWindowToTop(hwnd)
            user32.SetForegroundWindow(hwnd)
            user32.SetFocus(hwnd)

            # Thread bağlantısını kaldır
            if aktif_thread != hedef_thread:

                user32.AttachThreadInput(
                    aktif_thread,
                    hedef_thread,
                    False
                )

            return True

        time.sleep(0.1)

    return False


def program_ac(program):

    yol = program_bul(program)

    if not yol:
        return f"{program} bulunamadı."

    try:

        islem = subprocess.Popen(yol)

        # Hesap makinesi ve Chrome birden fazla
        # process kullanabildiği için Popen PID'si
        # gerçek pencereyle eşleşmeyebilir.
        if program.lower() in ["calc", "chrome"]:

            time.sleep(1)

            return f"{program} açıldı."

        # Diğer programlarda normal pencere sistemi
        if _pencereyi_one_getir(islem.pid):

            return f"{program} açıldı."

        return f"{program} açıldı fakat penceresi bulunamadı."

    except Exception as e:

        print("Program açma hatası:", e)

        return f"{program} açılamadı."


def program_kapat(program):

    kapandi = False

    for islem in psutil.process_iter(["name"]):

        try:

            isim = islem.info["name"]

            if (
                isim
                and program.lower() in isim.lower()
            ):

                islem.kill()
                kapandi = True

        except Exception:
            pass

    if kapandi:

        return f"{program} kapatıldı."

    return f"{program} çalışmıyor."