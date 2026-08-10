import subprocess
import psutil

from tools.appfinder import program_bul


def program_ac(program):

    yol = program_bul(program)

    if yol:
        subprocess.Popen(yol)
        return f"{program} açıldı."

    return f"{program} bulunamadı."



def program_kapat(program):

    kapandi = False

    for islem in psutil.process_iter(["name"]):

        try:
            isim = islem.info["name"]

            if isim and program.lower() in isim.lower():

                islem.kill()
                kapandi = True

        except:
            pass


    if kapandi:
        return f"{program} kapatıldı."

    return f"{program} çalışmıyor."