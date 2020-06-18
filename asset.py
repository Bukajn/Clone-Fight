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
imgLatajacaWyspa= resource_path("assets/latajaca_wyspa.png")
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
#sound
soundJump = resource_path("assets/sound/jump.wav")
zbieranieMana_coin = resource_path("assets/sound/zbieraniemany.wav")
soundShoot = resource_path("assets/sound/shootsound.wav")
soundWrogStrzal = resource_path("assets/sound/soundstrzalwroga.wav")
#font
czcionkaRoboto = resource_path("assets/fonts/Roboto-Medium.ttf")