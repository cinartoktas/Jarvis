from tools.files import (
    dosya_olustur,
    dosyaya_yaz,
    dosya_oku,
    dosya_sil,
    dosya_tasi,
    klasor_olustur,
    klasor_sil
)


def calistir(action, target, content=None):

    if action == "create_file":
        return dosya_olustur(target)

    elif action == "write_file":
        return dosyaya_yaz(target, content)

    elif action == "read_file":
        return dosya_oku(target)

    elif action == "delete_file":
        return dosya_sil(target)

    elif action == "move_file":
        return dosya_tasi(
            target["source"],
            target["destination"]
        )

    elif action == "create_folder":
        return klasor_olustur(target)

    elif action == "delete_folder":
        return klasor_sil(target)

    else:
        return False, "Bilinmeyen dosya işlemi."