from agents.vision_agent import bul
from tools.mouse import hareket_et, sol_tik

sonuc = bul("Google")

if sonuc:

    print("Bulundu:", sonuc)

    hareket_et(
        sonuc["x"],
        sonuc["y"]
    )

    sol_tik()

else:

    print("Bulunamadı.")