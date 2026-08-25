import socket
from os import listdir

from connectr import listen, send



print("YOU HAVE BECAME A PLAYER!")
agreement = input("Do you wanna play?\n\t").strip.lower()

if agreement == "n" or agreement == "no":
    print("Oh.. Okay...")
    quit


plyrHostname = socket.gethostname()
playerIP = socket.gethostbyname(plyrHostname)



masterIP = input("Please, enter Master's IP:\n\t").strip()


gotAccepted = False

def process_offer(sender, ip):
    if sender.recv(1024).decode() == "?":
        wantsToPlay = input("Do you wanna play?\n\t").strip().lower()
        
        if wantsToPlay == "y" or wnatToPlay == "yes":
            send(ip, "V")
            gotAccepted = True
        
        else:
            send(ip, "X")



print("Now, wait for Master's offers\n"
      "If you are tired, then press ^c")

while True:
    try:
        listen(masterIP, do_on_answer=process_offer, answerAmount=1)
        
        if gotAccepted:
            break
    
    except KeyboardInterrupt:
        print("Goodbye, player!")
        quit



with open("./games/" + listdir("./games/")[
        int.from_bytes(listen(masterIP, do_on_answer=get_game_no, answerAmount=1),
        "little")] + "/player.py") as f:
    exec(f.read())



print("Goodbye, player!")
