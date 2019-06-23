
from colorama import Fore, init
import gateway1, gateway2, time, os


def CODECHECKER():
    banner = """
    
  {y}.--------[ {g}CODECHECKER CLI {y}]-------------.
  {y}|  {r}- 2 Gateways                          {y}|
  {y}|  {r}- CCN / CVV Checkers                  {y}|
  {y}'----------------------------------------'

   ----------------------------------------
             - CHOOSE GATEWAY - 
   ----------------------------------------
  
  {g}[1] {r} Gateway 1 CCN / CVV (Good on Amazon / Banned 5210 and 510)
  {g}[2] {r} Gateway 2 CVV (5210/510)
  
  """.format(g=Fore.GREEN, r=Fore.LIGHTRED_EX, y=Fore.YELLOW)
    print(banner)
    while True:
        try:
            codechecker = input(Fore.RESET + 'codechecker >>> ')
        except KeyboardInterrupt:
            print(Fore.RED + '\n[-] ' + Fore.RESET + 'Recieved Exit.')
            exit(1)

        if codechecker == "1":
            print()
            print(Fore.YELLOW + "[*] " + Fore.RESET + "Starting Gateway 1...")
            print()
            print("""
        {re}             {g}_____________{re}
        {re}------------{g}[ {r}CODECHECKER {g}]{re}------------
        {re}------------{g}|- {r}GATEWAY 1 -{g}|{re}------------
        {re}---------------------------------------
        """.format(g=Fore.GREEN, r=Fore.RED, re=Fore.RESET))
            ranges = []
            try:
                with open('cc.txt', 'r') as ccs:
                    for x in ccs.read().split('\n'):
                        ranges.append(x)
                print(Fore.YELLOW + "[*] " + Fore.RESET + 'Checking ' + str(len(ranges)) + ' Credit Cards.')
                input(Fore.RESET + "PRESS ANY KEY TO CONTINUE")
                print(Fore.BLUE + "Start Checking at " + str(time.ctime()))
                print(Fore.RESET)
                
                cc = open('cc.txt', 'r')
                credit_cards = cc.read()
                ccEntry = 0

                if not os.path.exists("lives.txt"):
                    live = open("lives.txt", "w+")
                    live.write(" -- LIVES -- \n")
                    live.close()

                for x in credit_cards.split('\n'):
                    ccEntry += 1
                    try:
                        gateway1.StripeAutomate(x, ccEntry, 'Odec', "Rillek")
                    except KeyboardInterrupt:
                        break
            except KeyboardInterrupt:
                pass
            print()
            print(Fore.GREEN + "[+] " + Fore.RESET + "Done on Gateway 1")
            print()

        elif codechecker == "2":
            print()
            print(Fore.YELLOW + "[*] " + Fore.RESET + "Starting Gateway 2...")
            print()
            try:
                gateway2.Checker()
            except KeyboardInterrupt:
                pass
            print()
            print(Fore.GREEN + "[+] " + Fore.RESET + "Done on Gateway 2")
            print()


CODECHECKER()
