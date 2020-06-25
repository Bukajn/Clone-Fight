import os,sys

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#image
imgPlayerRight = resource_path("assets/playerRight.png")
imgPlayerLeft = resource_path("assets/playerLeft.png")
imgPodloze = resource_path("assets/podłoga.png")
imgPodlozeM2 = resource_path("assets/podłogaM2.png")
imgLatajacaWyspa= resource_path("assets/latajaca_wyspa.png")
imgLatajacaWyspaM2 = resource_path("assets/latajaca_wyspaM2.png")
imgManaCoin = resource_path("assets/mana.png")
imgApteczka = resource_path("assets/apteczka.png")
imgRekaRight=resource_path("assets/rekaRight.png")
imgRekaLeft=resource_path("assets/RekaLeft.png")
imgStrzala=resource_path("assets/strzal.png")
imgStrzalaWrog=resource_path("assets/strzalWrog.png")

imgWrogPrawo=resource_path("assets/wrogRight.png")
imgWrogLewo=resource_path("assets/wrogLeft.png")
imgWrogRekaRight = resource_path("assets/rekaWrogRight.png")
imgWrogRekaLeft = resource_path("assets/wrogRekaLeft.png")

imgTytul = resource_path("assets/tytul.png")

imgDrzwi = resource_path("assets/drzwi.png")
imgDrzwiObramowka = resource_path("assets/DrzwiObramowka.png")
imgDrzwiOtwarte = resource_path("assets/DrzwiOtwarte.png")
imgDrzwiOtwarteObramowka = resource_path("assets/DrzwiOtwarteObramowka.png")

imgBed = resource_path("assets/Łóżko.png")
imgBedObramowka = resource_path("assets/LóżkoObramowka.png")

imgPhone = resource_path("assets/telefon.png")
imgPhoneObramowka = resource_path("assets/telefonObramowka.png")

imgPoleDialogowe = resource_path("assets/PoleDialogowe.png")
#sound
soundJump = resource_path("assets/sound/jump.wav")
zbieranieMana_coin = resource_path("assets/sound/zbieraniemany.wav")
soundShoot = resource_path("assets/sound/shootsound.wav")
soundWrogStrzal = resource_path("assets/sound/soundstrzalwroga.wav")
soundClick = resource_path("assets/sound/clicksound.wav")

soundDoor = resource_path("assets/sound/soundDoor.wav")
#font
czcionkaRoboto = resource_path("assets/fonts/Roboto-Medium.ttf")