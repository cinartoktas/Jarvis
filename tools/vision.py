import mss
import numpy as np
import cv2
import easyocr


reader = easyocr.Reader(
    ["tr","en"]
)



def ekrani_oku():


    with mss.mss() as sct:


        ekran = sct.monitors[1]


        img = np.array(
            sct.grab(ekran)
        )


    img = cv2.cvtColor(
        img,
        cv2.COLOR_BGRA2BGR
    )


    sonuc = reader.readtext(img)


    veriler=[]


    for item in sonuc:


        kutu=item[0]
        yazi=item[1]
        guven=item[2]


        x=int(
            (kutu[0][0]+kutu[2][0])/2
        )


        y=int(
            (kutu[0][1]+kutu[2][1])/2
        )


        veriler.append({

            "text":yazi,
            "x":x,
            "y":y,
            "confidence":float(guven)

        })


    return veriler




def yaziyi_bul(aranan):


    sonuc=ekrani_oku()


    for veri in sonuc:


        if aranan.lower() in veri["text"].lower():

            return veri


    return None