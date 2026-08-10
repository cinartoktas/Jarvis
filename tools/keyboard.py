from pywinauto import Application
import time


def yazi_yaz(metin):

    try:
        # Not Defteri'ne bağlan
        app = Application(backend="uia").connect(title_re=".*Not Defteri.*")

        pencere = app.top_window()

        pencere.set_focus()

        time.sleep(0.5)

        # Edit alanını bul
        edit = pencere.child_window(control_type="Edit")

        edit.type_keys(
            metin,
            with_spaces=True,
            set_foreground=True
        )

        return "Yazı yazıldı."

    except Exception as e:
        return f"Hata: {e}"