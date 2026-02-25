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
print("Thanks for using my tool!")
print()

print("1 - set time and execute the code")
print("2 - quit")

choose = input("which one: ")

if choose == "1":
    
    try:
        sure = float(input("how many seconds for start: "))
        tekrar = int(input("how many commands: "))
    except ValueError:
        print("ENTER AN A FUCKİNG NUMBER")
        exit()

    komutlar = []

    for i in range(tekrar):
        cmd = input(f"{i+1}. enter command: ")
        komutlar.append(cmd)

    print("\n5Seconds for prepare")
    time.sleep(5)

    print(f"{sure} Waiting the time...")
    time.sleep(sure)

    print("Writing commands...\n")

    for komut in komutlar:
        pyautogui.typewrite(komut, interval=0.05)
        pyautogui.press("enter")
        time.sleep(0.5)

    print("End.")

elif choose == "2":
        print("Goodbye!")
        exit()