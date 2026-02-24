import time
import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.01

print(r"""   _____          __                         __            _____  ___________
  /  _  \  __ ___/  |_  ____   _____ _____ _/  |_  ____   /     \ \_   _____/
 /  /_\  \|  |  \   __\/  _ \ /     \\__  \\   __\/ __ \ /  \ /  \ |    __)_ 
/    |    \  |  /|  | (  <_> )  Y Y  \/ __ \|  | \  ___//    Y    \|        \
\____|__  /____/ |__|  \____/|__|_|  (____  /__|  \___  >____|__  /_______  /
        \/                         \/     \/          \/        \/        \/ """)

print("made by: elliot")
print()

print("1 - zaman ayarla ve kodları çalıştır")
print("2 - çık")

choose = input("which one: ")

if choose == "1":
    
    try:
        sure = float(input("kaç saniye sonra başlasın: "))
        tekrar = int(input("kaç komut gireceksin: "))
    except ValueError:
        print("adam akıllı sayı gir.")
        exit()

    komutlar = []

    for i in range(tekrar):
        cmd = input(f"{i+1}. komutu gir: ")
        komutlar.append(cmd)

    print("\nHazırlanman için 5 saniye...")
    time.sleep(5)

    print(f"{sure} saniye bekleniyor...")
    time.sleep(sure)

    print("Komutlar yazılıyor...\n")

    for komut in komutlar:
        pyautogui.typewrite(komut, interval=0.05)
        pyautogui.press("enter")
        time.sleep(0.5)

    print("Bitti.")

elif choose == "2":
    print("çıkılıyor...")
    exit()

else:
    print("geçersiz seçim yaptın.")
