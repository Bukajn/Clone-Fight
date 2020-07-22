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

imgZnakAutobusowy = resource_path("assets/ZnakAutobusowy.png")
imgZnakAutobusowyObramowka = resource_path("assets/ZnakAutobusowyObramowka.png")

imgPoleDialogowe = resource_path("assets/PoleDialogowe.png")

imgTloSamouczek = resource_path("assets/tloSamouczek.png")
imgTloSamouczek2 = resource_path("assets/tloSamouczek2.png")

imgProfessor = resource_path("assets/professor.png")
imgProfessorObramowka =resource_path("assets/professorObramowka.png")

imgKlonowator = resource_path("assets/imgKlonowator.png")
imgKlonowatorObramowka = resource_path("assets/imgKlonowatorObramowka.png")
imgKlonowatorUruchomiony = resource_path("assets/imgKlonowatorUruchomiony.png")

imgJablko = resource_path("assets/jablko.png")

imgWieza = resource_path("assets/wieza.png")
imgwiezaObramowka=resource_path("assets/wiezaObarmowka.png")
imgWiezaAktywowana=resource_path("assets/wiezaAktywowana.png")

imgRight1 = resource_path("assets/walkingRight/1.png")
imgRight2 = resource_path("assets/walkingRight/2.png")
imgRight3 = resource_path("assets/walkingRight/3.png")
imgRight4 = resource_path("assets/walkingRight/4.png")
imgRight5 = resource_path("assets/walkingRight/5.png")
imgRight6 = resource_path("assets/walkingRight/6.png")

imgLeft1 = resource_path("assets/walkingLeft/1.png")
imgLeft2 = resource_path("assets/walkingLeft/2.png")
imgLeft3 = resource_path("assets/walkingLeft/3.png")
imgLeft4 = resource_path("assets/walkingLeft/4.png")
imgLeft5 = resource_path("assets/walkingLeft/5.png")
imgLeft6= resource_path("assets/walkingLeft/6.png")

imgEnemyRight1 = resource_path("assets/enemywalkingRight/1.png")
imgEnemyRight2 = resource_path("assets/enemywalkingRight/2.png")
imgEnemyRight3 = resource_path("assets/enemywalkingRight/3.png")
imgEnemyRight4 = resource_path("assets/enemywalkingRight/4.png")
imgEnemyRight5 = resource_path("assets/enemywalkingRight/5.png")
imgEnemyRight6 = resource_path("assets/enemywalkingRight/6.png")

imgEnemyLeft1 = resource_path("assets/enemywalkingLeft/1.png")
imgEnemyLeft2 = resource_path("assets/enemywalkingLeft/2.png")
imgEnemyLeft3 = resource_path("assets/enemywalkingLeft/3.png")
imgEnemyLeft4 = resource_path("assets/enemywalkingLeft/4.png")
imgEnemyLeft5 = resource_path("assets/enemywalkingLeft/5.png")
imgEnemyLeft6 = resource_path("assets/enemywalkingLeft/6.png")
#sound
soundJump = resource_path("assets/sound/jump.wav")
zbieranieMana_coin = resource_path("assets/sound/zbieraniemany.wav")
soundShoot = resource_path("assets/sound/shootsound.wav")
soundWrogStrzal = resource_path("assets/sound/soundstrzalwroga.wav")
soundClick = resource_path("assets/sound/clicksound.wav")

soundDoor = resource_path("assets/sound/soundDoor.wav")
soundBed = resource_path("assets/sound/soundBed.wav")
soundPhone = resource_path("assets/sound/soundPhoneCalling.wav")
soundKlonowator = resource_path("assets/sound/soundKlonowator.wav")
soundWin=resource_path("assets/sound/win.wav")
#font
czcionkaRoboto = resource_path("assets/fonts/Roboto-Medium.ttf")