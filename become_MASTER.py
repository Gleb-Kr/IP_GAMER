import socket
from os import listdir

from connectr import listen, send



print("YOU HAVE BECAME THE MASTER!")
agreement = input("Do you think you'll bare this?\n\t").strip().lower()

if agreement == "n" or agreement == "no":
    print("Oh... Okay...")
    quit


mstrHostname = socket.gethostname()
masterIP = socket.gethostbyname(mstrHostname)



print("EVERYONE! A new Master has\n"
      "appeared! They will give you\n"
      "an offer to play. Listen!\n"
      "Also enter Master's IP for\n"
      "security reasons:\n"
     f"{masterIP}")



players = []


print("Enter all player IPs,\n"
      "type DONE, when done\n")

while True:
    playerIP = input().strip().split()
    
    if playerIP[0].lower() == "done":
        break
    else:
        for ip in playerIPs:
            send(ip, "?")
            if listen(ip, answerAmount=1).decode() == "X":
                print(f"Player {ip} declined your offer...")
            else:
                players.append(ip)



print("\x1B[2J\x1BH", end="")


print("Now, Master, you need to pick a"
      "game to play from this list:\n")

for no, game in enumerate(listdir("./games/")):
    print(f"{no}. {game}")


print("")

while True:
    try:
        gameNo = int(input("Game Number:\n\t")) - 1
    
    except ValueError:
        print("Please, enter index, not name")
    
    else:
        if gameNo >= len(listdir("./games/")) or gameNow < 0:
            print("Index is out of range!")
        
        else:
            break



with open("./games/" + listdir("./games/")[gameNo] + "/master.py", "r") as f:
    exec(f.read())



print("Goodbye, Master!")
