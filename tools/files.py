from pathlib import Path
import shutil


def masaustu_bul():

    desktop = Path.home() / "OneDrive" / "Desktop"

    if desktop.exists():
        return desktop

    return Path.home() / "Desktop"


def belgeler_bul():

    documents = Path.home() / "OneDrive" / "Documents"

    if documents.exists():
        return documents

    return Path.home() / "Documents"


def indirilenler_bul():

    downloads = Path.home() / "OneDrive" / "Downloads"

    if downloads.exists():
        return downloads

    return Path.home() / "Downloads"



def yolu_duzelt(yol):

    yol = str(yol)

    yol = yol.replace("\\", "/")

    yol = yol.lower()


    if yol.startswith("masaustu/"):

        return masaustu_bul() / yol.replace("masaustu/", "", 1)


    if yol.startswith("belgeler/"):

        return belgeler_bul() / yol.replace("belgeler/", "", 1)


    if yol.startswith("indirilenler/"):

        return indirilenler_bul() / yol.replace("indirilenler/", "", 1)


        return Path(yol)



def dosya_olustur(yol):

    try:

        dosya = yolu_duzelt(yol)

        dosya.parent.mkdir(parents=True, exist_ok=True)

        dosya.touch(exist_ok=True)

        return True, f"{dosya} oluşturuldu."

    except Exception as e:

        return False, str(e)



def dosyaya_yaz(yol, metin):

    try:

        dosya = yolu_duzelt(yol)

        dosya.parent.mkdir(parents=True, exist_ok=True)

        with open(dosya, "w", encoding="utf-8") as f:
            f.write(metin)

        return True, f"{dosya} dosyasına yazıldı."

    except Exception as e:

        return False, str(e)



def dosya_oku(yol):

    try:

        dosya = yolu_duzelt(yol)

        if not dosya.exists():
            return False, "Dosya bulunamadı."

        with open(dosya, "r", encoding="utf-8") as f:
            return True, f.read()

    except Exception as e:

        return False, str(e)



def dosya_sil(yol):

    try:

        dosya = yolu_duzelt(yol)

        if not dosya.exists():
            return False, "Dosya bulunamadı."

        dosya.unlink()

        return True, f"{dosya} silindi."

    except Exception as e:

        return False, str(e)



def dosya_tasi(kaynak, hedef):

    try:

        kaynak = yolu_duzelt(kaynak)
        hedef = yolu_duzelt(hedef)

        hedef.parent.mkdir(parents=True, exist_ok=True)

        shutil.move(str(kaynak), str(hedef))

        return True, f"{kaynak} -> {hedef}"

    except Exception as e:

        return False, str(e)



def klasor_olustur(yol):

    try:

        klasor = yolu_duzelt(yol)

        klasor.mkdir(parents=True, exist_ok=True)

        return True, f"{klasor} oluşturuldu."

    except Exception as e:

        return False, str(e)



def klasor_sil(yol):

    try:

        klasor = yolu_duzelt(yol)

        shutil.rmtree(klasor)

        return True, f"{klasor} silindi."

    except Exception as e:

        return False, str(e)